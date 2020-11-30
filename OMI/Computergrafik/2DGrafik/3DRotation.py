# 3D-Rotation für Einführung in die Computergrafik - Ein rotierender Würfel
# Erstellt: 15/11/20

# Rotiert leider noch nicht, Fehlermeldung

from tkinter import *
import numpy as np

p1=(10,10,0)
p2=(110,10,0)
p3=(110,100,1)
p4=(120,50,1)
p5=(120,120,1)
p6=(30,120,1)
p7=(10,100,1)
p8=(30,50,1)

pointDic = {"cube1":[(p1,p2), (p2,p4), (p4,p8), (p8,p1),(p4,p5),(p8,p6),(p5,p6),(p1,p7),(p2,p3),(p7,p3),(p7,p6),(p3,p5)]}
pointList = (p1,p2,p3,p4,p5,p6,p7,p8)

class Window(Frame):

    def clearCanvas(self):
        self.cavDraw.delete("all")
        self.drawAxis()

    def drawLine(self, p1, p2):
        p1 = self.transform2Axis(p1)
        p2 = self.transform2Axis(p2)
        self.cavDraw.create_line(p1,p2)

    def transform2Axis(self, p):
        w = canvasWidth // 2
        h = canvasHeight // 2
        return (p[0]+w, h-p[1])

    def transform2Axis2(self, p):
        w = canvasWidth // 2
        h = canvasHeight // 2
        return (p[0]-w, h-p[1])

    def drawCube(self,points):
        for point in points:
            self.drawLine(point[0], point[1])

    def rotate3D(self):
        w = 45
        w = np.radians(w)
        mRot = np.array([[np.cos(w), 0, np.sin(w),0],[0,1,0,0],[-np.sin(w),0,np.cos(w),0],[-np.sin(w),0,np.cos(w),0],[0,0,0,1]])
        newPoints = [np.dot(mRot, np.array([p[0],p[1],p[2],1])) for p in pointList]
        self.drawCube(newPoints)

    def drawAxis(self):
        y = canvasHeight // 2
        w = canvasWidth
        self.cavDraw.create_line(0, y, w, y)
        y = 0
        x = canvasWidth // 2
        h = canvasHeight
        self.cavDraw.create_line(x, 0, x, h)
        # Pfeil am oberen Ende der y-Achse
        p1 = (canvasWidth // 2 - 10, 10)
        p2 = (canvasWidth // 2, 0)
        self.cavDraw.create_line(p1, p2)
        p1 = (canvasWidth // 2 + 10, 10)
        p2 = (canvasWidth // 2, 0)
        self.cavDraw.create_line(p1, p2)
        # Pfeil am rechten Ende der x-Achse
        p1 = (canvasWidth - 10, canvasHeight // 2 - 10)
        p2 = (canvasWidth, canvasHeight // 2)
        self.cavDraw.create_line(p1, p2)
        p1 = (canvasWidth - 10, canvasHeight // 2 + 10)
        p2 = (canvasWidth, canvasHeight // 2)
        self.cavDraw.create_line(p1, p2)
        # x und y zeichnen
        p1 = (canvasWidth - 10, canvasHeight // 2 + 15)
        self.cavDraw.create_text(p1, text="x",anchor="w")
        p1 = (canvasWidth // 2 + 10, 18)
        self.cavDraw.create_text(p1, text="y",anchor="w")

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # Durch die Zuweisung gibt Canvas None zurück, so dass grid() nicht direkt folgen kann
        self.cavDraw = Canvas(master,width=canvasWidth,height=canvasHeight)
        self.cavDraw.grid(row=0,column=0)
        self.cavDraw["bg"] = "lightblue"
        self.fraControl = Frame(master,width=180,height=600)
        self.fraControl.grid(row=0,column=1,sticky="N")

        self.drawAxis()

        btnClear = Button(master=self.fraControl,text="Clear",width=16,height=2,
           command=self.clearCanvas)
        btnClear["bg"] = "magenta"
        btnClear.pack(side=TOP, padx=40, pady=10)

        btnDrawCube = Button(master=self.fraControl,text="Cube",width=16,height=2,
           command=lambda: self.drawCube(pointDic["cube1"]))
        # oder Attributwerte nachträglich setzen
        btnDrawCube["bg"] = "lightyellow"
        btnDrawCube.pack(side=TOP, padx=40, pady=10)

        btnRotate = Button(master=self.fraControl,text="Rotate",width=16,height=2,
           command=lambda: self.rotate3D())
        btnRotate["bg"] = "lightblue"
        btnRotate.pack(side=TOP, padx=40, pady=10)

        self.speedVar = StringVar(value="1")
        speedGrad = Entry(master=self.fraControl,textvariable=self.speedVar,width=10)
        speedGrad.pack(side=TOP,padx=20,pady=10)


canvasHeight = 600
canvasWidth = 600
winHeight = 600
winWidth = 800

root = Tk()
root.geometry(f"{winWidth}x{winHeight}")
root.title("3D-Grafik - Rotierender Würfel")

win = Window(root)
win.mainloop()