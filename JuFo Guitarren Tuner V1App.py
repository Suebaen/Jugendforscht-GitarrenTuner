from subprocess import call
import numpy as np
import sys
import pyaudio
import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.widget import Widget
from kivy.uix.image import Image, AsyncImage
import serial
# import time 
# from time import sleep
import speech_recognition as s_r
class CallPy(object):

    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasA.py'):
        self.path =path
    
    def  call_python_file(self):
        call(["Python3", "{}".format(self.path)])
class CallPy2(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasC.py'):
        self.path =path
    
    def  call_python_file2(self):
        call(["Python3", "{}".format(self.path)])
class CallPy3(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasD.py'):
        self.path =path
    
    def  call_python_file3(self):
        call(["Python3", "{}".format(self.path)])
class CallPy4(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasE.py'):
        self.path =path
    
    def  call_python_file4(self):
        call(["Python3", "{}".format(self.path)])

class CallPy5(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasF.py'):
        self.path =path
    
    def  call_python_file5(self):
        call(["Python3", "{}".format(self.path)])

class CallPy6(object):
    def __init__(self,path = '/Users/benjamin/Documents/GitHub/Jugendforscht-GitarrneTuner/SteppMotorV2/include/NurDasG.py'):
        self.path =path
    
    def  call_python_file6(self):
        call(["Python3", "{}".format(self.path)])


class test(GridLayout):
    def prinrelease1(self, obj):
               c= CallPy()
               c.call_python_file()
    def prinrelease2(self, obj):
        c= CallPy2()
        c.call_python_file2()

    def prinrelease3(self, obj):
        c= CallPy3()
        c.call_python_file3()

    def prinrelease4(self, obj):
        c= CallPy4()
        c.call_python_file4()

    def prinrelease5(self, obj):
        c= CallPy5()
        c.call_python_file5()
        
    def prinrelease6(self, obj):
        c= CallPy6()
        c.call_python_file6()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        # self.button1 = Button(text= "A", size_hint = (0.2,0.2), font_size = '20sp',
        #                 pos_hint={'center_x' :0.5, 'center_y' :0.1}, #size_hite = (breite,Höhe)
        #                 on_release= self.prinrelease1,)
        self.button1 = Button(text= "A")#, size_hint = (0.2,0.2), font_size = '20sp', pos_hint={'center_x' :0.5, 'center_y' :0.1},  on_release= self.prinrelease1,)#size_hite = (breite,Höhe)
        self.button1.bind(on_release= self.prinrelease1)         
        self.add_widget(Label())
        self.add_widget(self.button1)

        self.button2 = Button(text= "C")
        self.button2.bind(on_release= self.prinrelease2)         
        self.add_widget(Label())
        self.add_widget(self.button2)

        self.button3 = Button(text= "D")
        self.button3.bind(on_release= self.prinrelease3)         
        self.add_widget(Label())
        self.add_widget(self.button3)

        self.button4 = Button(text= "E")
        self.button4.bind(on_release= self.prinrelease4)         
        self.add_widget(Label())
        self.add_widget(self.button4)

        self.button5 = Button(text= "F")
        self.button5.bind(on_release= self.prinrelease5)         
        self.add_widget(Label())
        self.add_widget(self.button5)

        self.button6 = Button(text= "G")
        self.button6.bind(on_release= self.prinrelease6)         
        self.add_widget(Label())
        self.add_widget(self.button6)
    
        # self.img = AsyncImage(source = 'https://image.freepik.com/free-vector/flat-black-white-guitar-illustration_72147494527.jpg')




class MainApp(App):
    def build(self):
        return test()

MainApp().run()
    
    
    
    
    
    
    
     # def build(self):
        # img = AsyncImage(source = 'https://image.freepik.com/free-vector/flat-black-white-guitar-illustration_72147494527.jpg')
        # return img