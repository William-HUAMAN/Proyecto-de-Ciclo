#Creación de pantalla de KivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from pantallas.splash_screen import SplashScreen
import webbrowser
  

class MedicoApp(MDApp):
    def build(self):
        sm=ScreenManager()
        self.title='Medic-App'
        self.theme_cls.primary_palette='Blue'
        return sm
    
    def on_start(self):
        ss=SplashScreen()
        self.root.add_widget(ss)
        self.root.current='splash_screen'
    
    def cerrar_sesion(self):
        print('cerrar')


MedicoApp().run()