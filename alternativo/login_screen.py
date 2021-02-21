from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

kv="""
<LoginScreen>
    name:'Login_screen'
    MDLabel:
        text:'pantalla de inicio'
"""
class LoginScreen(MDScreen):
    Builder.load_string(kv)