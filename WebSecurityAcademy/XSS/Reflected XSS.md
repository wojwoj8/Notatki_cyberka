Występuje kiedy dane podane użytkownika w żądaniu http są zawarte w źródle strony bez walidacji. np. strona pokazuje że użytkownik o nicku "qwerty" istnieje kiedy chcemy zmienić username, można wpisać zamiast tego skrypt.

Przykład: Atakujący może wysłać linka z wbudowanym iframe na innej stronie zawierającym JS payload do ofiar, co po wejściu w link spododuje wykonanie kodu w ich przeglądarce np. do kradzieży ciasteczek

Może wystąpić w:
- Parametrze url
- ścieżce url
- czasami w nagłówkach http (mało prawdopodowne w praktyce)
