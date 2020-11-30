# Woche 3, Aufgabe 2

# Gesucht ist die Verstärkung eines Mikrofonvorverstärkers Vdb
import math

uMic = 7.75 # Eingangsspannung in mV
dLtg = 6 # Dämpfung der Leitung db
dBu = 6 # dbu Pegel am Ausgang

V = math.pow(10, dBu/20)

print("Verstärkungsfaktor=%.2f" % V)

# Wo kommt uMic ins Spiel?