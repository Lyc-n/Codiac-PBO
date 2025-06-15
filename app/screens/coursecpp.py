from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file("app/ui/coursecpp.kv")
Builder.load_file("app/ui/course/c++/pengenalan/course_i.kv")
Builder.load_file("app/ui/course/c++/pengenalan/course_ii.kv")
Builder.load_file("app/ui/course/c++/pengenalan/course_iii.kv")
Builder.load_file("app/ui/course/c++/pengenalan/course_iv.kv")
Builder.load_file("app/ui/course/c++/pengenalan/course_v.kv")
Builder.load_file("app/ui/course/c++/pengenalan/task_i.kv")
Builder.load_file("app/ui/course/c++/pengenalan/task_ii.kv")
Builder.load_file("app/ui/course/c++/pengenalan/task_iii.kv")
Builder.load_file("app/ui/course/c++/pengenalan/task_iv.kv")
Builder.load_file("app/ui/course/c++/pengenalan/task_v.kv")

class CourseCpp(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.load_screen)
        self.user_answer = {}
        
    def load_screen(self, dt):
        self.ids.screen_manager.add_widget(CourseScreen_i(name="course_i"))
        self.ids.screen_manager.add_widget(CourseScreen_ii(name="course_ii"))
        self.ids.screen_manager.add_widget(CourseScreen_iii(name="course_iii"))
        self.ids.screen_manager.add_widget(CourseScreen_iv(name="course_iv"))
        self.ids.screen_manager.add_widget(CourseScreen_v(name="course_v"))
        self.ids.screen_manager.add_widget(TaskScreen_i(name="task_i"))
        self.ids.screen_manager.add_widget(TaskScreen_ii(name="task_ii"))
        self.ids.screen_manager.add_widget(TaskScreen_iii(name="task_iii"))
        self.ids.screen_manager.add_widget(TaskScreen_iv(name="task_iv"))
        self.ids.screen_manager.add_widget(TaskScreen_v(name="task_v"))
        
        
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
                "task_i": "Mendeklarasikan pustaka",
                "task_ii": "Mengakhiri program dengan status sukses",
                "task_iii": "float",
                "task_iv": "Mengambil input dari pengguna",
                "task_v": "=="
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
        # Akses screen lain lewat app.root
        score_screen = MDApp.get_running_app().root.get_screen("scorecourse")
        score_screen.ids.score_label.text = f"Skor Anda: {skor}%"
        # Pindah ke screen skor
        MDApp.get_running_app().root.current = "scorecourse"



class CourseScreen_i(MDScreen): pass
class CourseScreen_ii(MDScreen): pass
class CourseScreen_iii(MDScreen): pass
class CourseScreen_iv(MDScreen): pass
class CourseScreen_v(MDScreen): pass
class TaskScreen_i(MDScreen): pass
class TaskScreen_ii(MDScreen): pass
class TaskScreen_iii(MDScreen): pass
class TaskScreen_iv(MDScreen): pass
class TaskScreen_v(MDScreen): pass