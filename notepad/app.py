
import os
import logic
from kivy.app import App
from kivy.uix.label import Label


class Notepad(App):
    def build(self):
        return Label(text="hello")

Notepad().run()

