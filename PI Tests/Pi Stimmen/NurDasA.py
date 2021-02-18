#! /usr/bin/env python
#########################################################

import numpy as np
from numpy.lib import index_tricks
import pyaudio
import speech_recognition as s_r
import RPi.GPIO as GPIO          
from time import sleep


def TonA():

    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=0)# in die Klammer (device_index=0)
    print(my_mic)




    in1 = 24
    in2 = 23
    en = 25
    temp1=1

    # GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    # GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    # p=GPIO.PWM(en,1000)

    Das_ist_ein_A4 = ('A4.75', 0.003337767668014635)
    Das_ist_ein_A2 = ('E4.333333333333333', 0.005231129721877892)



    gegen = "gegen den Uhrzeiger"
    mit= "mit dem Uhrzeiger"
    DieZeit = 1
    PerfekteNote = 3
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


    NOTE_MIN = 60       # C4
    NOTE_MAX = 69       # A4
    FSAMP = 48000 #22050       # Sampling frequency in Hz
    FRAME_SIZE = 2048   # How many samples per frame?  
    FRAMES_PER_FFT = 16 # FFT takes average across how many frames?

    SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
    FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT


    NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()



    def freq_to_number(f): return 69 + 12*np.log2(f/440.0)
    def number_to_freq(n): return 440 * 2.0**((n-69)/12.0)
    def note_name(n): return NOTE_NAMES[n % 12] + str(n/12 - 1)


    def note_to_fftbin(n): return number_to_freq(n)/FREQ_STEP
    imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN-1))))
    imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX+1))))


    buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
    num_frames = 0

    # Initialize audio
    stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=FSAMP,
                                    input=True,
                                    frames_per_buffer=FRAME_SIZE)


    freq1 = 440.08
    window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, SAMPLES_PER_FFT, False)))
    print ('sampling at', FSAMP, 'Hz with max resolution of', FREQ_STEP, 'Hz')



    while stream.is_active():


        buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
        buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE, exception_on_overflow = False), np.int16)

        # Run the FFT on the windowed buffer
        fft = np.fft.rfft(buf * window)

        # Get frequency of maximum response in range
        freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP
        # Get note number and nearest note
        n = freq_to_number(freq)
        n0 = int(round(n))

        # Console output once we have a full buffer
        num_frames += 1
        
        pyaudio.get_portaudio_version()

    

        if num_frames >= FRAMES_PER_FFT:
            print ('freq: {:9.4f} Hz     note: {:>3s} {:+.2f}'.format(
                freq, note_name(n0), n-n0))
        
    #  A4  

        if  (note_name(n0), n-n0) < (Das_ist_ein_A4):
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            print("backward")
            print (mit)
            
            print(A)

            
        elif (note_name(n0), n-n0) > (Das_ist_ein_A4):
            print (gegen)
            if(temp1==1):
             GPIO.output(in1,GPIO.HIGH)
             GPIO.output(in2,GPIO.LOW)
            print(A)

        else:
            A += 1
            print('Super das ist ein Perfektes A')

            print(A)

        if A <= PerfekteNote:
            print (note_name(n0), n-n0)
            
            print(A)

        else:
            break    

        
    #  A4  

        if  (note_name(n0), n-n0) < (Das_ist_ein_A2):
            
            print (mit)
            if(temp1==1):
             GPIO.output(in1,GPIO.LOW)
             GPIO.output(in2,GPIO.HIGH)
            print(A)

            
        elif (note_name(n0), n-n0) > (Das_ist_ein_A2):
            print (gegen)
            if(temp1==1):
             GPIO.output(in1,GPIO.HIGH)
             GPIO.output(in2,GPIO.LOW)
            print(A)
            
        else:
            A += 1
            print('Super das ist ein Perfektes A')
            print(A)

        if A <= PerfekteNote:
            print (note_name(n0), n-n0)
            print(A)

        else:
            break 



