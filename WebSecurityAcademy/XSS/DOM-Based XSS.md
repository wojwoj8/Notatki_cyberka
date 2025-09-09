Występuje bezpośrednio w przeglądarce, bez wysyłania formularzy ani tworzenia nowych stron. Wykonuje się kiedy kod js przeglądarki działa z inputami albo na interakcji z użytkownikiem.

Przykład:
Kod JS na stronie pobiera dane z parametru `window.location.hash` i zapisuje go na stronie która jest obecnie wyświetlana. Treść `hash` nie jest sprawdzana, co pozwala atajującemu wstrzyknąć kod js w stronę.

Zagrożenia:
Specjalnie spreparowane linki mogę przekierować użytkowników na inną stronę albo wykraść dane z sesji na danej stronie.

Jak sprawdzać ten xss:
- W kodzie źródłowym szukać zmiennych jak window.location.x
- Jak takie zmienne istnieją to zobaczyć jak są przetwarzane i czy wartości są zapisywane w DOM albo przekazywane do niebezpiecznych funkcji jak eval().