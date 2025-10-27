Digital Forensics and Incident Response - zbieranie danych z komputerów, telefonów itp. w celu śledztwa po jakimś zdarzeniu.

## Koncepty

### Artifacts

Są one częściami dowodów wskazujących na jakąś aktywność w systemie, np edycja rejestrów w Windowsie

### Evidence preservation

Zabezpieczenie dowodów, np. danie write-only na zebrane dane, zrobienie pełnej kopii systemu itp.

### Chain of custody

Zbieranie dowodów w sprawie zapewniając ich integralność

### Order of volatility

Skupienie się na danych które mogą zostać w pierwszej kolejnośći utracone, np. RAM. 

### Timeline creation

Ustrukruryzowanie zebranych dowodów w historię, co, gdzie, kiedy, i jak.

## Normy incident response

Different organizations have published standardized methods to perform Incident Response. NIST has defined a process in their [SP-800-61 Incident Handling guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf), which has the following steps:
1. Preparation
2. Detection and Analysis
3. Containment, Eradication, and Recovery
4. Post-incident Activity

Similarly, SANS has published an [Incident Handler's handbook](https://www.sans.org/white-papers/33901/). The handbook defines the steps as follows:
1. Preparation  - Przed incydentem, jest to przygotowanie na to że taki może się zdarzyć
2. Identification - Identyfikacja i sprawdzenie czy false positive oraz przekazanie dalej.
3. Containment - ograniczenie skutków ataku
4. Eradication - Wyzbycie się ataku 
5. Recovery - Powrót systemów do działania
6. Lessons Learned - Dokumentacja i przygotowanie na taki incydent.

To można zapamiętać skrótem PICERL.