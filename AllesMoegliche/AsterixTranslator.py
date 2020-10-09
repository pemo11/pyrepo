# Übersetzung der Axterix-Namen in verschiedene Sprachen
# https://de.wikipedia.org/wiki/Asterix#Figuren


dicDe = {"Miraculix":("","Der Druide"),"Majestix":("", "Der Häuptling"),"Gutemine":("", "Die Frau des Häuptlings"),"Idefix":("","Der Hund von Asterix")}
dicFr = {"Miraculix":("Panoramix",""),"Majestix":("Abraracourcix", ""),"Gutemine":("Bonemine",""),"Idefix":("Idéfix","")}
dicPo = {"Miraculix":("Panoramix",""),"Majestix":("Matasetix ", ""),"Gutemine":("Naftalina", ""),"Idefix":("Idéiafix","")}
dicEn = {"Miraculix":("Getafix",""),"Majestix":("Vitalstatistix", ""),"Gutemine":("Impedimenta",""),"Idefix":("Dogmatix","")}
dicUs = {"Miraculix":("Magigimmix",""),"Majestix":("Macroeconomix", ""),"Gutemine":("Belladona",""),"Idefix":("Dogmatix","")}
dicIt = {"Miraculix":("Panoramix",""),"Majestix":("Abraracourcix", ""),"Gutemine":("Beniamina",""),"Idefix":("Idefix","")}
dicEs = {"Miraculix":("Panorámix",""),"Majestix":("Abraracúrcix", ""),"Gutemine":("Karabella",""),"Idefix":("Ideafix","")}
dicNl = {"Miraculix":("Panoramix",""),"Majestix":("Abraracourcix", ""),"Gutemine":("Bellefleur",""),"Idefix":("Idefix","")}
dicSe = {"Miraculix":("Miraculix",""),"Majestix":("Majestix", ""),"Gutemine":("Bonemine",""),"Idefix":("Idefix","")}

dicFiguren = {"deutsch":dicDe, "Französisch":dicFr, "Portugiesisch":dicPo, "Amerikanisch":dicUs,
 "Italienisch":dicIt, "Spanisch":dicEs, "Holländisch":dicNl, "Schwedisch":dicSe}

print(dicFiguren)

# Am Ende soll eine Übersetzung von z.B. "Obelix und Idefix gehen auf Wildschweinjagd" in eine andere Sprache
# durch Austausch der Namen möglich sein - Asterix und Obelix besitzen in allen Sprachen diesselben Namen
# Lernthema: Umgang mit Dictionaries
