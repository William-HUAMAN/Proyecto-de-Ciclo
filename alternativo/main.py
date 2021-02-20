#Creación de pantalla de KivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import webbrowser
  

class MedicoApp(MDApp):
    def build(self):
        self.title='Medic-App'
        self.theme_cls.primary_palette='Blue'
        return Builder.load_file('main.kv')
    
    def cerrar_sesion(self):
        print('cerrar')


MedicoApp().run()