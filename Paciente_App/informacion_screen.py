from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#from login_screen import LoginScreen
import webbrowser

kv="""
<InformacionScreen>:
    name:'information_screen'
    Screen:
        FitImage:
            source:'recursos/imagenes/fondo_2.jpg'
        BoxLayout:
            id:box
            orientation: 'vertical'
            size_hint: .6,.75
            height: self.minimum_height
            pos_hint: {"center_x": .5,"center_y": .5 }
            padding:"30dp","15dp","30dp","30dp"
            spacing:'10dp'

            canvas:
                Color: 
                    rgba: 1,1,1, .5
                RoundedRectangle:
                    pos:self.pos
                    size:self.size
                    radius: 10,10,10,10

            MDLabel:
                id:indicaciones
            MDRaisedButton:
                pos_hint: {"center_x": .5,"center_y": .5 }
                text: "Regístrese aquí"
                text_color: 1,0,0,1
                md_bg_color: 1, 1, 1, 1
                on_release:root.enviar_al_enlace()
"""

class InformacionScreen(MDScreen):
    Builder.load_string(kv)
    def on_pre_enter(self, *args):
        self.ids["indicaciones"].text='ga \n ga'

    def enviar_al_enlace(self):
        webbrowser.open('https://stark-spire-16180.herokuapp.com/reg_medico#')
        