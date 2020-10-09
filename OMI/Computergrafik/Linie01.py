# Zeichnen einer Linie per einfacher Geradengleichung mit einem tkInter canvas
# Erstellt: 25/09/20
import tkinter as tk

# Version: 8.6
# print(tkinter.TkVersion)

win = tk.Tk()
win.geometry("600x400")
win.title("Computergrafik mit Python")

cav1 = tk.Canvas(width=400,height=320)
cav1["bg"] = "lightgreen"
cav1.pack(padx=100,pady=20)

ar = float(cav1["height"]) / float(cav1["width"])

def Zeichnen():
    y = 320
    for x in range(0,400):
        y -= ar
        # Ab tkinter 8.6.9 geht auch x,y,x,y
        # cav1.create_line(x, y, x+1, y,fill="#ff0000")
        cav1.create_oval(x,y,x+1,y+1,width=5,fill="#0000ff")

btn1 = tk.Button(width=24,height=32,text="Zeichnen",command=Zeichnen)

btn1.pack(pady=4)

win.mainloop()