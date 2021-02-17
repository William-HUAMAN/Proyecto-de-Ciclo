from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class Login(Screen):
    pass

class MedicoApp(MDApp):
    def build(self):
        self.title='Medic-App'
        self.theme.cls.primary_palette='Blue'
        return Builder.load_file('main.kv')


MedicoApp().run()