#! usr/bin/python3
# Zeichnen eines CIE-Diagramms mit Hilfe des colour-Moduls
# Erstellt: 16/01/21

# Hatte zuerst das falsche Package installiert - colour-science statt colour
# Dann wurde ein wunderschönes Diagramm angezeigt
import matplotlib.pyplot as plt
import colour
from colour.plotting import *
# from ipywidgets import interact

plot_chromaticity_diagram_CIE1931(standalone=False)
x, y = 10,10
plt.plot(x, y, 'o-', color='white')

render(
    standalone=True,
    limits=(-0.1, 0.9, -0.1, 0.9),
    x_tighten=True,
    y_tighten=True)