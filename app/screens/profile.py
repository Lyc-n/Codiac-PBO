from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.lang import Builder
from pathlib import Path
import json

Builder.load_file("app/ui/profile.kv")
logsess = Path("data/session.json")

class ProfileScreen(MDScreen):
    uname = StringProperty("sedang dimuat...")
    
    def on_enter(self):
        if logsess.exists():
            with open("data/session.json", "r") as f:
                    data = json.load(f)
                    self.uname = data.get("username", "user")
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
    