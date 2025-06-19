from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.lang import Builder
from pathlib import Path
import json

Builder.load_file("app/ui/profile.kv")
logsess = Path("data/session.json")

class ProfileScreen(MDScreen):
    uname = StringProperty("sedang dimuat...")
    sertif = StringProperty("0")
    task = StringProperty("0")
    
    def on_enter(self):
        if logsess.exists():
            with open("data/session.json", "r") as f:
                    data = json.load(f)
                    self.uname = data.get("username", "user")
                    self.sertif = str(data.get("sertif", 0))
                    self.task = str(data.get("task", 0))
        else: pass

    def logout(self):
        nama_file = "data/session.json"
        with open(nama_file, "r") as f:
            data = json.load(f)
        data["is_logged_in"] = False
        with open(nama_file, "w") as f:
            json.dump(data, f, indent=4)    