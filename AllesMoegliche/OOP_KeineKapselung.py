# Keine echte Kapselung in Python
# Erstellt: 29/09/20

# Globale Variablen

staedte = {"ES":("Esslingen",80000),"PO":("Plochingen",24000),"GP":("Göppingen",44000), "NT":("Nürtingen",28000)}

# Klassendefinition

class Stadt:

    def __init__(self, Abkz):
        # Fehler: Attribut Abkz sollte durch die Schreibweise self.__Abkz privat gemacht werden
        self.Abkz = Abkz

    # Diese Methode kann nicht direkt aufgerufen werden, da sie privat ist
    def __Einwohner(self, Abkz):
        if staedte.get(self.Abkz) != None:
            return staedte[self.Abkz][1]

    # Nicht optimal - diese Methode kann auch direkt aufgerufen werden, da sie nicht privat ist
    def Stadtname(self, Abkz):
        # Nicht optimal, da staedte außerhalb der Klasse definiert ist
        if staedte.get(self.Abkz) != None:
            return staedte[self.Abkz][0]

    # Dies sollte die einzige "öffentliche" Methode sein
    def Info(self):
        return f"Name: {self.Stadtname(self.Abkz)} - Einwohner: {self.__Einwohner(self.Abkz)}"

    # Offiziell werden Attribute über Properties abgerufen


ES = Stadt("ES")
print(ES.Info())

# Geht, sollte aber nicht gehen
print(ES.Stadtname("ES"))

# Geht, sollte definitiv nicht gehen
print(ES.Abkz)

# Geht nicht, da privat
print(ES.__Einwohner("ES"))

