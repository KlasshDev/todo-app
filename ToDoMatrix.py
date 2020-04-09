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




Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')


class ProjectPage(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class TodoMatrix(App):
    def build(self):
        return ProjectPage()

if __name__ == "__main__":
    TodoMatrix().run()