# Übung Nr. 2: Ein Lauflicht mit mehreren PINs
# Module importieren 

import RPi.GPIO as GPIO 
import time 

# Pins vorbereiten 
GPIO.setmode(GPIO.BCM)
 
# Nummern der Pins zusammenfassen 

pinListe = [5,6,13,19,26] 

# Alle Pins auf Ausgabe schalten 
for pin in pinListe: 
   GPIO.setup(pin, GPIO.OUT) 


# Wieder alle Pins durchgehen 
for pin in pinListe: 
    # Pin einschalten
    GPIO.setup(pin, GPIO.HIGH) 
    time.sleep(2) 
    # Pin ausschalten
    GPIO.setup(pin, GPIO.LOW) 
