# Kurvenberechnung nach Casteljau
# Erstellt: 29/11/20
# Stimmt exakt mit dem Ergebnis aus dem Skript, Seite 177 überein
# Die Frage t nur, warum es mehrere Durchläufe geben soll

p = {}
p[(0,0)] = (1,1)
p[(1,0)] = (2,4)
p[(2,0)] = (4,3)
p[(3,0)] = (5,0)

def casteljau(l):
    n = 3   # Kurvengrad, in der Regel 3 
    a = len(l.keys())
    a = 4
    du = round(1 / (a - 1),2)
    u = du
    while u < 1:
        print(f"*** Durchlauf mit u={u} ***")
        for j in range(0,n):
            for i in range(0,n-j):
                x = round((1-u) * l[(i,j)][0] + u * l[(i+1,j)][0],3)
                y = round((1-u) * l[(i,j)][1] + u * l[(i+1,j)][1],3)
                l[(i,j+1)] = (x,y)
                print(f"p({i},{j+1})={l[(i,j+1)]}")
        u += du

casteljau(p)