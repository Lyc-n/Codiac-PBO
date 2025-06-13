from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from kivy.core.audio import SoundLoader

Builder.load_file("app/ui/timer.kv")

class TimerScreen(MDScreen):
    time_left = NumericProperty(0)
    time_display = StringProperty("00:00:00")
    is_running = BooleanProperty(False)
    hour_text = StringProperty("Jam")
    minute_text = StringProperty("Menit")
    second_text = StringProperty("Detik")
    _event = None

    def on_pre_enter(self):
        self.create_menus()

    def create_menus(self):
        self.hour_menu = MDDropdownMenu(
            caller=self.ids.hour_picker,
            items=[{"text": str(i), "on_release": lambda x=i: self.set_time("hour", x)} for i in range(0, 24)],
            width_mult=3,
        )
        self.minute_menu = MDDropdownMenu(
            caller=self.ids.minute_picker,
            items=[{"text": str(i), "on_release": lambda x=i: self.set_time("minute", x)} for i in range(0, 60)],
            width_mult=3,
        )
        self.second_menu = MDDropdownMenu(
            caller=self.ids.second_picker,
            items=[{"text": str(i), "on_release": lambda x=i: self.set_time("second", x)} for i in range(0, 60)],
            width_mult=3,
        )

    def set_time(self, unit, value):
        if unit == "hour":
            self.hour_text = str(value)
        elif unit == "minute":
            self.minute_text = str(value)
        elif unit == "second":
            self.second_text = str(value)

        # Tutup semua menu
        self.hour_menu.dismiss()
        self.minute_menu.dismiss()
        self.second_menu.dismiss()

    def start_timer(self):
        if self.is_running:
            return

        try:
            h = int(self.hour_text) if self.hour_text.isdigit() else 0
            m = int(self.minute_text) if self.minute_text.isdigit() else 0
            s = int(self.second_text) if self.second_text.isdigit() else 0
        except:
            toast("Pilih durasi dulu!")
            return

        self.time_left = h * 3600 + m * 60 + s
        if self.time_left <= 0:
            toast("Durasi harus lebih dari 0")
            return

        self.update_time_display()
        self.is_running = True
        self._event = Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_time_display()
        else:
            self.timer_done()

    def timer_done(self):
        self.stop_timer()
        self.update_time_display()
        toast("⏰ Waktu habis!")
        self.play_alarm()

    def play_alarm(self):
        sound = SoundLoader.load("assets/250629__kwahmah_02__alarm1.mp3")
        if sound:
            sound.play()

    def stop_timer(self):
        self.is_running = False
        if self._event:
            self._event.cancel()
            self._event = None

    def reset_timer(self):
        self.stop_timer()
        self.time_left = 0
        self.time_display = "00:00:00"

    def update_time_display(self):
        m, s = divmod(self.time_left, 60)
        h, m = divmod(m, 60)
        self.time_display = f"{h:02}:{m:02}:{s:02}"
