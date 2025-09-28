Borken User Authentication - endpoint API pozwala atakującemu na dotęp do bazy danych lub zdobycie wyższych uprawnień niż te które powinien mieć. Głównie jest to wina złej implementacji uwierzytelniania jak niepoprawne zapytania email lub hasła, brak mechanizmów bezpieczeństwa jak tokeny czy nagłówki uwierzytelniające.

Środki ograniczające ryzyko:
- Wymaganie złożonych haseł o wyższej entropii.
- Nie ujawnianie danych uwierzytelniających w żądaniach GET lub POST.
- Silne tokeny JSON Web Tokens (JWT), nagłówki autoryzacyjne itp.
- Uwierzytelniania wieloskładnikowe (tam, gdzie to możliwe), blokady konta lub systemu captcha, aby ograniczyć ataki brute force na poszczególnych użytkowników.
- Upewnie się, że hasła nie są zapisywane w postaci zwykłego tekstu w bazie danych, aby uniknąć przejęcia konta przez atakującego. 

