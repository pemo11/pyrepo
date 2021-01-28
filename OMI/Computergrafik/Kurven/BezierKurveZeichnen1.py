# Zeichnen einer Bezier-Kurve mit Hilfe von Castelau
# Erstellt: 02/02/12

from tkinter import *


class Window(Frame):

    def buttonDown(self, event):
        global drawpoints
        xPos = event.x
        yPos = event.y
        # Liegt der Punkt auf der Linie?
        lX = [p for p in drawpoints if p[0] > xPos - 20 and p[0] < xPos + 20]
        lY = [p for p in drawpoints if p[1] > yPos - 20 and p[1] < yPos + 20]
        if len(lX) == 1 and len(lY) == 1:
            self.cavDraw.create_oval(xPos, yPos, xPos + 1, yPos + 1, width=8, outline="red")

    def showPos(self, event):
        self.svX.set(event.x)
        self.svY.set(event.y)

    def __init__(self, root):
        global drawpoints
        self.Root = root
        btnDraw = Button(master=root, width=16, text="Draw",command=self.startCastelau1)
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

    def startCastelau1(self):
        pointsList = [(100,100),(200,400),(400,300),(500,0)]
        self.casteljau(pointsList)

    def casteljau(self, p):
        global drawpoints
        n = 3   # Kurvengrad, in der Regel 3
        a = len(p)
        a = 10
        du = round(1 / (a - 1), 2)
        u = du
        xPoints = [point[0] for point in p]
        yPoints = [point[1] for point in p]
        xLast = xPoints[0]
        yLast = yPoints[0]
        drawpoints = []
        while u < 1:
            for j in range(1,n+1):
                for i in range(0,n-j+1):
                    xPoints[i] = round((1-u) * xPoints[i] + u * xPoints[i+1],3)
                    yPoints[i] = round((1-u) * yPoints[i] + u * yPoints[i+1],3)
            u += du
            x = xPoints[0]
            y = yPoints[0]
            self.cavDraw.create_oval(x, y, x + 1, y + 1, width=8, outline="blue")
            self.cavDraw.create_line(xLast, yLast, x, y, width=2, fill="blue")
            xLast = xPoints[0]
            yLast = yPoints[0]
            drawpoints.append((xLast,yLast))

tk = Tk()
app = Window(tk)
tk.mainloop()
