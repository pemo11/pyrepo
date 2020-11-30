# Matrix-Multiplikation ohne Numpy
# Erstellt: 06/11/20

# Ergebnis stimmt

def MatrixMul(M1, M2):
    # Passen die Dimensionen?
    if len(M1) != len(M2[0]):
        print("*** Dimensionen passen nicht ***")
        exit
    # Leere Matrix mit Nullen anlegen
    M3 = [[0 for i in range(len(M1))] for j in range(len(M2))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                M3[i][j] += M1[i][k] * M2[k][j]
    return M3

def MatrixOut(M):
    for i in range(len(M)):
        line = " ".join([str(M[i][j]) for j in range(len(M[i]))])
        print(line)


# Wichtig: Liste = Zeile, nicht Spalte
M1 = [[8,12,-11],
      [14,7,3],
      [-6,4,21]]

M2 = [[3,9,-1],
      [16,7,3],
      [-6,-4,13]]

M3 = MatrixMul(M1, M2)

MatrixOut(M3)

M1 = [[4,2],[1,0]]
M2 = [[2,-1],[3,2]]

M3 = MatrixMul(M1, M2)
MatrixOut(M3)
