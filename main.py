from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CalkulatorMidApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Пользователь", halign="center")


CalkulatorMidApp().run()