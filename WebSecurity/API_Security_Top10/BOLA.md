Broken object level authorisation - Użytkownik wykorzystuje input i dostaje dostęp do zasobów do których nie ma autoryzowanego dostępu (coś jak IDOR), z reguły kontrola tego jest w modelu MVC.

## Przykład

`http://localhost:80/MHT/apirule1_s/user/{id}` tutaj nie jest weryfikowane czy wpiszę w id 1 czy 2. Rozwiązaniem jest dodanie Authorization-Token Header.
``