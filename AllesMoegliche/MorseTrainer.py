# Morse-Trainer
# Erstellt: 06/09/20
import winsound

duration = 500
shortFreq = 440
longFreq = 1000

morseCodes = {"A":"·−","B":"−···","C":"−·−·","D":"−··","E":".","F":"··−·","G":"−−·","H":"....","I":"..","J":".---","K":"-.-",
              "L":"·−··","M":"--","N":"-.","O":"---","P":".--.","Q":"−−·−","R":".-.","S":"...","T":"-","U":"..-",
              "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}

wort = input("Wort?")

# Das geht: winsound.PlaySound("SystemExit", winsound.SND_ALIAS), beep nicht

for c in wort.upper():
    morse = morseCodes[c]
    for m in morse: 
        print(m)
        if m == ".":
            winsound.Beep(shortFreq, duration)
        else:
            winsound.Beep(longFreq, duration)

