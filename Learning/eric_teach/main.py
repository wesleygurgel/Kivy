from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from eric_teach.ourstring import change_screen
from kivymd.theming import ThemeManager

Window.size = (360, 600)


class DemoApp(MDApp):
    def build(self):
        theme_cls = ThemeManager()

        screen = Builder.load_string(change_screen)

        return screen


DemoApp().run()
