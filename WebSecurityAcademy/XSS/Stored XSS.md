Jest w bazie danych strony, np. nazwa użytkownika ze złośliwym kodem. Każdy użytkownik któremu wyświetli się ta nazwa, np w poście na forum to wykona się u niego ten kod.

Występowanie:
- komentarze na blogach
- Informacje na profilu użytkownika

Może wystąpić **Blind XSS**, nie będzie widać że payload zadziałał, albo będzie tylko działał tylko na innych.

Przykład:
- Można napisać ticket do supportu ze złośliwym kodem i dopiero administrator który ma dostęp do ticketów zobaczy tę wiadomość.

Jak testować blind XSS:
- trzeba się upewnić że wysłanie payloadu spowoduje odpowiedź http servera co będzie oznaczać że payload został wysłany.

Popularnym narzędziem do testowania tego xss jest XSS Hunter Express.