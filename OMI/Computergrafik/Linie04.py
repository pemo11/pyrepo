# DDA-Linie mit Abstandstransformation
# Erstellt: 26/09/20
import tkinter as tk

win = tk.Tk()
win.geometry("600x400")
win.title("Computergrafik mit Python")

frm1 = tk.Frame()
frm1.pack()

cav1 = tk.Canvas(master=frm1,width=400,height=320)
cav1["bg"] = "lightgreen"
cav1.pack(side=tk.LEFT,padx=10,pady=20)

# was bedeuten width und height bei einer Listbox, nur mit diesen Zahlen ist die Listbox so groß wie der Canvas?
lst1 = tk.Listbox(master=frm1,width=24,height=20)
lst1["bg"] = "lightyellow"
lst1.pack(padx=0,pady=20)

def Zeichnen(p1, p2, f=1):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    length = abs(x2 - x1)
    if abs(y2-y1) > length:
        length = abs(y2-y1)
    dx = (x2 - x1) / length * f
    dy = (y2 - y1) / length * f
    x = x1
    y = y1
    for _ in range(1, length + 1, f):
        x = round(x) 
        y = round(y)
        cav1.create_oval(x,y,x+1,y+1,width=2,fill="#0000ff")
        lst1.insert(0,f"x={x}/y={y}")
        x += dx
        y += dy

# Wichtig: y1 und y1 werden vertauscht, damit der Ausgangspunkt in der linken unteren Ecke liegt    
btn1 = tk.Button(width=24,height=32,text="Zeichnen",command = lambda: Zeichnen((0,320),(400,1),20))

btn1.pack(pady=4)

win.mainloop()