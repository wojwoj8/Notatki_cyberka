Select - pobieranie danych
Union - łączenie np. kilku select w jednym
Delete - delete
Upadate - update
Insert - insert

# Działanie w url

W url na końcu zapytania danie `;--` oznacza że reszta zapytania jest nie ważna (jest komentarzem).

# In-Band SQL injection

SQLi które zwraca na stronie odpowiedź po wykorzystaniu podatności

# Error-Based SQL Injection

SQLi bazujące na błędach, np. enumeracja użytkowników systemu poprzez zakładanie konta z zajętą nazwą użytkownika i obserwanie czy jest błąd że taki użytkownik istnieje.

# Union-Based SQL Injection

Wykorzystuje union wraz z select w celu zwrócenia dodatkowych danych na stronie. 


Za pomocą UNION SELECT 1,2,3  - można wyznaczyć ilość kolumn w tabeli.

Podobnie można bazować na czasie odpowiedzi
`admin123' UNION SELECT SLEEP(5);--` to sprawdzi ilość kolumn na podstawie czasu odpowiedzi, jak odpowiedź natychmiastowa to złe zapytanie ale np. `admin123' UNION SELECT SLEEP(5),2;--` może już trwać 5s to wiadomo że istnieje 2 kolumny.

`where database() like '%';--` - sprawdzenie nazwy bazy danych w '%' zamiast tego wpisać znak jakiś `'a%'` to sprawdzi nazwę na a i tak dalej iterować

`UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--` union select 1,2,3 zwraca true po tyle kolumn jest, dalej to information_schema.tables zawiera listę nazw tabel, table schema to nazwa bazy danych, table name to nazwa tabeli i też można iterować.
Identyczny przykład jest z kolumnami, `information_schema.COLUMNS` jako kolumny i `column_name like` jako nazwa kolumny.

**WAŻNE, jak majstrowanie przy url `https://website.thm/analytics?referrer=admin123' UNION SELECT SLEEP(1),2 from users where username='admin' and password like'%` to na końcu bez tego apostrofa trzeba dać!!!!**
