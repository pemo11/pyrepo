# Übergabe als Referenz an eine Function
# Ein Call by Reference mit Primitiven gibt es nicht

def swap(a, b):
    a,b = b,a
    print(f"a={a} b={b}")
    return (a,b)

x = 11
y = 22

swap(x, y)

print(f"x={x} y={y}")

(x,y) = swap(x,y)
print(f"x={x} y={y}")
