# Umgang mit Zeichenketten (auch Strings genannt)

# Zeichenketten werden in Anführungszeichen oder Apostrophe gesetzt

zk = "Informationssicherheitsmanagementsystem"

# Wie lang ist das Wort?
print(len(zk))

# len() ist eine eingebaute Function (kein Befehl)

# Wie viele i's enthält das Wort?
print(zk.count("i"))

# count() ist keine eingebaute Function, sondern eine sog. Methode, die auf ein Objekt angewendet wird
# Das Objekt ist die Zeichenkette in Gestalt der Variablen zk

# An welcher Position steht das erste s?
print(zk.index("s"))

# Beginnt die Nummerierung bei 0 oder 1?
print(zk[11]) # Gibt "s" zurück

print(zk[0]) # Gibt "I" zurück

# Oder so, auch wenn es keinen Sinn ergibt...
print(zk[zk.index("s")])

# Zeichen ersetzen
print(zk.replace("m", "M"))

# Alle Zeichen einzeln ausgeben (sehr einfach)
for z in zk:
    print(z)

# Das Wort in Großbuchstaben umwandeln und ausgeben
print(zk.upper())

# Ab jetzt wird es etwas anspruchsvoller...

# Zählen der Häufigkeit aller Buchstaben
h = {}
for z in zk:
    if h.get(z) == None:
        h[z] = 1
    else:
        h[z] += 1
print(h)

# Und jetzt wird es noch etwas anspruchsvoller
# Sortieren nach der Häufigkeit der Buchstaben (da musste ich auch erst einmal "nachschauen";)

hNeu = sorted(h.items(), key=lambda x: x[1])
print(hNeu)

# In absteigender Reihenfolge
hNeu = sorted(h.items(), key=lambda x: x[1], reverse=True)
print(hNeu)

'''
Python ist eine wunderbare Programmiersprache. Es macht richtig Spaß, sich mit ihr zu beschäftigen.
Die Syntax wurde so festgelegt, dass wenn man ein paar einfache Regeln kennt, sich vieles von alleine ergibt
Beispiel: Ich weiß, dass ich mit "abc".upper() eine Zeichenkette in Großbuchstaben umwandeln kann, dann 
denke ich mir, das ein "abc".count("a") die Anzahl der a's zählt (vielleicht besseres Beispiel)
Aber es gibt natürlich auch Menschen, die das nicht so sehen. Sie finden die Syntax von Python etwas
merkwürdig und stören sich z.B. daran, dass Variablen nicht "ordentlich" deklariert werden müssen,
und das das Einrücken einer Befehlszeile festgelegt, wie sie interpretiert wird.
Das ist aber vollkommen in Ordnung. Keine Programmiersprache ist perfekt, auch Python nicht.
Es kommt auf die Zielgruppe an. Python soll Menschen das Programmieren einfach machen und das macht es auch.
Dann sollen Menschen angesprochen werden, für die eine "richtige" Programmiersprache wie Java oder C++ nicht in
Frage kommt. Auch das macht Python hervorragend.
Das Schöne an Python ist, dass es trotzdem keine Einschränkungen gibt.
Wenn große Internetfirmen oder die NASA in den USA Python einsetzen, spricht das für ihr Potential
Man muss aber wissen, dass Python nicht für alles die beste Wahl ist, und dass es Menschen gibt,
die Vorlieben und Abneigungen haben. Auch das ist vollkommen normal
'''