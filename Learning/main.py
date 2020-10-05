from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpersstring import username_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, MDList, ThreeLineListItem, ThreeLineIconListItem, \
    ThreeLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget, ImageRightWidget
from kivy.uix.scrollview import ScrollView

Window.size = (360, 600)
# No builder as classes são importadas automaticamente
list_helper = """
Screen:
    ScrollView:
        MDList:
            id: mylist
                
"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        for i in range(20):
            items = OneLineListItem(text='Item ' + str(i))
            self.root.ids.mylist.add_widget(items)


DemoApp().run()
