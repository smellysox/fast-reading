import time
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Label
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import StringProperty

class ScreenManagement(ScreenManager):
    pass
class MainScreen(Screen):
    Word = StringProperty
    def __init__(self,**kwargs):
        super(MainScreen, self).__init__(**kwargs)
    def doit(self):
        return 0
    def writing(self):
        f = open('example.txt')
        for word in f.read().split():
            Word = word
            return(word)
        f.close()
presentation = Builder.load_file("bekethingie.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == "__main__":
        MainApp().run()