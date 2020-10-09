# Zeichnen einer Linie nach Prozedur Plot_Line (W.D. Fellner)
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

def Zeichnen(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    s = (y2-y1) / (x2-x1)
    for x in range(x1,x2):
        c = (y1*x2 - y2*x1) / (x2-x1)
        y = round(s*x+c)
        cav1.create_oval(x,y,x+1,y+1,width=2,fill="#0000ff")
        lst1.insert(0,f"x={x}/y={y}")

# Wichtig: y1 und y1 werden vertauscht, damit der Ausgangspunkt in der linken unteren Ecke liegt    
btn1 = tk.Button(width=24,height=32,text="Zeichnen",command = lambda: Zeichnen((0,320),(400,1)))

btn1.pack(pady=4)

win.mainloop()