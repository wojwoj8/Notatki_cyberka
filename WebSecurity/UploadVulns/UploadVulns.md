## Bypassing Client-Side Filtering

Można ominąć filtrowanie po froncie uploadów (np. zdjęć) na kilka sposobów:
1. wyłączenie w przeglądarce JS
2. przechwycenie zapytanie w burp intercep i usunięcie filtra js
3. przechwycenie w burp zapytania i edycja uploadu tak żeby przeszedł
4. wysłanie bezpośrednio do celu uploadu za pomocą np. `curl`, coś jak `curl -X POST -F "submit:<value>" -F "<file-parameter>:@<path-to-file>" <site>`

Ważne - burp domyślnie nie przechwytuje JS i trzeba w opcje i pod "Intercept Client Requests" i trzeba pod pierwszą linią usunąć wpis `^js$|`

![](Attachments/{F53C5455-C46E-4C40-8E3F-1605C7556BBF}.png)

## Bypassing Server-Side Filtering: File Extensions

Można próbować wgrywać różne rozszerzenia plików. Np. jest blacklista na .php i .phtml. PHP akceptuje też inne rozszerzenia jak: `.php3`, `.php4`, `.php5`, `.php7`, `.phps`, `.php-s`, `.pht` i podanie owego ominie ten filtr na rozszerzenia. Może też być tak że np. działa tylko jpg to można próbować wysłać `plik.jpg.php`, kod wychwyci że jest `.jpg` i przepuści.


## Bypassing Server-Side Filtering: Magic Numbers

Magic numbers to ciąg znaków na początku pliku określający jego rozszerzenie
[Lista rozszerzeń (sygnatur)](https://en.wikipedia.org/wiki/List_of_file_signatures)
Prosty sposób na oszukanie filtra:
1. Mamy plik z np. reverse shell i go odpalamy w vim i dodajemy na samym początku `AAAA`
![](Attachments/{9B3A37B4-F81C-4524-8EE3-D65E3F971A1B}.png)
Dalej w hexeditor edytujemy te pierwsze 4 bajty
Przed edycją:![](Attachments/{1B08B4FC-8EE8-4743-8AEC-97D706B47142}.png)
Po edycji (sygnatura JPEG):
![](Attachments/{3196D771-1EE9-4903-AA63-C5AFA2DF51C6}.png)
Po edycji:
![](Attachments/{96A2EF11-22A6-4FCB-9413-10B3F0B68DA9}.png)
Wrzucenie tego da reverse shell.