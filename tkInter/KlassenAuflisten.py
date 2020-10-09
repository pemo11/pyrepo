# Alle Klassen aus dem tkinter-Modul auflisten
# Erstellt: 03/10/20

import sys,inspect
import tkinter

moduleName = "tkinter"
for name, obj in inspect.getmembers(sys.modules[moduleName]):
    if inspect.isclass(obj):
        print(obj)