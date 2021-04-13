import tkinter, math

class canvas:
    def __init__(self):
        self.application = tkinter.Tk()
        self.application.config(bg='black')
        self.area = tkinter.Canvas(self.application)
        self.area.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        self.angle=0
        self.width = 800
        self.height = 500
        self.scale = 300
        self.resolution = 10
        self.lock = False
        self.clockwise = True
        self.patternloop = True
        self.resize(800,500)
        self.setbackground('white')
        self.application.after(100,self.startloop)

    def startloop(self):
        self.patternloop = True
        self.application.after(100,self._loop)

    def stoploop(self):self.patternloop = False

    def _loop(self):
        self.drawpattern(self.angle)
        self.angle += 1
        if self.angle>360:self.angle = 1
        if self.patternloop:self.application.after(100,self._loop)
        
    def loop(self):self.application.mainloop()

    def setbackground(self,color):self.area.config(bg=color)

    def resize(self,width,height):
        self.application.geometry('{0}x{1}'.format(width,height))
        self.area.config(width=width,height=height)
        self.width = width;self.height = height

    def drawpattern(self,value):
        if self.clockwise:i,j = math.cos(value), math.sin(value)
        else:i,j = math.sin(value), math.cos(value)
        is_fractel = 0
        width = self.width
        height = self.height
        if not(self.lock):
            self.lock = True
            self.area.delete('all')
            for x in range(0, width, 10):
                for y in range(0, height, 10):
                    a = self.map(x,width,self.scale)
                    b = self.map(y,height,self.scale)
                    c1 = i # a
                    c2 = j # b
                    n = 0
                    while(n < self.resolution):
                        if (a*a + b*b > 4):break
                        t_a = a*a - b*b
                        t_b = 2 * a * b
                        a = t_a + c1
                        b = t_b + c2
                        n += 1
                    if n == self.resolution:self.area.create_oval(x-4,y-4,x+4,y+4,fill='green')
            self.lock = False

    def map(self,value,dimension,scale):return (value/dimension)*((dimension/scale)-(-1*dimension/scale))+(-1*dimension/scale)
    
if __name__ == "__main__":
    c = canvas()
    c.loop()
