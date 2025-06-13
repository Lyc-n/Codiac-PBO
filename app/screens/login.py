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
            app = self.get_app()
            app.go_to_pilih()
        else:
            self.ids.status.text = "Login gagal. Coba lagi."
            
    #Buat Login Session
    def log_session(self, username):
        data = {
            "username": username,
            "is_logged_in": True,
            "bahasa": "c++"
        }
        with open("data/session.json", "w") as f:
            json.dump(data, f, indent=4)  
    
    #Login tanpa session
    def not_log_session(self, username):
        data = {
            "username": username,
            "is_logged_in": False,
            "bahasa": "c++"
        }
        with open("data/session.json", "w") as f:
            json.dump(data, f, indent=4)
      
    def get_app(self):
        from kivy.app import App
        return App.get_running_app()