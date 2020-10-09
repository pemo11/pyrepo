# Zeichnen einer Linie nach Prozedur Octantal DDA (W.D. Fellner)
# Entspricht dem Bresenham-Algo?
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
    x = x1
    y = y1
    dx = x2 - x1
    # dy = y2 - y1
    # Wegen der y-Koordinaten-Vertauschung
    dy = y1 - y2
    c1 = 2 * dy
    error = c1 - dx
    c2 = error - dx
    Abbruch = False
    while not Abbruch:
        cav1.create_oval(x,y,x+1,y+1,width=2,fill="#0000ff")
        lst1.insert(0,f"error={error} x={x}/y={y}")
        x += 1 * f
        if error < 0:
            error += c1
        else:
            y -= 1 * f
            error += c2
        if x > x2:
            Abbruch = True

# Wichtig: y1 und y1 werden vertauscht, damit der Ausgangspunkt in der linken unteren Ecke liegt    
btn1 = tk.Button(width=24,height=32,text="Zeichnen",command = lambda: Zeichnen((0,320),(400,1),15))

btn1.pack(pady=4)

win.mainloop()