# Zeichnen eines Kreises mit dem Bresenham-Algorithmus
# Umsetzung nach OMI-Video
# Erstellt: 11/10/20
# Stimmt noch nicht ganz

from tkinter import *

class Window(Frame):

    def set(self, x, y, f):
        self.cavDraw.create_oval(x,y,x+1,y+1,width=1,fill=f)

    def zeichnen1(self, event, r):
        self.zeichnen((event.x, event.y), r)

    def zeichnen(self,p,r):
        e = 5 - 4 * r
        x = 0
        y = r
        xMittel = p[0]
        yMittel = p[1]
        self.set(xMittel+x,yMittel+y,"red")
        self.set(xMittel+x,yMittel-y,"red")
        self.set(xMittel-x,yMittel+y,"red")
        self.set(xMittel-x,yMittel-y,"red")
        self.set(xMittel+y,yMittel+x,"red")
        self.set(xMittel+y,yMittel-x,"red")
        self.set(xMittel-y,yMittel+x,"red")
        self.set(xMittel-y,yMittel-x,"red")
        while x < y:
            if e > 0:
                e += 8 * (x-y) + 20
                y -= 1
            else:
                e += 8 * x + 12
            x += 1
            self.set(xMittel+x,yMittel+y,"red")
            self.set(xMittel+x,yMittel-y,"red")
            self.set(xMittel-x,yMittel+y,"red")
            self.set(xMittel-x,yMittel-y,"red")
            self.set(xMittel+y,yMittel+x,"red")
            self.set(xMittel+y,yMittel-x,"red")
            self.set(xMittel-y,yMittel+x,"red")
            self.set(xMittel-y,yMittel-x,"red")

    def __init__(self, Root):
        self.Master = Root
        # Ohne update() werden die Geometrie-Werte nicht aktualisiert und bleiben auf 1
        Root.update()
        g = Root.geometry()
        w = Root.winfo_width()
        h = Root.winfo_height()
        self.cavDraw = Canvas(Root,width=w,height=h-40)
        self.cavDraw["bg"] = "lightgreen"
        # Geniale Syntax dank Lambdas
        self.cavDraw.bind("<Button-1>",lambda event, r=100: self.zeichnen1(event, r))
        self.cavDraw.pack()
        bntDraw = Button(Root, text="Zeichnen",command=lambda: self.zeichnen((300,200),100))
        bntDraw.pack()


root = Tk()

root.title("Einen Kreis zeichnen mit Bresenham")
root.geometry("600x400")
win = Window(root)

root.mainloop()
