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
<PacientesScreen>:
    name:'pacientes_screen'
    BoxLayout:
        BoxLayout:
            MDLabel:
                text:'pantalla de Pacientes'
        BoxLayout:
            MDLabel:
                text:'No ha seleccionado ningun paciente'

"""

#clase encargada de crear las filas
# class Banner(FloatLayout):
    
#     def __init__(self,hora,actividad, **kwargs):
#         self.hora=hora
#         self.actividad=actividad
#         super().__init__()
#         with self.canvas.before:
#             Color(rgba=(0,.5,1,.1))
#             self.rect=RoundedRectangle(radius=[(20.0,20.0),(20.0,20.0),(20.0,20.0),(20.0,20.0)])
        
#         self.bind(pos=self.update_rect,size=self.update_rect)

#         #etiquetas
#         self.title_hora=MDLabel(text=self.hora,pos_hint={'center_x': .1, 'center_y':.5},size_hint=(.15,.3),halign='center')
        
#         self.title_actividad=MDLabel(text=self.actividad,pos_hint={'center_x': .6, 'center_y':.5},size_hint=(.75,.3),halign='left')

#         self.menos=MDIconButton(icon='close',pos_hint={'center_x': .95, 'center_y':.5},on_release=kwargs['on_release'])

#         self.add_widget(self.title_hora)
#         self.add_widget(self.title_actividad)
#         self.add_widget(self.menos)
    
#     def update_rect(self,*args):
#         self.rect.pos=self.pos
#         self.rect.size=self.size



class PacientesScreen(MDScreen):
    Builder.load_string(kv)
    
    def __init__(self,**kw):
        super().__init__(**kw)
        
        self.filas_pacientes=Conexion_BD()
    
    def on_pre_enter(self):
        self.filas_pacientes.obtener_pacientes()


