## solve
* 그냥 p,q,e를 주기 때문에 조건에 맞게 decrypt를 하고, 다시 base64 decode를 하고, 다시 hex값으로 decode한 값을 보내면 서버에서 flag를 보내준다.

</br>
## Result

```
~/machome/ctf/doubles_ctf/crypto-150-rsa(master*) » python solve.py                                  stitch@certis
[+] Opening connection to 203.251.182.94 on port 4000: Done
0x4d7a55344f5449314d4441314d44517a4d4449344e4463794e7a49324e7a59354e7a45304d546b334e4467354f4451334f5451334e4463774e6a59314d7a4d324d6a63324e4445354e446b314d4445324e6a63784e7a49324d5449794f54417a4f5467314e7a673d
OZotWSO2qIHqCk5w00aTSkpVzqT56DIr
[*] Switching to interactive mode
flag{Y34hh_RSA_1S_S0_E4sy}
[*] Got EOF while reading in interactive
$
```
