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
            id:Box_historial
            orientation: 'vertical'
            height: self.minimum_height
            padding:"30dp","15dp","30dp","30dp"

            canvas:
                Color: 
                    rgba: 1,0,1, .6
                Rectangle:
                    pos:self.pos
                    size:self.size
                    

            MDLabel:
                halign:'center'
                text:'Datos enviados agdg ad ada dsgsg  dsg d gs g  fdf'
                color_text: 0,0,0,0
                #font_style:'H2'
                size_hint: (1,.15)
        
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
                text:'No ha seleccionado ningun dato'

"""

class HistorialScreen(MDScreen):
    Builder.load_string(kv)
    
    def __init__(self,**kw):
        super().__init__(**kw)
        
        self.filas_mis_datos=Conexion_BD()
    
    def on_pre_enter(self,*args):
        print('historial')
        #self.app.title="Historial"
        #self.filas_pacientes.obtener_pacientes()