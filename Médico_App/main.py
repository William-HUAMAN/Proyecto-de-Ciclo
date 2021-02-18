from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class Informacion(Screen):
    pass

class Login(Screen):
    pass

class Pacientes(Screen):
    pass

class MedicoApp(MDApp):
    def build(self):
        self.title='Medic-App'
        self.theme_cls.primary_palette='Blue'
        return Builder.load_file('main.kv')
    
    def cerrar_sesion(self):
        print('cerrar')


MedicoApp().run()