from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from app.services.auth import AuthDB

Builder.load_file("app/ui/register.kv")

class RegisterScreen(MDScreen):
    def do_reg(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        cpassword = self.ids.cpassword.text
        cbox_active = self.ids.checkBox_terms.active

        if password!=cpassword:
            self.ids.status.text = "password tidak sama"
            return
        if not cbox_active:
            self.ids.status.text = "centang persetujuan dulu.."
            return
        if AuthDB().register_user(username, email, password):
            self.ids.status.text = "Login berhasil!"
            self.do_log()
        else:
            self.ids.status.text = "Login gagal. Coba lagi."
            
    def do_log(self):
        self.ids.status.text = "Balik ke login"
        app = self.get_app()
        app.go_to_login(dt=None)
    
    #hubungkan ke main.py    
    def get_app(self):
      from kivy.app import App
      return App.get_running_app()
      