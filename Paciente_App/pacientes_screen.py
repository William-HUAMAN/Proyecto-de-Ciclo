from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#Para el Banner
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color,RoundedRectangle
from functools import partial
from io import open
import time

from conexion_BD import MedicionesPacientes
from conexion_BD import Conexion_BD

kv="""
<PacientesScreen>:
    name:'pacientes_screen'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            sise_hint_y:.8
            MDLabel:
                text:' subir datos'
        BoxLayout
            sise_hint_y:.2
            MDRaisedButton:
                text:'Enviar dato'
                on_release:root.enviar_mediciones()
        
"""


class PacientesScreen(MDScreen):
    Builder.load_string(kv)
    
    def __init__(self,**kw):
        super().__init__(**kw)
        
        self.insertar=Conexion_BD()
    
    def enviar_mediciones(self):
        f=open('info_paciente.txt','r')
        lineas_texto=f.readlines()
        f.close()
        dni=int(lineas_texto[2])
        fecha=time.strftime('%d/%m/%Y')
        fecha_int=int(time.strftime('%Y%m%d'))
        hora=time.strftime("%I:%M:%S %p")
        hora_int=int(time.strftime("%H%M%S")) 
        pulso=150#cambiar depende de sensor
        temperatura=36.5#cambiar depende de sensor
        oxigeno=80#cambiar depende de sensor
        self.mediciones=MedicionesPacientes(dni,fecha,fecha_int,hora,hora_int,pulso,temperatura,oxigeno)

        self.insertar.insertar_dato(self.mediciones.toCollection())
        
    # def on_pre_enter(self):
    #     self.filas_pacientes.obtener_pacientes()


