from re import MULTILINE
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
from kivy.uix.image import Image, AsyncImage
import serial

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

class test(GridLayout):
    def prinrelease1(self, obj):
               c= CallPy()
               c.call_python_file()
    def prinrelease2(self, obj):
        c= CallPy2()
        c.call_python_file2()

        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button1 = Button(text= "B", size_hint = (0.2,0.2), font_size = '20sp', pos_hint={'center_x' :0.5, 'center_y' :0.1},  on_release= self.prinrelease1,)#size_hite = (breite,Höhe)
        self.button1.bind(on_release= self.prinrelease1)         
        self.add_widget(Label())
        self.add_widget(self.button1)

        self.button2 = Button(text= "A", size_hint = (0.2,0.2), font_size = '20sp', pos_hint={'center_x' :0.5, 'center_y' :0.1},  on_release= self.prinrelease1,)#
        self.button2.bind(on_release= self.prinrelease2)         
        self.add_widget(Label())
        self.add_widget(self.button2)
    
        # self.img = AsyncImage(source = 'https://image.freepik.com/free-vector/flat-black-white-guitar-illustration_72147494527.jpg')

        self.username = TextInput( multiline = False)
        self.add_widget(self.username)

        self.username3 = TextInput( multiline = False)
        self.add_widget(self.username3)

        
        self.username2 = TextInput(multiline = False)

        self.add_widget(self.username2)




class MainApp(App):
    def build(self):
        return test()

 # def build(self):
        # img = AsyncImage(source = 'https://image.freepik.com/free-vector/flat-black-white-guitar-illustration_72147494527.jpg')
        # return img
if __name__=='__main__':
    MainApp().run()