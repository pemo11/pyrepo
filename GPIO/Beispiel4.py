# Übung Nr. 4 - PIN-Abfrage
# Module importieren 

import RPi.GPIO as GPIO 
import time 

# Pins vorbereiten 
GPIO.setmode(GPIO.BOARD)

pinNr = 5
wartezeit = 1
GPIO.setup(pinNr, GPIO.IN) 

def pinStatus(Nr):
    status = "Pin Nr. %d ist eingeschaltet" % pinNr if GPIO.input(pinNr) == 1 else "Pin-Nr. %d ist ausgeschaltet" % pinNr
    return status

while True:
    # Pin einschalten
    print(pinStatus(pinNr))
    time.sleep(wartezeit) 
