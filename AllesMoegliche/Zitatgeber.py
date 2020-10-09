# Ein Zitat pro Aufruf

import random

zitate = []

with open("Zitate.txt", "r") as fhandle:
   zitate = fhandle.readlines()
   
z = random.randint(0, len(zitate) - 1)

print(zitate[z])