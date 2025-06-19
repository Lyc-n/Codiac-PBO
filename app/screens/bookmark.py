from kivymd.uix.screen import MDScreen
from kivy.factory import Factory
from kivy.lang import Builder
import json, os

Builder.load_file("app/ui/bookmark.kv")

class BookmarkScreen(MDScreen):
    def on_enter(self):
        self.tampilkan_materi()

    def tampilkan_materi(self):
        box = self.ids.materi_box
        box.clear_widgets()
    
        try:
            # Pastikan file ada dulu (opsional, tapi rapi)
            if not os.path.exists("data/materi.json"):
                raise FileNotFoundError("File materi.json tidak ditemukan.")
    
            # Baca file JSON
            with open("data/materi.json") as f:
                data = json.load(f)
    
        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
            return  # keluar dari fungsi tanpa memuat apapun
    
        except json.JSONDecodeError as e:
            print(f"❌ Format JSON rusak: {e}")
            return
    
        # Kalau aman, tampilkan materi
        for key, value in data.items():
            if key.startswith("m_") and value:
                btn = Factory.Course()
                btn.ctext = f"Materi {key.upper()}"
                btn.rtext = "pemula"
                btn.dtext = "materi pengenalan c++"
                btn.on_release = lambda x=key: print(f"{x} ditekan")
                box.add_widget(btn)