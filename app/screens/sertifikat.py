from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import json

Builder.load_file("app/ui/sertifikat.kv")

class SertifikatScreen(MDScreen):
    def markdone(self):
        # Buka dan muat data JSON
        with open("data/session.json", "r") as file:
            data = json.load(file)
        
        # Tambahkan key baru
        data["studykasus"] = True
        data["sertif"] = data.get("sertif", 0) + 1
        
        # Simpan kembali ke file
        with open("data/session.json", "w") as file:
            json.dump(data, file, indent=4)
    