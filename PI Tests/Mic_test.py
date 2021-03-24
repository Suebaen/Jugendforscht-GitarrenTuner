#!/usr/bin/env python
import pyaudio
from pprint import pprint

p = pyaudio.PyAudio()


# SUCCEEDS
pprint(p.is_format_supported(input_format=pyaudio.paInt8,input_channels=1,rate=44100,input_device=0)) # => True
try:
    stream = p.open(format=pyaudio.paInt8,channels=1,rate=44100,input=True,frames_per_buffer=1024)
    data = stream.read(1024)
except IOError as e:
    print ('This never happens: '+str(e))

# FAILS
pprint(p.is_format_supported(input_format=pyaudio.paInt8,input_channels=1,rate=22050,input_device=0)) # => True
try:
    stream = p.open(format=pyaudio.paInt8,channels=1,rate=22050,input=True,frames_per_buffer=1024)
    data = stream.read(1024)
except IOError as e:
    print ('This fails: '+str(e))

# FAILS
pprint(p.is_format_supported(input_format=pyaudio.paInt8,input_channels=1,rate=22050,input_device=0)) # => True
try:
    stream = p.open(format=pyaudio.paInt8,channels=1,rate=22050,input=True,frames_per_buffer=512)
    data = stream.read(1024)
except IOError as e:
    print ('This also fails: '+str(e))

# FAILS
pprint(p.is_format_supported(input_format=pyaudio.paInt8,input_channels=1,rate=11025,input_device=0)) # => True
try:
    stream = p.open(format=pyaudio.paInt8,channels=1,rate=11025,input=True,frames_per_buffer=512)
    data = stream.read(1024)
except IOError as e:
    print ('This also fails as well: '+str(e))

stream.stop_stream()
stream.close()
p.terminate()