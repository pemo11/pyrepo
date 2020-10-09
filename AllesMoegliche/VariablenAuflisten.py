# Auflisten aller Variablen eines Programms
# Erstellt: 23/09/20

# dir() - list of in scope variable
# globals() -  a dictionary of global variables
# locals() - dictionary of local variables

a = 1
b = 2
c = 3
y = "Hallo, Python!"

varNames = [v for v in locals() if v != None and not v.startswith("__")]

print(varNames)