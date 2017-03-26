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
