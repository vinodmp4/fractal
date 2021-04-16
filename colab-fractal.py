!pip3 install colabturtle
import ColabTurtle.Turtle as sam
sam.initializeTurtle()
sam.speed(13)
sam.showturtle()

scale = 200
resolution = 100
drawjulia = False

def drawpoint(x,y):
    sam.penup()
    sam.goto(x,y)
    sam.pendown()
    sam.width(1)
    sam.goto(x,y)
width = sam.window_width()
height = sam.window_height()
def mapval(val, r_x, r_y, x, y):
    return ((val-r_x)/(r_y-r_x))*(y-x)+x
mandelbrot_area = 0
points = []
for x in range(width):
    for y in range(height):
        a = mapval(x, 0, width, (-1*width/scale), (width/scale))
        b = mapval(y, 0, height, (-1*height/scale), (height/scale))
        c1 = a if not(drawjulia) else -0.8
        c2 = b if not(drawjulia) else 0.156
        n = 0
        while (n<resolution):
            t_a = a**2 - b**2
            t_b = 2 * a * b                       
            a = t_a + c1
            b = t_b + c2 
            if (a*a + b*b > 4):break
            n += 1
        if n == resolution:
            if not(mandelbrot_area==1):mandelbrot_area = 1;points.append((x,y))
        else:
            if not(mandelbrot_area==0):mandelbrot_area = 0;points.append((x,y-1))
for point in points:
    drawpoint(point[0],point[1])
