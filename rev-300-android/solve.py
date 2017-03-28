from Crypto.Cipher import AES

dat = open('classes.dex','rb').read()

key = ''.join([chr(ord(a)^ord(b)) for a, b in zip(dat[0x67c:0x67c+24],dat[0x694:0x694+24])])
enc = '8Bl8GDuXQJbTQrjT6LfQdw=='.decode('base64')

cipher = AES.new(key[8:], AES.MODE_ECB)
print cipher.decrypt(enc)

