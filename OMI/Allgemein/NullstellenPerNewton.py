# Nullstellen bestimmen mit dem Newton-Verfahren
# 05/05 - noch kein Ergebnis:(
import math

# Lambdas als Alternative
def f(x):
    return 2 * math.pow(x, 4) - 14 * math.pow(x, 2) - 12 * x

def f1(x):
    return 8 * math.pow(x, 3) - 28 * x - 12

for x in range(-10, 10):
    print(f"f({x})={f(x)}")

while(True):
    a = (float)(input("Geschätzter Anfangswert?"))
    y = f(a)
    y1 = f1(a)
    if math.fabs(y1) > 1E-20:
        break
    print("Wert zu klein - bitte einen anderen Anfangswert eingeben.")

while(True):
    y = f(a)
    y1 = f1(a)
    a1 = a - y/y1
    if math.fabs(a - a1) < math.fabs(a * 1E-5):
        break
    a = a1

print(f"Nullstelle: {(a+a1)/2}")



