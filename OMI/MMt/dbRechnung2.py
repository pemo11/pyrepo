# Aufgaben aus dem Skript

# Welches Leistungsverhältnis in dB ergibt sich für P1 = 1 mW und P0 = 10uW?
import math

p1 = 0.001
p0 = 0.00001

l = 10 * math.log10(p1/p0) 

print("Antwort: %.2f Db" % l)