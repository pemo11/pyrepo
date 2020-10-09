# Ein einfaches Zeichenprogramm für 2D-Figuren mit tkinter
# Erstellt: 06/10/20
# Schritt 2: Die Widgets Canvas, Aktionsflächen und Eingabefelder mit Beschriftung für das Zeichnen von Linien

from tkinter import *

canvasHeight = 600
canvasWidth = 600

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # Durch die Zuweisung gibt Canvas None zurück, so dass grid() nicht direkt folgen kann
        self.cavDraw = Canvas(master,width=canvasWidth,height=canvasHeight)
        self.cavDraw.grid(row=0,column=0)
        self.cavDraw["bg"] = "lightblue"
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
        self.btnZeichnen = Button(self.fraControl,width=12,text="Zeichnen")
        self.btnZeichnen.grid(row=5,column=1,columnspan=2)
        Label(self.fraControl,background="lightyellow").grid(row=6,column=0,columnspan=4)
        self.btnZeichnen = Button(self.fraControl,width=12,text="Löschen")
        self.btnZeichnen.grid(row=7,column=1,columnspan=2)

        # Sorgt dafür, dass fraControl die volle Fläche einnimmt und nicht nur die, die es benötigt
        self.fraControl.grid_propagate(False) 

        self.entX1.insert(0,"1")
        self.entX2.insert(0,"100")
        self.entY1.insert(0,"1")
        self.entY2.insert(0,"100")

root = Tk()
root.geometry("800x600")
root.title("PyMiniDraw 0.1")

win = Window(root)
win.mainloop()