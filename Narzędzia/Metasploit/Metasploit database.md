Ustawienie bazy danych pozwoli na prostsze zarządzanie gdy atakowane jest kilka celów.

Odpalenie bazy danych: `systemctl start posgresql`

Inicjalizacja bazy metasploit `msfdb init`, czasami może być tak że pokaże że jako non-root trzeba to wtedy - `sudo -u postgres msfdb init`

Usunięcie bazy - `sudo msfdb delete`

Sprawdzenie stanu bazy danych w msfconsole - `db_status`

Tworzenie oddzielnych środowisk do konkretnych projektów -  `workspace`,:
- `-a nazwa_środowiska` - tworzenie środowiska
- `-d nazwa_środowiska` - usunięcie

Jak włączono z bazą danych metasploit to pod `help` znajdą się polecenia związane z bazą.

`db_nmap` - uruchomienie polecenia z db_nmap zadziała jak nmap, tylko zapisze wynik w bazie.

`hosts` i `services` - pokaże zebrane informacje o celu.

`hosts -h` i `services -h` - więcej informacji

`hosts -R` - jak jest informacja o ip celu to doda to jego ip do RHOSTS, jak jest więcej ip to wszystkie zostaną dodane.