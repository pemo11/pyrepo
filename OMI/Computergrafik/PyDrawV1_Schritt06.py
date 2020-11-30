# Ein einfaches Zeichenprogramm für 2D-Figuren mit tkinter
# Erstellt: 09/10/20
# Schritt 6: Zeichnen von Kurven und kontinuierliches Zeichnen
# Geht noch nicht - Problem mit der Zustandsverwaltung
# Das Verhalten soll so sein:
# Wenn connectMode = True ist, soll die nächste Linie automatisch am Endpunkt der letzten Linie beginnen
# Außerdem soll in diesem Fall die letzte Linie nicht gelöscht werden, dh. das Löschen der Linie muss 1x aussetzen
# Oder vielleicht einfacher umsetzbar: Wenn connectMode = True, wird der Anfangs nur dann auf den Endpunkt gesetzt,
# wenn er sich in der Nähe befindet,also z.B. im Radius von 10 Pixeln

from tkinter import *
from tkinter.colorchooser import *
from os import path

canvasHeight = 600
canvasWidth = 600
currentX = 0
currentY = 0
drawMode = False
drawColor = "#0000ff"
connectMode = False
curveMode = False
lineMode = False

currentYOld = 0
currentXOld = 0
currentX1Old = 0
currentY1Old = 0

class Window(Frame):

    def Zeichnen1(self):
        x1 = int(self.entX1.get())
        x2 = int(self.entX2.get())
        y1 = int(self.entY1.get())
        y2 = int(self.entY2.get())
        lineWidth = int(self.entLineWidth.get())
        scaleFactor = int(self.entFactor.get())
        dx = abs(y2-y1) 
        dy = abs(x2-x1)
        s =  dx / dy
        # y-Koordinate muss "umgedreht" werden, da 0/0 => 0/canvasHeight
        y = canvasHeight - y1
        for x in range(x1, x2):
            y -= s * scaleFactor
            x *= scaleFactor
            self.cavDraw.create_oval(x,y,x+1,y+1,width=lineWidth,outline=drawColor)
    
    def clearCanvas(self):
        self.cavDraw.delete("all")

    def chooseColor(self):
        global drawColor
        # askcolor() gibt ein Tupel (RGB,#Farbcode) zurück
        drawColor = askcolor()[1]

    def startDraw(self, event):
        global currentX, currentY, drawMode
        currentX = event.x
        currentY = event.y
        drawMode = True

    def stopDraw(self, event):
        global drawMode
        global currentYOld, currentXOld, currentX1Old, currentY1Old
        currentYOld, currentXOld, currentX1Old, currentY1Old = (0,0,0,0)
        drawMode = False

    def changeDrawMode(self):
        global connectMode
        connectMode = not connectMode

    def drawSomething(self, event):
        global currentYOld, currentXOld, currentX1Old, currentY1Old
        # Soll ein Rechteck gezeichnet werden?
        if LineMode == 1:
            drawLine(event)
        if rectMode == 1:
            drawRect(event)
        elif circleMode == 1:
            drawCircle(event)
        else:
            drawCurve(event)

    def drawLine(self, event):
        # Linienbreite holen
        lineWidth = int(self.entLineWidth.get())
        # Die alte Linie löschen
        if drawMode and currentXOld != 0:
            self.cavDraw.create_line(currentXOld, currentYOld, currentX1Old, currentY1Old, width=lineWidth, fill="white")
        currentX1 = event.x
        currentY1 = event.y
        self.cavDraw.create_line(currentX, currentY, currentX1, currentY1, width=lineWidth,fill=drawColor)
        currentXOld = currentX
        currentYOld = currentY
        currentX1Old = currentX1
        currentY1Old = currentY1

    def drawRect(self, event):
        # Das alte Rechteck löschen
        pass

    def drawCircle(self, event):
        # Den alten Kreis löschen
        pass

    def drawCurve(self, event):
        pass

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # Durch die Zuweisung gibt Canvas None zurück, so dass grid() nicht direkt folgen kann
        self.cavDraw = Canvas(master,width=canvasWidth,height=canvasHeight)
        self.cavDraw.grid(row=0,column=0)
        self.cavDraw["bg"] = "white"
        # Wichtig: Button-1-Event binden
        self.cavDraw.bind("<Button-1>", self.startDraw) 
        self.cavDraw.bind("<ButtonRelease-1>", self.stopDraw) 
        self.cavDraw.bind("<B1-Motion>", self.drawSomething)
        self.fraControl = Frame(master,width=200,height=600)
        self.fraControl.grid(row=0,column=1,sticky="N")
        self.fraControl["bg"] = "lightyellow"

        Label(self.fraControl,background="lightyellow").grid(row=0,column=0,columnspan=4)
        Label(self.fraControl, width=4, borderwidth=1, text="X1:").grid(row=1,column=0,padx=4)
        self.entX1 = Entry(self.fraControl, width=5)
        self.entX1.grid(row=1,column=1,padx=4)
        Label(self.fraControl, width=5, borderwidth=1, text="Y1:").grid(row=1,column=2,padx=4)
        self.entY1 = Entry(self.fraControl, width=5)
        self.entY1.grid(row=1,column=3)
        Label(self.fraControl,background="lightyellow").grid(row=2,column=0,columnspan=4)
        Label(self.fraControl, width=4, text="X2:").grid(row=3,column=0,padx=4)
        self.entX2 = Entry(self.fraControl, width=5)
        self.entX2.grid(row=3,column=1)
        Label(self.fraControl, width=4, borderwidth=1, text="Y2:").grid(row=3,column=2,padx=4)
        self.entY2 = Entry(self.fraControl,width=5)
        self.entY2.grid(row=3,column=3)
        Label(self.fraControl,background="lightyellow").grid(row=4,column=0,columnspan=4)
        Label(self.fraControl, width=5, borderwidth=1, text="Faktor:").grid(row=5,column=0,padx=4)
        self.entFactor = Entry(self.fraControl, width=5)
        self.entFactor.grid(row=5,column=1)
        Label(self.fraControl,background="lightyellow").grid(row=6,column=0,columnspan=4)
        Label(self.fraControl, width=5, borderwidth=1, text="Stärke:").grid(row=7,column=0,padx=4)
        self.entLineWidth = Entry(self.fraControl, width=5)
        self.entLineWidth.grid(row=7,column=1)
        Label(self.fraControl,background="lightyellow").grid(row=8,column=0,columnspan=4)
        self.btnZeichnen = Button(self.fraControl,width=12,text="Zeichnen",command=self.Zeichnen1)
        self.btnZeichnen.grid(row=9,column=1,columnspan=2)
        Label(self.fraControl,background="lightyellow").grid(row=10,column=0,columnspan=4)
        self.btnZeichnen = Button(self.fraControl,width=12,text="Löschen",command=self.clearCanvas)
        self.btnZeichnen.grid(row=11,column=1,columnspan=2)
        Label(self.fraControl,background="lightyellow").grid(row=12,column=0,columnspan=4)
        self.btnZeichnen = Button(self.fraControl,width=12,text="Farbwahl",command=self.chooseColor)
        self.btnZeichnen.grid(row=13,column=1,columnspan=2)
        Label(self.fraControl,background="lightyellow").grid(row=14,column=0,columnspan=4)
        self.chkConti = Checkbutton(self.fraControl, width=12, text="Freihand", onvalue=1, offvalue=0, anchor="w", command=self.changeDrawMode)
        self.chkConti.grid(row=15,column=1,columnspan=2)
        # variable= setzt die angegebene Variable auf den Wert 0/1 bzw. den durch onvalue/offvalue festgelegten Wert
        self.chkLinie = Checkbutton(self.fraControl, width=12, text="Linie", onvalue=1, offvalue=0,  anchor="w", variable=lineMode)
        self.chkLinie.grid(row=16,column=1,columnspan=2)
        self.chkLinie = Checkbutton(self.fraControl, width=12, text="Kreis", onvalue=1, offvalue=0,  anchor="w", variable=circleMode)
        self.chkLinie.grid(row=17,column=1,columnspan=2)
        
        # Sorgt dafür, dass fraControl die volle Fläche einnimmt und nicht nur die, die es benötigt
        self.fraControl.grid_propagate(False) 
        # self.fraControl.grid_rowconfigure(1, weight=1)
        # self.fraControl.grid_columnconfigure(1, weight=1)

        self.entX1.insert(0,"1")
        self.entX2.insert(0,"100")
        self.entY1.insert(0,"1")
        self.entY2.insert(0,"100")
        self.entLineWidth.insert(0, "2")
        self.entFactor.insert(0,"10")

root = Tk()
root.geometry("800x600")
icoPath = path.join(path.dirname(__file__), "pydraw.ico")
root.iconbitmap(icoPath)
root.title("PyMiniDraw 0.1")

win = Window(root)
win.mainloop()