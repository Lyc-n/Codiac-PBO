from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from app.screens.login import LoginScreen
from app.screens.register import RegisterScreen
from app.screens.splash import SplashScreen
from app.screens.course_i import CourseScreen_i
from app.screens.course_ii import CourseScreen_ii
from app.screens.course_iii import CourseScreen_iii
from app.screens.course_iv import CourseScreen_iv
from app.screens.task_i import TaskScreen_i
from app.screens.pilihcourse import PilihCourse
from app.screens.teskemampuan import TesKemampuanScreen
from layoutbase import LayoutBase
from kivy.core.window import Window
from pathlib import Path
import json

#Untuk debugging windows
# Window.size = (405, 720)
# Window.minimum_width = 405
# Window.minimum_height = 720
# Window.left = 50
# Window.top = 50

#Initialize Components 
Builder.load_file("app/components/custombtn.kv")
# Builder.load_file("root.kv")

#Global Path
logsess = Path("data/session.json")


class MainApp(MDApp):
    def build(self):
        self.load_font()
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Dark" 

        self.sm = ScreenManager()
        self.sm.add_widget(SplashScreen(name="splash"))
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegisterScreen(name="register"))
        self.sm.add_widget(CourseScreen_i(name="course_i"))
        self.sm.add_widget(CourseScreen_ii(name="course_ii"))
        self.sm.add_widget(CourseScreen_iii(name="course_iii"))
        self.sm.add_widget(CourseScreen_iv(name="course_iv"))
        self.sm.add_widget(TaskScreen_i(name="task_i"))
        self.sm.add_widget(PilihCourse(name="pilihcourse"))
        self.sm.add_widget(LayoutBase(name="layoutbase"))
        self.sm.add_widget(TesKemampuanScreen(name="teskemampuan"))
        Clock.schedule_once(self.go_to_login, 4)

        return self.sm
    
    #Pindah ke LoginPage
    def go_to_login(self, dt):
        log = self.check_session()
        if log:
            self.sm.current = "layoutbase"
        else: 
            self.sm.current = "login"
    
    #Pindah ke RegisterPage
    def go_to_reg(self):
        self.sm.current = "register"
    
    #Pindah ke HomePage
    def go_to_home(self):
        self.sm.current = "layoutbase"
        
    #Pindah ke pilih
    def go_to_pilih(self):
        self.sm.current = "pilihcourse"
        
    #Cek Sessions untuk AutoLogin
    def check_session(self):
        if logsess.exists():
            with open(logsess, "r") as f:
                data = json.load(f)
            log_true = data.get("is_logged_in")
            return log_true
        else:
            return False
    
    def bahasa(self, pilih):
        if logsess.exists():
            with open(logsess, "r") as f:
                data = json.load(f)
                
            data["bahasa"]= pilih
            
            with open(logsess, "w") as f:
                json.dump(data, f, indent=4)
            self.go_to_home()
        else:
            return
        
    def change(self, changeS):
        self.sm.current = changeS
    
    def change_screen(self, screen_name):
        MDApp.get_running_app().root.get_screen("layoutbase").ids.screen_manager.current = screen_name

    def show_snackbar(self):
        dialog = MDDialog(
            text="belum tersedia",
            buttons=[
                MDFlatButton(
                    text="Tutup",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    #Tambah Font Custom
    def load_font(self):
      LabelBase.register(
        name= "Poppins",
        fn_regular= "assets/fonts/Poppins-Regular.ttf",
        fn_bold= "assets/fonts/Poppins-Bold.ttf",
        )
      LabelBase.register(
        name= "Inter",
        fn_regular= "assets/fonts/Inter-VariableFont_opsz,wght.ttf",
        fn_italic= "assets/fonts/Inter-Italic-VariableFont_opsz,wght.ttf",
        )
      LabelBase.register(
        name="CourierPrime",
        fn_regular="assets/fonts/CourierPrime-Regular.ttf",
        fn_bold="assets/fonts/CourierPrime-Bold.ttf",
      )
    
    
if __name__ == '__main__':
    MainApp().run()