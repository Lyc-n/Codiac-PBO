from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
import json

Builder.load_file("app/ui/tsscpp.kv")
Builder.load_file("app/ui/course/c++/tessoal/soal_i.kv")
Builder.load_file("app/ui/course/c++/tessoal/soal_ii.kv")
Builder.load_file("app/ui/course/c++/tessoal/soal_iii.kv")
Builder.load_file("app/ui/course/c++/tessoal/soal_iv.kv")
Builder.load_file("app/ui/course/c++/tessoal/soal_v.kv")

class TssCpp(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.load_screen)
        self.user_answer = {}
    
    def on_enter(self):
        self.waktu = 25
        self.ids.timer_label.text = f"sisa {self.waktu}"
        self.event = Clock.schedule_interval(self.update_timer, 1)
    
    def update_timer(self, dt):
        self.waktu -= 1
        if self.waktu >= 0:
            self.ids.timer_label.text = f"sisa {self.waktu}"
        else:
            Clock.unschedule(self.event)
            self.timer_selesai()
            
    def timer_selesai(self):
        self.ids.timer_label.text = "Waktu Habis!"
        # Contoh: Panggil fungsi dari App
        self.show_score()
        
    def load_screen(self, dt):
        self.ids.screen_manager.add_widget(Soal_i(name="soal_i"))
        self.ids.screen_manager.add_widget(Soal_ii(name="soal_ii"))
        self.ids.screen_manager.add_widget(Soal_iii(name="soal_iii"))
        self.ids.screen_manager.add_widget(Soal_iv(name="soal_iv"))
        self.ids.screen_manager.add_widget(Soal_v(name="soal_v"))
        
        
    def select_one(self, selected_btn):
            # Ambil screen saat ini
            layout = selected_btn.parent
    
            # Reset semua tombol di dalam layout
            for widget in layout.children:
                if hasattr(widget, "md_bg_color") and not isinstance(widget, MDBoxLayout):
                    widget.md_bg_color = (0.1, 0.1, 0.2, 1)
    
            # Aktifkan warna pada tombol yang diklik
            selected_btn.md_bg_color = (0.2, 0.2, 0.3, 1)
        
            # Simpan jawaban: ambil nama screen dan nilai benar/salah
            current_screen = self.ids.screen_manager.current  # misalnya: "task_i"
            self.answer_keys = {
                "soal_i": "Hello, World!",
                "soal_ii": "Hasil: 8",
                "soal_iii": "15",
                "soal_iv": "Modulus: 1",
                "soal_v": "Nilai: 1"
            }
            # Anggap jawaban yang benar adalah "==", ubah sesuai kebutuhan
            is_correct = selected_btn.custext == self.answer_keys.get(current_screen, "")
    
            # Simpan ke dict
            self.user_answer[current_screen] = is_correct

    def calculate_score(self):
        total = len(self.user_answer)
        benar = sum(1 for x in self.user_answer.values() if x)
        if total == 0:
            return 0
        return round((benar / total) * 100)
        
    def show_score(self):
        skor = self.calculate_score()
        if not self.verif():
            self.markdone()
        # Akses screen lain lewat app.root
        score_screen = MDApp.get_running_app().root.get_screen("scorecourse")
        score_screen.ids.score_label.text = f"Skor Anda: {skor}%"
        # Pindah ke screen skor
        MDApp.get_running_app().root.current = "scorecourse"
        
        
    def markdone(self):
        # Buka dan muat data JSON
        with open("data/session.json", "r") as file:
            data = json.load(file)
        
        # Tambahkan key baru
        data["teskemampuanncpp"] = True
        data["task"] = data.get("task", 0) + 1
        
        # Simpan kembali ke file
        with open("data/session.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def verif(self):
        with open("data/session.json", "r") as file:
            data = json.load(file)
            done = data.get("teskemampuanncpp", False)
        return done
        
class Soal_i(MDScreen): pass
class Soal_ii(MDScreen): pass
class Soal_iii(MDScreen): pass
class Soal_iv(MDScreen): pass
class Soal_v(MDScreen): pass