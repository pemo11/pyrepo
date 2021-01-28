#! usr/bin/python3
# Erstellt: 17/01/21
# Das Prinzip der additiven Farbmischung visualisiert

from tkinter import *
from PIL import *

class AppWindow(Frame):

    def __int__(self, root):
        self.root = root



tk = Tk()
tk.title("Additive Farbmischung mit RGB")
tk.geometry("600x400")

app = AppWindow(tk)

tk.mainloop()