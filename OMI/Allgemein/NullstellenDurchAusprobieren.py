# Nullstellen finden durch ausprobieren
import math

gefunden = False

#f = lambda  x: -2 * math.pow(x, 3) + 30 * math.pow(x, 2) + 50 * x - 750
#f = lambda  x: math.pow(x, 3) - 5 * math.pow(x, 2) + 5 * math.pow(x, 2) - 19 * x - 30
#f = lambda  x: math.pow(x, 3) - 5 * math.pow(x, 2) + 5 * math.pow(x, 2) - 19 * x - 30
# f = lambda  x: 2 * math.pow(x, 4) - 14 * math.pow(x, 2) - 12 * x
#f = lambda  x: math.pow(x, 4) - 10 * math.pow(x, 3) + 2 * math.pow(x, 2) - 10 * x
#f = lambda  x: math.pow(x, 4) - 17 * math.pow(x, 3) + 80 * math.pow(x, 2) - 100 * x
f = lambda x: (math.pow(x, 3) + 7 * math.pow(x, 2) + 4 * x -12) / (math.pow(x, 2) + 5 * x + 6)

nichtErlaubteTeiler = [-2,-3]
for x in range(-15,15):
        if x not in nichtErlaubteTeiler:
           if f(x) == 0:
              print("*** Nullstelle bei %d" % x)
              gefunden = True

if gefunden == False:
    print("Leider keine einzige Nullstelle gefunden, sorry")