from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

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