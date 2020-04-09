"""
Title: ToDo Matrix
Author: Cameron Schweeder
Date: 2020.04.08
"""

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty




Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')


class ProjectPage(Screen):
    pass

class ContextPage(Screen):
    pass

class InBoxPage(Screen):
    pass
class NotesPage(Screen):
    pass
class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)

class TodoMatrix(App):
    def build(self):
        return WindowManager()


kv = Builder.load_file("todomatrix.kv")
sm = WindowManager()

if __name__ == "__main__":
    TodoMatrix().run()