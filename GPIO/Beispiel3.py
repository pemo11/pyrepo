# Übung Nr. 3: Dauerblinken durch Endlosschleife
# Module importieren 

import RPi.GPIO as GPIO 
import time 

# Pins vorbereiten 
GPIO.setmode(GPIO.BOARD)

pinNr = 7
wartezeit = 3
GPIO.setup(pinNr, GPIO.OUT) 

while True:
    # Pin einschalten
    GPIO.setup(pinNr, GPIO.HIGH) 
    time.sleep(wartezeit) 
    # Pin ausschalten
    GPIO.setup(pinNr, GPIO.LOW) 
    time.sleep(wartezeit)
