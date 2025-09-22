
`getcap` - pozwala na zobaczenie "capabilities (możliwości?)" plików. Trochę inne niż SUID i GUID, podobno bezpieczniejsze niż one.

Definicja: specjalne atrybuty które mogą zostać przypisane do procesów, plików itp., które umożliwiają korzystanie z konkretnych specjalnych pozwoleń.

`getcap -r / 2>/dev/null`

Skan coś jak `find / -perm 4000 2>/dev/null` ale nie działa na tych specjalnych bitach tylko tych możliwościach?

https://steflan-security.com/linux-privilege-escalation-exploiting-capabilities/