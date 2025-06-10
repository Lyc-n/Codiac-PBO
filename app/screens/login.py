from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from app.services.auth import AuthDB
import json

Builder.load_file("app/ui/login.kv")

class LoginScreen(MDScreen):
    def do_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        cbox_active = self.ids.checkBox_terms.active
        
        if cbox_active:
            self.log_session(username)
        else:
            self.not_log_session(username)
        
        if AuthDB().login_user(username, password):
            self.ids.status.text = "Login berhasil!"
        else:
            self.ids.status.text = "Login gagal. Coba lagi."
            
    #Agar tidak perlu login berulang
    def log_session(self, username):
        data = {
            "username": username,
            "is_logged_in": True
        }
        
        with open("data/session.json", "w") as f:
            json.dump(data, f, indent=4)  
            
    def not_log_session(self, username):
        data = {
            "username": username,
            "is_logged_in": False
        }
        
        with open("data/session.json", "w") as f:
            json.dump(data, f, indent=4)  