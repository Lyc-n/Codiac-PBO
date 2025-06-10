from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import json

Builder.load_file("app/ui/home.kv")

class HomeScreen(MDScreen):
    def getNameUser(self):
        with open("data/session.json", "r") as f:
            data = json.load(f)
            uname = data.get("username")
        return uname
    
    def search(self):
        pass
    