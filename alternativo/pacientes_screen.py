from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
kv="""
<PacientesScreen>:
    name:'pacientes_screen'
    MDLabel:
        text:'pantalla de Pacientes'
"""

class PacientesScreen(MDScreen):
    Builder.load_string(kv)
