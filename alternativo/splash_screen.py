from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
#Para la conexion con la BD
from conexion_BD import Conexion_BD
#importando pantallas
from navigation_screen import NavigationScreen
from login_screen import LoginScreen
#transicion
from kivy.clock import Clock

kv="""
<SplashScreen>
    name: "splash_screen"
    md_bg_color:app.theme_cls.primary_color
    Image:
        source:'recursos/imagenes/logo.png'
        size_hint:(.5,.5)
        pos_hint:{'center_x':.5,'center_y':.5}
"""
class SplashScreen(MDScreen):
    Builder.load_string(kv)

    def __init__(self,**kw):
        super().__init__(**kw)
        self.app=MDApp.get_running_app()
        self.mi_conexion=Conexion_BD()
        

    def on_enter(self):
        pantalla_navegacion=NavigationScreen()
        pantalla_inicio=LoginScreen()
        self.app.root.add_widget(pantalla_navegacion)
        self.app.root.add_widget(pantalla_inicio)
        try:
            with open("mi_conexion.txt","r") as f:
                codigo_acceso=f.read()
                self.mi_conexion.verificar_mi_conexion(codigo_acceso)
                Clock.schedule_once(lambda dt:self.cargar_navegacion(),10)

        except:
            Clock.schedule_once(lambda dt:self.cargar_login(),10)
            #print('cambiar al login')
    
    def cargar_navegacion(self):
        self.app.root.current='navigation_screen'
    
    def cargar_login(self):
        self.app.root.current='login_screen'
