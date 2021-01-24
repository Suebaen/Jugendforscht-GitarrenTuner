#! /usr/bin/env python

import numpy as np
import sys
import pyaudio
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import serial

import speech_recognition as s_r
#####################################################################
print("Start")
port= "/dev/tty.HC-05-SPPDev"   #dev/tty.HC-05-SPPDev  tty.Bluetooth-Incoming-Port
# bluethooth= serial.Serial(port, 115200) # 9600) 115200

bluethooth = serial.Serial(port, 38400, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)#38400
print ("connectied")
bluethooth.flushInput()

r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)
print(my_mic)

def DasBLESignal_Rechts():
    bluethooth.write(b"N")
    input_data = bluethooth.readline()
    print(input_data.decode())


def DasBLESignal_Links():
    bluethooth.write(b"F")
    input_data = bluethooth.readline()
    print(input_data.decode())

Das_ist_ein_A4 = ('A4.75', 0.003337767668014635)
Das_ist_ein_A4_Raute = ('A#4.833333333333333', -0.018885406668275095)
Das_ist_ein_C4 = ('C4.', 0 -0.08014706457605314)
Das_ist_ein_C4_Raute = ('C#4.083333333333333', 0.0035821878896484804)
Das_ist_ein_D4=('D4.166666666666667', -0.016212240985851167)
Das_ist_ein_D4_Raute= ('D#4.25', -0.013435641316277724)
Das_ist_ein_E4 = ('E4.333333333333333', 0.005231129721877892)
Das_ist_ein_F4 = ('F4.416666666666667', 0.000664601985590707)
Das_ist_ein_F4_Raute = ('F#4.5', 0.005029562635286311)
Das_ist_ein_G4 = ('G4.583333333333333', 0.013800740096982622)
Das_ist_ein_G4_Route = ('G#4.666666666666667', -0.004903988515962965)

gegen = "gegen den Uhrzeiger"
mit= "mit dem Uhrzeiger"
DieZeit = 1
PerfekteNote = 9
WieOftDieFlascheNoteGepsieltWerdenDamitSieEinSiganlAbgiebt = 0

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0
K = 0

A1 = 0
A2 = 0
A1R = 0
A2R = 0
C1 = 0
C2 = 0
C1R = 0
C2R = 0
D1 = 0
D2 = 0
D1R = 0
D2R = 0
E1 = 0
E2 = 0
F1 = 0
F2 = 0
F1R = 0
F2R = 0
G1 = 0
G2 = 0
G1R = 0
G2R = 0


NOTE_MIN = 60       
NOTE_MAX = 69       
FSAMP = 22050       
FRAME_SIZE = 2048   
FRAMES_PER_FFT = 16 

######################################################################


SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT

######################################################################


NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()

######################################################################


def freq_to_number(f): return 69 + 12*np.log2(f/440.0)
def number_to_freq(n): return 440 * 2.0**((n-69)/12.0)
def note_name(n): return NOTE_NAMES[n % 12] + str(n/12 - 1)

######################################################################
def note_to_fftbin(n): return number_to_freq(n)/FREQ_STEP
imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN-1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX+1))))


buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32) # Ursprügnlich war stand da ... .float32 (mit float16 gieng alles gut)
num_frames = 0


stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)


freq1 = 440.08

window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, SAMPLES_PER_FFT, False)))

# Print initial text
print ('sampling at', FSAMP, 'Hz with max resolution of', FREQ_STEP, 'Hz')
print




while stream.is_active():

   
    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE, exception_on_overflow = False), np.int16)

    
    fft = np.fft.rfft(buf * window)

    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP
    #sleep(DieZeit)
    
    n = freq_to_number(freq)
    n0 = int(round(n))

    
    num_frames += 1
    
    pyaudio.get_portaudio_version()

    # auf 5 Kommastellen begrenzen
    # freq = float("{0:.5f}".format(freq))

    if num_frames >= FRAMES_PER_FFT:
        print ('freq: {:9.4f} Hz     note: {:>3s} {:+.2f}'.format(
            freq, note_name(n0), n-n0))

    
# #  A4#
  
    if  (note_name(n0), n-n0) < (Das_ist_ein_A4_Raute):
        print (mit)
        DasBLESignal_Rechts() #BLE Signal
 
    elif (note_name(n0), n-n0) > (Das_ist_ein_A4_Raute):
        print (gegen)
        DasBLESignal_Links() #BLE Signal

    else:
        B += 1
        print('Super das ist ein Perfektes A#')
    
    if B <= PerfekteNote:
           print (note_name(n0), n-n0)
           print(B)

    else:
        break    




