from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from screen_nav import change_screen

Window.size = (360, 600)


# No builder as classes são importadas automaticamente
# Builder.load_string(screen_helper)

class MyLayout(BoxLayout):
    scr_mngr = ObjectProperty(None)

    def check_data_login(self):
        jogadores = self.scr_mngr.screen1.jogadores.text

        print(jogadores)

        if jogadores != "":
            self.change_screen("screen2")

    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"

        screen = Builder.load_string(change_screen)

        return screen


DemoApp().run()
