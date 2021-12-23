import random
import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# Make Sure This Is Always the last import
from kivy import Config
Config.set('graphics', 'multisamples', '0')

restList = [] #List that will hold the restuarants
class MyGrid(Widget):
    
    restaurant = ObjectProperty(None)
    choice = ObjectProperty(None)

    def addrest(self):
        restList.append(self.restaurant.text)
        self.restaurant.text = ""
        
        print(restList) #Shows up the list as elements are added on.

    def btn(self):
        self.choice.text = random.choice(restList) #Chooses a random element to eat at.

# Main Code
class MyApp(App): #Must be same name lowercase for the kv style file
    def build(self):
        return MyGrid()

# Run This Thing
if __name__ == "__main__":
    MyApp().run()

