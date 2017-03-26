## Solve
- wireshark 에서 filter를 **usb.transfer_type == 0x01** 로 지정한 뒤, 패킷을 보면 몇 개 없다.
- 따라서 Leftover Capture Data를 python 배열에 한개씩 집어넣고, 구글링해서 얻은 딕셔너리에 키 값에 맞게 매칭해주었다.
- 앞에 20이 붙는 경우는 Shift를 눌린거라 -를 _로 해주면 플래그가 출력된다.

```python
#usb.transfer_type == 0x01

maps = {
0x04:"A",0x05:"B",0x06:"C",0x07:"D",0x08:"E",
0x09:"F",0x0A:"G",0x0B:"H",0x0C:"I",0x0D:"J",
0x0E:"K",0x0F:"L",0x10:"M",0x11:"N",0x12:"O",
0x13:"P",0x14:"Q",0x15:"R",0x16:"S",0x17:"T",
0x18:"U",0x19:"V",0x1A:"W",0x1B:"X",0x1C:"Y",
0x1D:"Z",0x1E:"1",0x1F:"2",0x20:"3",0x21:"4",
0x22:"5",0x23:"6",0x24:"7",0x25:"8",0x26:"9",
0x27:"0",0x28:"\n",0x2C:" ",0x2D:"-",0x2E:"=",
0x2F:"[",0x30:"]"
}

key = ['13', 'f', '21', '1c', '2d', '17', 'b', '20', '2d', 'e', '20', '1c', '5', '27', '4', '15', '7', '2c', '2c', '2c']

flag = ''
for i in key:
    flag += maps[int(i, 16)]

print flag.replace('-', '_').lower()
```

## Result

```
 ~/ctf/doubles_ctf/for-100-AIkeyboard/ [master*] python solve.py
pl4y_th3_k3yb0ard
```
