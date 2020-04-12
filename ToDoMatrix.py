"""
Title: ToDo Matrix
Author: Cameron Schweeder
Date: 2020.04.08
"""

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty




Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')

class NavBar(Widget):
    inboxpng = str('./img/InBox.png')
    inboxDeactive = str('./img/InBoxDeactive.png')
    notespng = str('./img/Notes.png')
    notesDeactive = str('./img/NotesDeactive.png')
    projectpng = str('./img/projects.png')
    projectpng = str('./img/ProjectsDeactive.png')

    def currentScreenIcon(self, event):
        print(self,event)
        self.event = event

        if self.event == "InBox":
            print("You Pressed the Inbox button!")
            self.inboxDeactive = str('./img/InBox.png')
        elif self.event == "Project":
            print("You Pressed the Project Button!")
        elif self.event == "Context":
            print("You Pressed the Context Button!")
        else:
            print("You pressed the Notes button!")
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
        return sm




kv = Builder.load_file("todomatrix.kv")
sm = WindowManager(transition=NoTransition())

if __name__ == "__main__":
    TodoMatrix().run()

