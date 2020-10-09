# Ein einfaches Zeichenprogramm für 2D-Figuren mit tkinter
# Erstellt: 06/10/20
# Schritt 1: Ein leerer Rahmen wird angelegt

from tkinter import *

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
    
root = Tk()
root.geometry("800x600")
root.title("PyMiniDraw 0.1")

win = Window(root)
win.mainloop()