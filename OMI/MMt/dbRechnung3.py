# Berechnen der Spannungsverhältnisse
import math

uList = ((1,0.001),(0.001,1),(2,1))

def spanvh(t):
    return 20 * math.log10(t[0]/t[1])

for u in uList:
    print("%.2f dB" % spanvh(u))