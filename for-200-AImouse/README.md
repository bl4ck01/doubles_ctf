# Solve
- 예전에 이런 류의 문제를 푼적이 있어서 킵해놓은 코드와 구글링을 통해 풀 수 있었다.
- tshark를 이용해서 pcap파일에서 필요한 데이터만 빼온다.

```
tshark -r mouse.pcap -T fields -e usb.capdata > data.txt
```

- 그리고 난 뒤, 이 정보에서 좌표정보만 빼서 그림으로 그려주는 코드에 넣으면 된다.

```python
from bokeh.plotting import figure, output_file, show

data = eval(str(filter(lambda x : len(x)==11, open('data.txt','r').read().strip('\n').split('\n'))).replace(':',''))

xf = 0
yf = 0
clicksx = []
clicksy = []

for i in data:
        x = int(i[2:4], 16)
        if x >= 1<<7:
            x -= 1<<8
        y = int(i[4:6], 16)
        if y >= 1<<7:
            y -= 1<<8

        xf += x
        yf += y

        clicked = int(i[0:2], 16)
        if(clicked == 1):
                clicksx.append(xf)
                clicksy.append(yf)

output_file("line.html")

p = figure(plot_width=600, plot_height=600)
# add a circle renderer with a size, color, and alpha
p.circle(clicksx[0:int(len(clicksx))], clicksy[0:int(len(clicksy))], size=1, color="black")

p.y_range.start = -5000
p.y_range.end = 5000
p.x_range.start = -5000
p.x_range.end = 5000

show(p)
#c4tch_th3_m0us3!
```

# Result

![result](https://github.com/st1tch/doubles_ctf/blob/master/for-200-AImouse/result.png)

- 대략 이런 결과가 나오는데, 저거 풀때는 잠이 너무와서 아무생각도 안나서 그냥 노트북을 뒤집고 거울을 가져다 댔다.;;ㅋㅋㅋ

![mirror](https://github.com/st1tch/doubles_ctf/blob/master/for-200-AImouse/mirror.png)

- 플래그가 잘 보인다.!
