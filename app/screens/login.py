from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from app.services.auth import AuthDB

Builder.load_file("app/ui/login.kv")

class LoginScreen(MDScreen):
    def do_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        cbox_active = self.ids.checkBox_terms.active

        if AuthDB().login_user(username, password):
            self.ids.status.text = "Login berhasil!"
        else:
            self.ids.status.text = "Login gagal. Coba lagi."
            