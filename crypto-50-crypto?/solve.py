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
