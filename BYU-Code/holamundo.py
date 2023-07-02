from kivy.app import App
from kivy.uix.label import Label


class kivySaludo(App):

    def build(self):
        return Label(text="Hola mundo")

kivySaludo().run()