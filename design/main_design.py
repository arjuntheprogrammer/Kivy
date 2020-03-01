from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv = Builder.load_file("my_design.kv")

class MyGrid(Widget):
    firstName = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("first name: ", self.firstName.text, " email: ", self.email.text)
        self.firstName.text = ""
        self.email.text = ""
    pass

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
