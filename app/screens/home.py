from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.lang import Builder
from pathlib import Path
import json

Builder.load_file("app/ui/home.kv")
logsess = Path("data/session.json")

class HomeScreen(MDScreen):
    uname = StringProperty("sedang dimuat...")
    bhs = StringProperty("sedang dimuat...")
    
    def on_enter(self):
        if logsess.exists():
            with open("data/session.json", "r") as f:
                    data = json.load(f)
                    self.uname = data.get("username", "user")
                    self.bhs = data.get("bahasa", "c++")
        else: pass
                
    def getNameUser(self):
        if logsess.exists():
            with open("data/session.json", "r") as f:
                data = json.load(f)
                uname = data.get("username")
            return uname
        else:
            uname = "user"
            return uname
    
    def getBahasa(self):
        if logsess.exists():
            with open("data/session.json", "r") as f:
                data = json.load(f)
                bhs = data.get("bahasa")
            return bhs
        else:
            bhs = "c++"
            return bhs
    
    def search(self):
        pass
    