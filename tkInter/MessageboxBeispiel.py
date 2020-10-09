# Anzeige von Messageboxen
# Erstellt: 03/10/20

# Warum ist dieser import erforderlich, da * doch alles importieren sollte?
# from tkinter import messagebox

# Variante A
# import tkinter.messagebox

# Geht mit A
# tkinter.messagebox.showinfo(master=None, title="Hinweis", message="Alles klaro!")
# geht nicht mit A
# messagebox.showinfo(master=None, title="Hinweis", message="Alles klaro!")

# Variante B
# from tkinter import messagebox

# Geht mit B
# messagebox.showinfo(master=None, title="Hinweis", message="Alles klaro!")

# Mit den beiden Befehlen wird nicht das messagebox-Modul importiert, es muss daher separat importiert werden
# from tkinter import *
# import tkinter
# Variante C
from tkinter.messagebox import *
# geht mit C
showinfo(master=None, title="Hinweis", message="Alles klaro!")