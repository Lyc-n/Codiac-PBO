from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from pathlib import Path
import json

Builder.load_file("app/ui/home.kv")
logsess = Path("data/session.json")

class HomeScreen(MDScreen):
    def getNameUser(self):
        if logsess.exists():
            with open("data/session.json", "r") as f:
                data = json.load(f)
                uname = data.get("username")
            return uname
        else:
            uname = "user"
            return uname
    
    def search(self):
        pass
    