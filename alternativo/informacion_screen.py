

from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
kv="""
<InformacionScreen>:
    name:'information_screen'
    MDLabel:
        text:'pantalla de Informacion'
"""

class InformacionScreen(MDScreen):
    Builder.load_string(kv)
