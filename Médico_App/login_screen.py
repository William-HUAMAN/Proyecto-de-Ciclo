from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from conexion_BD import Conexion_BD
from kivymd.app import MDApp
# importado para ir al enlace
import webbrowser
#importando la pantalla de navegacion
from navigation_screen import NavigationScreen

kv="""
<LoginScreen>:
    name:'login_screen'
    Screen:
        FitImage:
            source:'recursos/imagenes/fondo_1.jpg'
        
        BoxLayout:
            id:box
            orientation: 'vertical'
            size_hint: .45,.7
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
                text:'INICIO DE SESIÓN'
                bold:True
                theme_text_color:'Custom'
                text_color:0,0,0,1
                halign:'center'
            MDLabel:
                text:'Bienvenido!'
                bold:True
            MDLabel:
                text:'Necesitamos que nos brindes algunos datos para poder hacer uso de este servicio'
                font_style:'Caption'
            MDTextFieldRound:
                id:correo
                icon_left:'mail'
                pos_hint:{'center_x':.5}
                normal_color: 1,1,1,.5
                icon_left_color: 0,0,0
            
            MDTextFieldRound:
                id:password
                icon_left:'lock'
                pos_hint:{'center_x':.5}
                normal_color: 1,1,1,.5
                icon_left_color: 0,0,0
                
            MDRaisedButton:
                text:'Iniciar'
                pos_hint:{'center_x':.5}
                on_release:root.iniciar_sesion()
            
            BoxLayout:
                orientation:'horizontal'
                MDLabel:
                    text:'Si no posee una cuenta,regístrese en el siguiente'
                    font_style:'Caption'
                    pos_hint_x:.5
                MDRaisedButton:
                    text:'enlace'
                    text_color: 0, 0, 1, 1
                    md_bg_color:1,1,1,.6
                    #font_size: "18sp"
                    on_release: root.ir_enlace()
"""
class LoginScreen(MDScreen):
    Builder.load_string(kv)

    def __init__(self,**kw):
        super().__init__(**kw)
        self.app=MDApp.get_running_app()#
        self.mi_conexion=Conexion_BD()

        pantalla_navegacion=NavigationScreen()
        self.app.root.add_widget(pantalla_navegacion)

    
    def iniciar_sesion(self):
        if self.mi_conexion.inicio_sesion(self.ids.correo.text,self.ids.password.text) ==False:
            print('a ocurrido un error')
            self.ids.correo.text=''
            self.ids.password.text=''
        else:
            self.app.root.current='navigation_screen'
        # print(self.ids.correo.text)
        # print(self.ids.password.text)
        

    def ir_enlace(self):
        webbrowser.open('https://stark-spire-16180.herokuapp.com/reg_medico#')
        