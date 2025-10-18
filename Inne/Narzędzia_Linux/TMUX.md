Tmux - terminal multiplexer - działa w tle a jak jest sesja to nawet jak się terminal wyłączy
https://tmuxcheatsheet.com 
### Sterowanie

ctrl+b - tryb wyboru funkcji 

ctrl+b c - nowe okno

Mój setup ma ctrl+s jako ten wybór

% - splituje obraz horyzontalnie

" - wertykalny split

strzałki - wybór między tymi oknami (splity)

d - detatch (wyjście z tmux ale sesja zostaje)

tmux ls - wyświetlenie sesji (bez tego ctrl, normalnie w shellu)

tmux attatch - przywrócenie sesji

Jak detatched to tmux i nowa sesja ale tamta dalej istnieje.

s - lista sesji

: - polecenia można wpisywać

### Polecenia
: i polecenie

rename-window nazwa - zmiana nazwy okna

rename-session nazwa - nazwa sesji


### Moje bindy

prefix - ctrl + s

r - restart ustawień 

I - (duże i) instalacja pluginów

Zapisywanie sesji z tmux-ressurect
- `prefix + Ctrl-s` - save
- `prefix + Ctrl-r` - restore