maps = '''
.rodata:10000A63                 .byte 0x66 # f
.rodata:10000A67                 .byte 0x6C # l
.rodata:10000A6B                 .byte 0x61 # a
.rodata:10000A6F                 .byte 0x67 # g
.rodata:10000A73                 .byte 0x69 # i
.rodata:10000A77                 .byte 0x73 # s
.rodata:10000A7B                 .byte 0x5F # _
.rodata:10000A7F                 .byte 0x4D # M
.rodata:10000A83                 .byte 0x59 # Y
.rodata:10000A87                 .byte 0x5F # _
.rodata:10000A8B                 .byte 0x54 # T
.rodata:10000A8F                 .byte 0x52 # R
.rodata:10000A93                 .byte 0x41 # A
.rodata:10000A97                 .byte 0x50 # P
.rodata:10000A9B                 .byte 0x5F # _
.rodata:10000A9F                 .byte 0x43 # C
.rodata:10000AA3                 .byte 0x41 # A
.rodata:10000AA7                 .byte 0x52 # R
.rodata:10000AAB                 .byte 0x44 # D
.rodata:10000AB3                 .byte 0x3F # ?
.rodata:10000AB7                 .byte 0x5C # 
.rodata:10000ABB                 .byte 0x14
.rodata:10000ABF                 .byte 0x38 # 8
.rodata:10000AC3                 .byte    5
.rodata:10000AC7                 .byte 0x16
.rodata:10000ACB                 .byte 0x6B # k
.rodata:10000ACF                 .byte 0x3F # ?
.rodata:10000AD3                 .byte 0x37 # 7
.rodata:10000AD7                 .byte 0x3A # :
.rodata:10000ADB                 .byte 0x30 # 0
.rodata:10000ADF                 .byte  0xD
.rodata:10000AE3                 .byte 0x31 # 1
.rodata:10000AE7                 .byte 0x3F # ?
.rodata:10000AEB                 .byte 0x28 # (
.rodata:10000AEF                 .byte 0x70 # p
.rodata:10000AF3                 .byte 0x33 # 3
.rodata:10000AF7                 .byte 0x22 # "
.rodata:10000AFB                 .byte 0x27 # '
'''

key_list = [eval(i.split()[2]) for i in maps.split('\n')[1:-1]]

flag = ''
for i in range(19):
    flag += chr(key_list[i]^key_list[i+19])

print flag



