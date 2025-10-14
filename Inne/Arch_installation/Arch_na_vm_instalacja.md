
[instrukcja po polsku](https://wiki.archlinux.org/title/Installation_guide_(Polski))

Najpierw ustawienie klawiatury polskiej i czcionki z polskimi znakami

``` zsh
loadkeys pl
setfont Lat2-Terminus16
```

Dalej sprawdzenie czy jest legacy BIOS czy UEFI

```
cat /sys/firmware/efi/fw_platform_size
```

Jak nic nie ma to jest bios

Warto sprawdzić czy działa internet pingiem

Aktualizacja zegara 

```
timedatectl
```

## Format partycji

Wyświetlenie dysków jest za pomocą `fdisk -l` i dalej tworzenie partycji to:

Dalej wybieramy dysk `fdisk /dev/coś/dysk1`

PARTYCJE POWINNY BYĆ 2-3 MINIMUM:
1. na pliki
2. na swap (min 4GiB jest ale nie wiem czy więcej nie trzeba)
3. EFI jak jest UEFI 

Dalej serwery z których będą instalowane pakiety są w `/etc/pacman.d/mirrorlist`

Skrypt który sam to ustawi pod Polskę:

```
sudo reflector --country Poland --latest 5 --protocol http --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```

Instalacja podstawowych pakietów:

```
pacstrap -K /mnt base linux linux-firmware
```

Update pacmana

```
pacman -Syu
```

## Konfiguracja systemu

Generowanie pliku fstab - do montowania dysków i partycji

```
genfstab -U /mnt >> /mnt/etc/fstab
```

Dalej wejście na zainstalowany system

```
arch-chroot /mnt
```

###  Reszta paczek do pobrania

[TUTAJ RESZTA BYĆ MOŻE POTRZEBNYCH PACZEK DO POBRANIA](https://wiki.archlinux.org/title/Installation_guide_(Polski)#Instalacja_podstawowych_pakiet%C3%B3w)

Najpierw zainstalowałem wget i dalej wget pobrałem sugerowaną listę paczek:

```
https://geo.mirror.pkgbuild.com/iso/latest/arch/pkglist.x86_64.txt
```

Dalej instalacja tych paczek:

```
pacman -S $(awk '{print $1}'  input_file)
```

Ustawienie strefy czasowej:

```
ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
```

## Ustawienie języków systemu

w `/etc/locale.gen` trzeba odkomentować języki, tutaj:

```
en_US.UTF-8 UTF-8
pl_PL.UTF-8 UTF-8
```

Następnie `locale-gen` wygeneruje obsługę języków.
Dalej w `/etc/locale.conf` trzeba dopisać język: 

```
LANG=pl_PL.UTF-8
```

Układ klawiatury w `/etc/vconsole.conf` i terminal z polskimi znakami:

```
KEYMAP=pl
FONT=Lat2-Terminus16
FONT_MAP=8859-2
```

Zmiana nazwy hosta w sieci `/etc/hostname`

```
nazwa
```

Ustawienie hasła dla roota: `passwd`

## Boot loader

[Instrukcja](https://wiki.archlinux.org/title/Arch_boot_process#Boot_loader)

Trzeba zainstalować grub: 

```
pacman -S grub os-prober
```

Ten os-prober to usefull jak się na dualboot instaluje bo wykrywa inny system.

Dalej instalacja GRUB na dysku - TUTAJ WAŻNE TO JEST NA BIOS NIE UEFI

```
grub-install --target=i386-pc /dev/sda
```

Też ważne tutaj to i386-pc to oznaczenie biosu przez grub, nie jest to architektura systemu, dodatkowo to /dev/sda bez cyfry - to instaluje po prostu na dysku.

Config file dla GRUB:

```
grub-mkconfig -o /boot/grub/grub.cfg
```

Jak mam os-prober to samo doda inny system do tej konfiguracji

Dalej `exit` i potem `umount -R /mnt` i `reboot`. Jak wszystko wcześniej było git to powinien odpalić się system (logowanie do roota).