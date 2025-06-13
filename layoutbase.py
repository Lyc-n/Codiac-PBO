#from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
from app.screens.home import HomeScreen
from app.screens.bookmark import BookmarkScreen
from app.screens.timer import TimerScreen

Builder.load_file("layoutbase.kv")
# Builder.load_file("app/ui/home.kv")
# Builder.load_file("app/ui/bookmark.kv")
# Builder.load_file("app/ui/timer.kv")

class LayoutBase(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.load_screen)
        
    def load_screen(self, dt):
        self.ids.screen_manager.add_widget(HomeScreen(name="home"))
        self.ids.screen_manager.add_widget(BookmarkScreen(name="bookmark"))
        self.ids.screen_manager.add_widget(TimerScreen(name="timer"))
        