Command injection inaczej RCE - wykonywanie kodu na systemie z wykorzystaniem pozwoleń atakowanej aplikacji. Przykład - włamuję się na aplikację internetową i dostaję dostęp do systemu z pozwoleniami www-data.

Istnieją dwa rodzaje:
- blind - nie ma bezpośredniego outputu jak się testuje wysyłanie payloadów.
- verbose - po wysłaniu payloadu otrzymujemy wynik.

# Wykrywanie blind injection:

Dla tego typu trzeba wykorzystywać do payloadu polecenia trwające jakiś czas np. `sleep`  lub `ping`. W tym przypadku jak odpowiedź serwera by trwała np. 5s a nie 1s po poleceniu ping to wiadomo że działa.

Inna metoda to np użycie operatorów przekierowań `>` do wymuszenia przekierowania odpowiedzi polecenia do pliku i wyczytanie go potem np. za pomocą `cat`.

`curl` jest dobrym poleceniem do testowania tej podatności z racji na możliwość wysłania danych z i do serwera.

# Przydatne polecenia do detekcji

Linux

|             |                                                                                                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Payload** | **Description**                                                                                                                                                                                                      |
| whoami      | See what user the application is running under.                                                                                                                                                                      |
| ls          | List the contents of the current directory. You may be able to find files such as configuration files, environment files (tokens and application keys), and many more valuable things.                               |
| ping        | This command will invoke the application to hang. This will be useful in testing an application for blind command injection.                                                                                         |
| sleep       | This is another useful payload in testing an application for blind command injection, where the machine does not have `ping` installed.                                                                              |
| nc          | Netcat can be used to spawn a reverse shell onto the vulnerable application. You can use this foothold to navigate around the target machine for other services, files, or potential means of escalating privileges. |
Windows

|   |   |
|---|---|
|**Payload**|**Description**|
|whoami|See what user the application is running under.|
|dir|List the contents of the current directory. You may be able to find files such as configuration files, environment files (tokens and application keys), and many more valuable things.|
|ping|This command will invoke the application to hang. This will be useful in testing an application for blind command injection.|
|timeout|This command will also invoke the application to hang. It is also useful for testing an application for blind command injection if the `ping` command is not installed.|

# Zapobieganie

Unikanie potencjalnie niebezpiecznych bibliotek, filtrowanie i nie ufanie danym z front-endu, omijanie niebezpiecznych funkcji jak `exec, eval, passthru, system`

Jak aplikacja ma filtry znaków np `";&` to można próbować obejść to wpisując np wartości hex tych znaków.


# Lista przydatnych payloadów
https://github.com/payloadbox/command-injection-payload-list