### SSL/TLS Workflow

SSL/TLS handshake is performed to encrypt the communication between client and server through the following steps:

1. Client Hello Message: The client sends a hello message to the server; it includes the client TLS version and the cypher suite that the client supports, in addition to random bytes.
2. Server Hello Message: The server responds with a hello message, highlighting its certificate, chosen cypher suite and random bytes.
3. Authentication: The client authenticates the server’s certificate through the certificate authority that issued it. For example, when we visit [Google](https://www.google.com/), Google shares its certificate. The received certificate is verified by our browser, which is pre-installed with the certificates of various certificate authorities.
4. Premaster Secret: The client encrypts random bytes with the server’s public key. (The client retrieves the public key from the server’s certificate.)
5. Decryption of Premaster: The server decrypts the premaster with its private key.
6. Session Keys Generated: The client and the server generate session keys based on client random bytes, random server bytes and premaster secret. Both will arrive at the same results; **this session key is not transmitted**, and encryption and decryption are based on this key.
7. Ready Messages: The client and server send a “finished” message using the session key to indicate that the session is ready for transmission. The client and server are now ready to exchange messages over SSL/TLS encrypted connection.

### SOCKS5 protocol

Socket Secure (SOCKS) - protokół proxy dla wymiany pomiędzy serwerami. Wykorzystywany jest przez secure aplication layer protocols.

Działanie - zakładając scenariusz gdzie user A chce się połączyć z userem B przez internet ale stoi firewall między nimi:

- **Client Initiation**
    - Client A connects with the SOCKS5 proxy and sends the first byte (0x05) to the proxy where “5” is the SOCKS version.
    - Client A sends a second byte (0x01). One means authentication is supported.
    - Client A sends the third byte (0x00, 0x01, 0x02, or 0x03); these bytes denote the supported authentication methods and can be of variable length.
- **SOCKS5 Proxy Reply**
    - The proxy sends back a second byte, which is the chosen authentication method by the proxy server.
    - After the initiation packet, client A sends the request packet, which includes BHOST & BPORT numbers.
    - The successful session is established between client A and the proxy. The same steps are involved in the association of client B with the proxy.
- **Data Transfer**
    - After successfully associating both clients with a proxy server, both clients can exchange data and share information that will be routed through the proxy server.

![](Attatchments/Pasted%20image%2020251106141945.png)

Zalety;
- w bezpośredniej komunikacji przez serwer proxy ukrywa wewnętrzne detale z routingu przez internet
- Serwer proxy działa jak serwer pośredniczący, omijając cenzurę internetową opartą na adresie IP klienta.


### IPsec

IPsec uses the following protocols:

1. Authentication Header (AH): Provides authentication and integrity.
2. Encapsulating Security Payload (ESP): Provides authentication, integrity, and confidentiality.
3. Security Association (SA): Is responsible for negotiating the encryption keys and algorithms. One example is Internet Key Exchange (IKE). Discussing SA in more detail is outside the scope of this room.

AH nie zapewnia poufności danych.
Authentication header działa w dwóch trybach:
- Transport mode - zapewnia uwierzytelnianie dla nagłówków tcp/udp i danych
- Tunnel mode - zapewnia uwierzytelnianie dla nagłówków IP i tego co transport mode.  

![](Attatchments/Pasted%20image%2020251106163752.png)


### Encapsulating security payload (ESP)

Zapewnia szyfrowanie w dodatku do uwierzytelniania i integranlości, działa w dwóch trybach:
1. Transport Mode: Provides security (confidentiality and integrity) for the TCP/UDP header and data.
2. Tunnel Mode: Provides security (confidentiality and integrity) for the IP header, TCP/UDP header, and data.

![](Attatchments/Pasted%20image%2020251106164019.png)

