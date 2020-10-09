# Eher eine "Spaß-Aufgabe"
# Beweise, dass eine beliebige Zahl x, die zuerst verdoppelt, dann um 6 vergrößert wird, danach halbiert wird
# und danach vom dem Ergebnis die Ausgangszahl x abgezogen wird, immer 3 ergibt
# Wie erhalte ich 3 anstelle von 3.0?

z = int(input("Zahl?"))

print((z * 2 + 6) / 2 - z)