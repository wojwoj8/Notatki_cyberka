
# Telnet

Port TCP/23 - to co ssh tylko nie szyfrowane. Można łączyć się do różnych serverów (nie korzystających z szyfrowania) jak http czy smtp.

# HTTP

Port TCP/80

Popularne servery:
- Apache
- Internet Information Services(ISS)
- nginx

# FTP

 Port TCP/21 - do przesyłania danych (jawnie) Może działać w dwóch trybach:
 - Active - dane są wysyłane prez inny kanał z portu 20 serwera
 - Passive - dane są wysyłane przez inny kanał zaczynając od portu ftp klienta powyżej 1023.
Wysyłanie plików to nowe połączenie. Dane idą innym kanałem niż "control channel", który jest na porcie TCP/21

Serwery FTP:
- [vsftpd](https://security.appspot.com/vsftpd.html)
- [ProFTPD](http://www.proftpd.org/)
- [uFTP](https://www.uftpserver.com/)

# SMTP

TCP/25 - protokół do wysyłania emaili

![](Attachments/{1B1755B6-695A-42D8-9876-DE797B82BA0B}.png)
1. A Mail User Agent (MUA), or simply an email client, has an email message to be sent. The MUA connects to a Mail Submission Agent (MSA) to send its message.
2. The MSA receives the message, checks for any errors before transferring it to the Mail Transfer Agent (MTA) server, commonly hosted on the same server.
3. The MTA will send the email message to the MTA of the recipient. The MTA can also function as a Mail Submission Agent (MSA).
4. A typical setup would have the MTA server also functioning as a Mail Delivery Agent (MDA).
5. The recipient will collect its email from the MDA using their email client.

SMTP jest wykorzystywane w celu połączenia się z serverem MTA. Nie szyfruje danych.

# POP3

Port TCP/110 - Wykorzystywany do pobierania emaili z serwera MDA (mail delivery agent), może też uwierzytelniać i usuwać wiadomości. Typowy klient email. Nie szyfruje danych

# IMAP

Port TCP/143 - bardziej skomplikowany niż POP3, pozwala na synchronizację emaili na różnych urządzeniach i klientach email. Innymi słowy np. oznaczy email jako przeczytany na komputerze jak odczytam go na telefonie. Nie szyfruje danych