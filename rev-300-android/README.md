# Solve
- **대회때는 이문제 못봄ㅋ**
- 일반적인 dex2jar 로는 숨겨진 함수가 보이지않는다.
- IDA로 dex파일을 열어서 c로 decrypt를 해주면 AES 암호 루틴이 보인다.
```
CODE:000005D4 # Method 0 (0x0)
CODE:000005D4                 move-wide/16                    v0:v1, v3:v4 # Number of registers : 0x6
CODE:000005DA                 nop                     # Number of try_items : 0x0
CODE:000005DC                 invoke-direct                   {}, <void PrintStream.println(ref) imp. @ _def_PrintStream_println@VL> # Debug info
CODE:000005E2                 nop
CODE:000005E4                 const/16                        v0, 0x10
CODE:000005E8                 .prologue_end
CODE:000005E8                 .line 88
CODE:000005E8                 new-array                       v1, v0, <t: byte[]>
CODE:000005EC                 fill-array-data                 v1, word_67C
CODE:000005F2                 .line 90
CODE:000005F2                 new-array                       v2, v0, <t: byte[]>
CODE:000005F6                 fill-array-data                 v2, word_694
CODE:000005FC                 .line 92
CODE:000005FC                 new-instance                    v3, <t: StringBuilder>
CODE:00000600                 invoke-direct                   {v3}, <void StringBuilder.<init>() imp. @ _def_StringBuilder__init_@V>
CODE:00000606                 .line 94
CODE:00000606                 const/4                         v0, 0
CODE:00000608
CODE:00000608 loc_608:                                # CODE XREF: CODE:00000624j
CODE:00000608                 array-length                    v4, v1
CODE:0000060A                 if-ge                           v0, v4, loc_626
CODE:0000060E                 .line 96
CODE:0000060E                 aget-byte                       v4, v1, v0
CODE:00000612                 aget-byte                       v5, v2, v0
CODE:00000616                 xor-int/2addr                   v4, v5
CODE:00000618                 .line 97
CODE:00000618                 int-to-char                     v4, v4
CODE:0000061A                 invoke-virtual                  {v3, v4}, <ref StringBuilder.append(char) imp. @ _def_StringBuilder_append@LC>
CODE:00000620                 .line 94
CODE:00000620                 add-int/lit8                    v0, v0, 1
CODE:00000624                 goto                            loc_608
CODE:00000626 # ---------------------------------------------------------------------------
CODE:00000626
CODE:00000626 loc_626:                                # CODE XREF: CODE:0000060Aj
CODE:00000626                 .line 100
CODE:00000626                 new-instance                    v0, <t: SecretKeySpec>
CODE:0000062A                 new-instance                    v1, <t: String>
CODE:0000062E                 invoke-direct                   {v1, v3}, <void String.<init>(ref) imp. @ _def_String__init_@VL>
CODE:00000634                 invoke-virtual                  {v1}, <ref String.getBytes() imp. @ _def_String_getBytes@L>
CODE:0000063A                 move-result-object              v1
CODE:0000063C                 const-string                    v2, aAes # "AES"
CODE:00000640                 invoke-direct                   {v0, v1, v2}, <void SecretKeySpec.<init>(ref, ref) imp. @ _def_SecretKeySpec__init_@VLL>
CODE:00000646                 .line 101
CODE:00000646                 const-string                    v1, aAesEcbPkcs5pad # "AES/ECB/PKCS5Padding"
CODE:0000064A                 invoke-static                   {v1}, <ref Cipher.getInstance(ref) imp. @ _def_Cipher_getInstance@LL>
CODE:00000650                 move-result-object              v1
CODE:00000652                 .line 102
CODE:00000652                 const-string                    v2, a8bl8gduxqjbtqr # "8Bl8GDuXQJbTQrjT6LfQdw=="
CODE:00000656                 .line 104
CODE:00000656                 const/4                         v3, 2
CODE:00000658                 invoke-virtual                  {v1, v3, v0}, <void Cipher.init(int, ref) imp. @ _def_Cipher_init@VIL>
CODE:0000065E                 .line 105
CODE:0000065E                 invoke-static                   {v2}, <ref DatatypeConverter.parseBase64Binary(ref) imp. @ _def_DatatypeConverter_parseBase64Binary@LL>
CODE:00000664                 move-result-object              v0
CODE:00000666                 invoke-virtual                  {v1, v0}, <ref Cipher.doFinal(ref) imp. @ _def_Cipher_doFinal@LL>
CODE:0000066C                 move-result-object              v0
CODE:0000066E                 .line 106
CODE:0000066E                 new-instance                    v1, <t: String>
CODE:00000672                 invoke-direct                   {v1, v0}, <void String.<init>(ref) imp. @ _def_String__init_@VL_0>
CODE:00000678                 .line 107
CODE:00000678                 return-void
```

- 보이는 대로 그냥 복호화코드 짜면된다. ECB방식은 iv가 없기 때문에 간단하게 복호화가 된다.

```python
from Crypto.Cipher import AES

dat = open('classes.dex','rb').read()

key = ''.join([chr(ord(a)^ord(b)) for a, b in zip(dat[0x67c:0x67c+24],dat[0x694:0x694+24])])
enc = '8Bl8GDuXQJbTQrjT6LfQdw=='.decode('base64')

cipher = AES.new(key[8:], AES.MODE_ECB)
print cipher.decrypt(enc)
```


# Result
```
~/machome/ctf/doubles_ctf/rev-300-android(master*) » python solve.py                 stitch@certis
fl4g_1s_33k_3ck
```
