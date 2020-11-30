# 2D-Operationen
# Letzte Aktualisierung: 10/11/20
# Rotation um einen Punkt p funktioniert (endlich)

from tkinter import *
import numpy as np

pointDic = {"church":[(20,20), (140,20), (140,60), (120,80), (60,80), (40, 220), (20,80)]}
# pointDic = {"church":[(0,0), (120,0), (120,40), (100,60), (40,60), (20, 200), (0,60)]}

class Window(Frame):

    def clearCanvas(self):
        self.cavDraw.delete("all")
        self.drawAxis()

    def drawPoint(self, x,y):
        self.cavDraw.create_oval(x,y,x+1,y+1,width=1,fill="#0000ff")

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

    def rotate(self):
        w = int(self.gradVar.get())
        w = np.radians(w)
        # Liste = Zeile
        mRot = np.array([[np.cos(w),-np.sin(w),0], [np.sin(w),np.cos(w),0]])
        points =[self.transform2Axis2(p) for p in self.points]
        pointsNeu = [np.dot(mRot, np.array([p[0],p[1],1])).tolist() for p in points]
        pointsNeu = [self.transform2Axis(p) for p in pointsNeu]
        self.cavDraw.create_polygon(pointsNeu,outline="red",fill="",width=1)

    def rotate2(self):
        w = int(self.gradVar.get())
        w = np.radians(w)
        # Liste = Zeile
        points =[self.transform2Axis2(p) for p in self.points]
        # Es soll um den ersten Punkt rotiert werden
        pRot = points[0]
        pointsNeu = [np.dot(np.array([[np.cos(w),-np.sin(w), pRot[0]*(1-np.cos(w))+pRot[1]*np.sin(w)],
         [np.sin(w), np.cos(w), pRot[1]*(1-np.cos(w))-pRot[0]*np.sin(w)]]),
         np.array([p[0],p[1],1])).tolist() for p in points]
        pointsNeu = [self.transform2Axis(p) for p in pointsNeu]
        self.cavDraw.create_polygon(pointsNeu,outline="red",fill="",width=1)

    # Rotieren um einen Punkt per Translation
    def rotate3(self):
        w = int(self.gradVar.get())
        w = np.radians(w)
        points = [self.transform2Axis2(p) for p in self.points]
        mRot = np.array([[np.cos(w), -np.sin(w), 0], [np.sin(w), np.cos(w), 0], [0, 0, 1]])
        pRot = points[0]
        pointsNeu = [np.dot(np.dot(np.array([[1, 0, pRot[0]], [0, 1, pRot[1]], [0, 0, 1]]),mRot),
                     np.array([[1, 0, 0-pRot[0]], [0, 1, 0-pRot[1]], [0, 0, 1]])) for p in points]
        points = [self.transform2Axis(p) for p in pointsNeu]
        self.cavDraw.create_polygon(points,outline="green",fill="",width=1)

    def scale(self):
        points = [self.transform2Axis2(p) for p in self.points]
        scale = float(self.scaleVar.get())
        # mScale = np.array([[scaleVal,0,0],[0,scaleVal,0],[0,0,1]])
        pointsNeu = [points[0]] + [np.dot(np.array([p[0],p[1],1]), np.array([[scale,0,p[0]*(1-scale)],[0,scale,p[1]*(1-scale)],[0,0,1]])) for p in points[1:]]
        points = [self.transform2Axis(p) for p in pointsNeu]
        self.cavDraw.create_polygon(points,outline="red",fill="",width=1)

    def drawRect(self,p,w,h):
        p = self.transform2Axis(p)
        x1 = p[0]
        y1 = p[1]
        for x in range(0,w):
            # self.cavDraw.create_oval(x+x1,y1,x+x1+1,y1,width=1,fill="#0000ff")
            self.drawPoint(x+x1, y1)
            self.drawPoint(x+x1, y1+h)
        for y in range(0,h):
            self.drawPoint(x1, y+y1)
            self.drawPoint(x1+w, y+y1)

    def drawPolygon(self,key):
        self.points = [self.transform2Axis(p) for p in pointDic[key]]
        self.cavDraw.create_polygon(self.points,outline="black",fill="",width=1)

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

        btnDrawRect = Button(master=self.fraControl,text="Rect",width=16,height=2,
           command=lambda: self.drawRect((50,150),200,100))
        # oder Attributwerte nachträglich setzen
        btnDrawRect["bg"] = "lightyellow"
        btnDrawRect.pack(side=TOP, padx=40, pady=10)

        btnDraw2Object = Button(master=self.fraControl,text="2D-Objekt",width=16,height=2,
           command=lambda: self.drawPolygon("church"))
        # oder Attributwerte nachträglich setzen
        btnDraw2Object["bg"] = "lightblue"
        btnDraw2Object.pack(side=TOP, padx=40, pady=10)

        self.gradVar = StringVar(value="45")
        enGrad = Entry(master=self.fraControl,textvariable=self.gradVar,width=10)
        enGrad.pack(side=TOP,padx=20,pady=10)

        btnRotate = Button(master=self.fraControl,text="Rotate",width=16,height=2,
           command=lambda: self.rotate3())
        btnRotate["bg"] = "lightgreen"
        btnRotate.pack(side=TOP, padx=40, pady=10)

        self.scaleVar = StringVar(value="2")
        enScale = Entry(master=self.fraControl,textvariable=self.scaleVar,width=10)
        enScale.pack(side=TOP,padx=20,pady=10)

        btnScale = Button(master=self.fraControl,text="Scale",width=16,height=2,
           command=lambda: self.scale())
        btnScale["bg"] = "cyan"
        btnScale.pack(side=TOP, padx=40, pady=10)


canvasHeight = 600
canvasWidth = 600
winHeight = 600
winWidth = 800

root = Tk()
root.geometry(f"{winWidth}x{winHeight}")
root.title("2D-Grafik - Skalierung")

win = Window(root)
win.mainloop()