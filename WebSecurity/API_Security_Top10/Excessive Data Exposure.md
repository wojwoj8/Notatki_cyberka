Jak api zwraca za dużo danych niepotrzebnych, np. podczas wyświetlania wpisu na blogu użytkownika to wyświetli się jego lokalizacja, ip, hasło, email itp.

## Zapobieganie
- Nie wysyłać z back-endu zbędnych danych
- Unikać metod generycznych `to_string() `i ` to_json()` 