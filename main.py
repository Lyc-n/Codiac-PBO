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
from app.screens.home import HomeScreen
from app.screens.timer import TimerScreen
from app.screens.bookmark import BookmarkScreen
# from root import Root
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
        # Builder.load_file("app/components/custombtn.kv")
        # Builder.load_file("root.kv")

        self.sm = ScreenManager()
        self.sm.add_widget(SplashScreen(name="splash"))
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegisterScreen(name="register"))
        # self.sm.add_widget(Root(name="root"))
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(BookmarkScreen(name="bookmark"))
        self.sm.add_widget(TimerScreen(name="timer"))
        Clock.schedule_once(self.go_to_login, 4)

        return self.sm
    
    #Pindah ke LoginPage
    def go_to_login(self, dt):
        log = self.check_session()
        if log:
            self.sm.current = "home"
        else: 
            self.sm.current = "login"
    
    #Pindah ke RegisterPage
    def go_to_reg(self):
        self.sm.current = "register"
    
    #Pindah ke HomePage
    def go_to_home(self):
        self.sm.current = "home"
        
    #Cek Sessions untuk AutoLogin
    def check_session(self):
        if logsess.exists():
            with open(logsess, "r") as f:
                data = json.load(f)
            log_true = data.get("is_logged_in")
            return log_true
        else:
            return False
        
    def change_screen(self, screen_name):
        self.sm.current = screen_name

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
    
    
if __name__ == '__main__':
    MainApp().run()