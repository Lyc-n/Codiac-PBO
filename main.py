from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from app.screens.login import LoginScreen
from app.screens.register import RegisterScreen
from app.screens.splash import SplashScreen

Builder.load_file("app/components/custombtn.kv")

class MainApp(MDApp):
    def build(self):
        self.load_font()
        self.theme_cls.primary_palette = "Blue"  # Set warna tema utama
        self.theme_cls.theme_style = "Dark"  # Set tema utama

        self.sm = ScreenManager()
        self.sm.add_widget(SplashScreen(name="splash"))
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegisterScreen(name="register"))
        
        
        Clock.schedule_once(self.go_to_login, 4)

        return self.sm
    
    def go_to_login(self, dt):
        self.sm.current = "login"
        
    def go_to_reg(self):
        self.sm.current = "register"
        
    def load_font(self):
      LabelBase.register(
        name= "Poppins",
        fn_regular= "assets/fonts/Poppins-Regular.ttf",
        fn_bold= "assets/fonts/Poppins-Bold.ttf",
        )

if __name__ == '__main__':
    MainApp().run()