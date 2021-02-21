from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

kv="""
<NavigationScreen>
    name:'navigation_screen'
    MDLabel:
        text:'pantalla de Navegacion'
"""
class NavigationScreen(MDScreen):
    Builder.load_string(kv)