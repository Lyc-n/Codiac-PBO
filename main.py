from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from app.screens.login import LoginScreen
from app.screens.register import RegisterScreen
from app.screens.splash import SplashScreen
from app.screens.home import HomeScreen
from pathlib import Path
import json

#Initialize Components 
Builder.load_file("app/components/custombtn.kv")

#Global Variable 
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
        self.sm.add_widget(HomeScreen(name="home"))

        Clock.schedule_once(self.go_to_login, 4)

        return self.sm
    
    #Pindah ke LoginPage
    def go_to_login(self, dt):
        log = self.check_session()
        if log:
            self.go_to_home()
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
    
    #Deklarasi Warna Custom
    satu = get_color_from_hex("#191A29")
    light = get_color_from_hex("#C3BDCE")
    dark = get_color_from_hex("#1D162A")
    
if __name__ == '__main__':
    MainApp().run()