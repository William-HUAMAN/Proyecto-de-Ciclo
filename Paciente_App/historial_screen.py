from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#Para el Banner
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color,RoundedRectangle
from functools import partial

from conexion_BD import Conexion_BD

kv="""
<HistorialScreen>:
    name:'historial_screen'
    BoxLayout:
        BoxLayout:
            MDLabel:
                text:'pantalla de historial'
        BoxLayout:
            MDLabel:
                text:'No ha seleccionado ningun dato'

"""

class HistorialScreen(MDScreen):
    Builder.load_string(kv)
    
    def __init__(self,**kw):
        super().__init__(**kw)
        
        self.filas_pacientes=Conexion_BD()
    
    def on_pre_enter(self):
        pass
        #self.filas_pacientes.obtener_pacientes()


