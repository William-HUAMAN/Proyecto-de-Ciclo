#Creación de pantalla de KivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from splash_screen import SplashScreen

class PacienteApp(MDApp):
    def build(self):
        sm=ScreenManager()
        self.title='Pacient-App'
        self.theme_cls.primary_palette='Blue'
        return sm
    
    def on_start(self):
        ss=SplashScreen()
        self.root.add_widget(ss)
        self.root.current='splash_screen'

PacienteApp().run()