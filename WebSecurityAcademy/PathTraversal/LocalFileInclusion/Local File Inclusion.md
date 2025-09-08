Atak podobny do path traversal, wykorzystuje w PHP funkcje jak: `include, require, include_once, require_once`. Nie jest wyłączne do PHP, też występuje ta  podatność w ASP, JSP, Node.js.

Przykład:
```php
<?PHP 
	include($_GET["lang"]);
?>
```

`http://webapp.thm/index.php?lang=EN.php` ten url pobierze język angielski strony za pomocą żądania GET. zamiast tego EN można podać to `http://webapp.thm/get.php?file=/etc/passwd` i jest podobnie do path traversal tylko bezpośredni dostęp do danych z serwera.

Teraz przykład gdzie jest ograniczenie do folderu `/languages`

```php
<?PHP 
	include("languages/". $_GET['lang']); 
?>
```

Tutaj standardowy path traversal `http://webapp.thm/index.php?lang=../../../../etc/passwd` 

Może być tak, że aplikacja będzie forsować, żeby dany plik był z końcówką np `.php`. Wtedy path będzie taki: `http://webapp.thm/index.php?lang=EN` i będzie on oznaczał dostęp do pliku EN.php. Atak `http://webapp.thm/index.php?lang=../../../../etc/passwd` nie zadziała w tym przypadku bo aplikacja będzie chciała odczytać plik `passwd.php`. Tutaj wchodzi :

**NULL BYTE** - jest on wartością **%00**.

Oznacza on jakby koniec stringa. Ostatnia wartość stringa, dalej już nic nie ma. Ten exploit nie działa w PHP 5.3.4 i dalej.

`http://webapp.thm/index.php?lang=../../../../etc/passwd%00` odczyta plik.

Inny przykład to np. `/etc/passwd` jest filtrowane. Tutaj są 2 podejścia. Pierwsze to znowu dodać na końcu `%00`. Drugie to można w path wpisać `/etc/passwd/.` .

Inna opcja to aplikacja podmienia `../` na pusty string. Obejściem może być stosowanie zamiast `../../../` tego `....//....//....//` bo każde '../' zostanie usunięte i zostanie reszta która i tak pozwoli za zmianę folderu.

Kolejna opcja to, że wymagany jest folder w ścieżce, np. `languages/` to wystarczy dać go na początku ścieżki a dalej standardowo path traversal.

Czasami trzeba atakować po ciasteczkach, POST a nie GET, kiedy POST TRZEBA DODAĆ 
HEADER: `Content-Type: application/x-www-form-urlencoded` albo po curl zrobić zapytanie.

``