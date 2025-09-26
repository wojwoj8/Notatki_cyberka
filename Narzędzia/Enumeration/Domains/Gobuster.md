Wyszukiwanie podfolderów na stronie:
`gobuster dir -u IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
`

## Przykład

```
gobuster dir -w=/usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -u=http://lookup.thm -x .php, .html, .js -k
```
