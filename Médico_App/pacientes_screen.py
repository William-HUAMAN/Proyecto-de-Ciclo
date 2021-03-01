from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#Para el Banner
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color,RoundedRectangle
from functools import partial

from conexion_BD import Conexion_BD
from io import open

class Banner(FloatLayout):
    
    def __init__(self,apellidos,nombre, **kwargs):
        self.apellidos=str(apellidos)
        self.nombres=str(nombre)
        self.inicial='a'
        super().__init__()
        with self.canvas.before:
            Color(rgba=(0,.5,1,.1))
            self.rect=RoundedRectangle(radius=[(15.0,15.0),(15.0,15.0),(15.0,15.0),(15.0,15.0)])
        
        self.bind(pos=self.update_rect,size=self.update_rect)

        #etiquetas del banner
        self.title_apellidos=MDLabel(text=self.apellidos,pos_hint={'center_x': .5, 'center_y':.5},size_hint=(.2,.3),halign='center')
        self.title_nombres=MDLabel(text=self.nombres,pos_hint={'center_x': .5, 'center_y':.5},size_hint=(.2,.3),halign='right')
        self.icono=MDIcon(icon='alpha-'+self.inicial+'-circle',halign='left')
        #agregar widget
        self.add_widget(self.icono)
        self.add_widget(self.apellidos)
        self.add_widget(self.title_nombres)
    
    def update_rect(self,*args):
        self.rect.pos=self.pos
        self.rect.size=self.size
   

kv="""
<PacientesScreen>:
    name:'pacientes_screen'
    BoxLayout:
        BoxLayout:
            ScrollView:
                id:Scroll
                GridLayout:
                    id:grid_banner
                    cols:1
                    padding:[20,20,20,20]
                    size_hint_y:None
                    height:self.minimum_height
                    row_default_height:50
                    padding:'10dp'
                    spacing:'10dp'
        BoxLayout:
            MDLabel:
                text:'No ha seleccionado ningun paciente'

"""

class PacientesScreen(MDScreen):
    Builder.load_string(kv)
    
    def __init__(self,**kw):
        super().__init__(**kw)
        
        self.filas_pacientes=Conexion_BD()
    
    def on_pre_enter(self):
        f=open('info_medico.txt','r')
        linea_texto=f.readlines()
        f.close()
        centro=str(linea_texto[3])
        self.lista_pacientes=self.filas_pacientes.obtener_pacientes(centro)
        print(self.lista_pacientes)
        #añadiendo al scroll
        self.grid=self.ids['grid_banner']
