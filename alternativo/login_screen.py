from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

kv="""
<LoginScreen>
    name:'login_screen'
    MDLabel:
        text:'pantalla de inicio'
"""
class LoginScreen(MDScreen):
    Builder.load_string(kv)