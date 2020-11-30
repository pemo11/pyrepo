# Berechnen der Bresenham-Fehlerkorrektur
# Erstellt: 19/11/20

p1 = (1,1)
p2 = (10,20)

dx = p2[0] - p1[0]
dy = p2[1] - p1[1]
b = 0
x1 = p1[0]
x2 = p2[1]

def fehlerWert(x,y,dx,dy, b):
    e = y - dy/dx - b

e1 = lambda x,y,dx,dy,b: y - dy/dx * x - b
e2 = lambda x,y,dx,dy,b: dx * y - dy * x - dx * b

y = p1[1]
for x in range(x1,x2):
    print(e1(x,y,dx,dy,b))
    y += 1