# Ausgabe einer Sinuskurve
# Erstellt: 28/10/20

import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0,10,0.1)

amplitude   = np.sin(time)
plot.plot(time, amplitude)

plot.title("Eine Sinus-Kurve")

plot.xlabel("Zeit")
plot.ylabel("Amplitude = sin(Zeit)")

plot.grid(True,which="both")

plot.axhline(y=0,color="k")

plot.show()