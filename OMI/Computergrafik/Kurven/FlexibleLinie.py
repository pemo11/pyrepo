# Zeichnen einer flexiblen Linie mit variablen Stützpunkten
# Erstellt: 05/12/12

from tkinter import *

class Window(Frame):

    def buttonDown(self, event):
        global drawPoints, setPoints, drawMode
        # bei gedrückter Maustaste werden die Koordinanten nicht aktualisiert?
        self.showPos(event)
        # bringt nichts
        # self.cavDraw.update_idletasks()
        if not drawMode:
            return
        xPos = event.x
        yPos = event.y
        # Liegt der Punkt auf der Linie?
        lX = [p[0] for p in drawPoints if p[0] > xPos - 10 and p[0] < xPos + 10]
        lY = [p[1] for p in drawPoints if p[1] > yPos - 10 and p[1] < yPos + 10]
        if len(lX) == 1 and len(lY) == 1:
            x = lX[0]
            y = lY[0]
            p = (x,y)
            if p not in setPoints:
                self.cavDraw.create_oval(x, y, x + 1, y + 1, width=10, outline="red")
                setPoints.append(p)
            else:
                self.cavDraw.create_oval(x, y, x + 1, y + 1, width=10, outline="blue")
                setPoints.remove(p)

    def showPos(self, event):
        self.svX.set(event.x)
        self.svY.set(event.y)

    def newDraw(self, event):
        global drawPoints, drawMode
        xPos = event.x
        yPos = event.y
        # Entspricht die Mauskoordinate einem Punkt auf der Linie?
        lX = [p for p in drawPoints if p[0] > xPos - 10 and p[0] < xPos + 10]
        lY = [p for p in drawPoints if p[1] > yPos - 10 and p[1] < yPos + 10]
        if len(lX) == 1 and len(lY) == 1:
            drawMode = True
            p = lX[0]
            newPointIndex = drawPoints.index(p)
            drawPoints[newPointIndex] = (xPos, yPos)
            # Linie neu zeichnen
            self.drawLine(drawPoints)

    def stopDraw(self, event):
        global drawMode
        drawMode = False

    def __init__(self, root):
        global drawMode, drawPoints
        self.Root = root
        btnDraw = Button(master=root, width=16, text="Draw",command=self.startDraw)
        btnDraw.grid(row=1,column=1)
        self.cavDraw = Canvas(master=root,width=600,height=500,background="lightyellow")
        self.cavDraw.grid(row=2,column=1)
        fraInfo = Frame(master=root, background="lightblue",height=40,width=600)
        fraInfo.grid(row=3,column=1)
        lbl1 = Label(master=fraInfo,width=20,text="X:")
        lbl1.pack(side=LEFT)
        self.svX = StringVar(master=root)
        self.svY = StringVar(master=root)
        lblX = Label(master=fraInfo,width=20,textvariable=self.svX)
        lblX.pack(side=LEFT)
        lbl2 = Label(master=fraInfo,width=20,text="Y:")
        lbl2.pack(side=LEFT)
        lblY = Label(master=fraInfo,width=20,textvariable=self.svY)
        lblY.pack(side=LEFT)
        self.cavDraw.bind("<ButtonPress-1>", self.buttonDown)
        self.cavDraw.bind("<Motion>", self.showPos)
        self.cavDraw.bind("<B1-Motion>", self.newDraw)
        self.cavDraw.bind("<ButtonRelease>", self.stopDraw)
        drawMode = False
        drawPoints = []


    def drawLine(self,points):
        xLast = 0
        yLast = 0
        # Zeichenfläche leeren
        self.cavDraw.delete("all")
        for p in points:
            x = p[0]
            y = p[1]
            self.cavDraw.create_oval(x, y, x + 1, y + 1, width=8, outline="blue")
            if xLast != 0:
                self.cavDraw.create_line(xLast, yLast, x, y, width=2, fill="blue")
            xLast = x
            yLast = y

    def startDraw(self):
        global drawPoints,setPoints,drawMode
        setPoints = []
        drawMode = False
        drawPoints = [(100,100),(200,400),(400,300),(500,10)]
        self.drawLine(drawPoints)

tk = Tk()
app = Window(tk)
tk.mainloop()
