# FFT-Analyse an einem Beispiel
# https://pythontic.com/visualization/signals/fouriertransform_fft
# Es werden zwei Sinus-Wellen (Signale) erzeugt und überlagert
# Das Resultat wird per FFT analysiert und es werden vier Kurven angezeigt
# Erstellt: 28/10/20

import numpy as np
import matplotlib.pyplot as plotter

samplingFrequency = 100
samplingInterval = 1 / samplingFrequency

beginTime = 0
endTime = 10

signal1Frequency = 4
signal2Frequency = 7

time = np.arange(beginTime, endTime, samplingInterval)

amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)

axis[0].set_title("Sinuswelle 4 Hz")
axis[0].plot(time, amplitude1)
axis[0].set_xlabel("Zeit")
axis[0].set_ylabel("Amplitude")

axis[1].set_title("Sinuswelle 7 Hz")
axis[1].plot(time, amplitude2)
axis[1].set_xlabel("Zeit")
axis[1].set_ylabel("Amplitude")

# Aufaddieren der beiden Sinuswellen-Werte

amplitude = amplitude1 + amplitude2

axis[2].set_title("Sinuswelle mehrere Frequenzen")
axis[2].plot(time, amplitude)
axis[2].set_xlabel("Zeit")
axis[2].set_ylabel("Amplitude")

# Anwenden von FFT
fourierTransform = np.fft.fft(amplitude)/len(amplitude)
fourierTransform = fourierTransform[range(int(len(amplitude)/2))]

tpCount = len(amplitude)
values = np.arange(int(tpCount/2))
timePeriod  = tpCount / samplingFrequency
frequencies = values / timePeriod

axis[3].set_title("Das FFT-Ergebnis")
axis[3].plot(frequencies, abs(fourierTransform))
axis[3].set_xlabel("Frequenz")
axis[3].set_ylabel("Amplitude")

plotter.show()
 
