## Solve
- 문자열 중간중간에 [숫자] 이런것들이 있는데 그런것들만 따로 뽑아서 아스키값으로 바꿨다. </br>글의 내용이 시저에 대한 내용이였기 때문에 시프트를 하다가 보니 중괄호 사이에 약간 말되는 것이 보여서 인증했는데 안됬다. +를 n으로 하니까 인증이 제대로 됬다.

```python
import re
import string

def caesar_enc(key, msg):
    print ''.join(map(chr, [((ord(i)+key-ord('a'))%26)+ord('a') if ord('a')<=ord(i)<=ord('z') else ord(i) for i in msg]))

dat = open('Crypto.txt','r').read()
s = re.findall('\[[\d]{2,3}\]', dat)

out = ''
for i in s:
    out += chr(eval(i.strip('[]')))

caesar_enc(11, out.lower())
```
</br>

## Result

```
~/machome/ctf/doubles_ctf/crypto-50-crypto?(master*) » python solve.py                               stitch@certis
{c0+gratz_y0u_3olve_1t}i& !"#$%&'(
```
