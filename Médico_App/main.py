#Creación de pantalla de KivyMD
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import webbrowser

class Informacion(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.app=MDApp.get_running_app()
        
    def on_pre_enter(self, *args):
        self.app.title="Información"






class Login(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.app=MDApp.get_running_app()
        
    def on_pre_enter(self, *args):
        self.app.title="Inicio de Sesión"
    
    def ir_enlace(self):
        print ('ir enlace')









class Pacientes(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.app=MDApp.get_running_app()
        
    def on_pre_enter(self, *args):
        self.app.title="Pacientes"






        

class MedicoApp(MDApp):
    def build(self):
        self.title='Medic-App'
        self.theme_cls.primary_palette='Blue'
        return Builder.load_file('main.kv')
    
    def cerrar_sesion(self):
        print('cerrar')


MedicoApp().run()