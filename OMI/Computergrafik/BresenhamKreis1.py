# Zeichnen eines Kreises mit dem Bresenham-Algorithmus
# Erstellt: 10/10/20
# Umsetzung nach Wikipedia-Eintrag
# Stimmt noch nicht ganz

from tkinter import *

class Window(Frame):

    def set(self, x, y, f):
        self.cavDraw.create_oval(x,y,x+1,y+1,width=1,fill=f)

    def zeichnen(self,p,r):
        e = 5 - 4 * r
        x = r
        y = 0
        xMittel = p[0]
        yMittel = p[1]
        while y < x:
            dy = y * 2 + 1
            y += 1
            e -= dy
            if e < 0:
                dx = 1 - x * 2
                x -= 1
                e -= dx
            self.set(xMittel+x,yMittel+y,"#ff0000")
            self.set(xMittel+x,yMittel-y,"#0000ff")
            self.set(xMittel+y,yMittel-x,"#00ff00")
            self.set(xMittel-y,yMittel-x,"#0000ff")
            self.set(xMittel-x,yMittel-y,"#ff0000")
            self.set(xMittel-x,yMittel-y,"#0000ff")
            self.set(xMittel-x,yMittel+y,"#00ff00")
            self.set(xMittel-y,yMittel+x,"#0000ff")

    def __init__(self, Root):
        self.Master = Root
        # Ohne update() werden die Geometrie-Werte nicht aktualisiert und bleiben auf 1
        Root.update()
        g = Root.geometry()
        w = Root.winfo_width()
        h = Root.winfo_height()
        self.cavDraw = Canvas(Root,width=w,height=h-40)
        self.cavDraw["bg"] = "lightgreen"
        self.cavDraw.pack()
        bntDraw = Button(Root, text="Zeichnen",command=lambda: self.zeichnen((200,300),50))
        bntDraw.pack()


root = Tk()

root.title("Einen Kreis zeichnen mit Bresenham")
root.geometry("600x400")
win = Window(root)

root.mainloop()
