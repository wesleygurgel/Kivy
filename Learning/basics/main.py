from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Red Green Blue VALUES
Window.clearcolor = (0, 0, 0, 1)
Window.size = (360, 600)


class MainApp(App):
    def build(self):
        # Label
        label = Label(text='This is Batman.', font_size='20sp', bold=True,
                      color=(1, 1, 1, 1))

        # ---------------------------------------------------------------------

        # Button                                    widht, height
        button = Button(text='Print this', size_hint=(0.15, 0.15),
                        font_size='20sp',
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        on_press=self.printpress,
                        on_release=self.printrelease)

        # DEFAULT: HORIZONTAL
        btn1 = Button(text='Button1')
        btn2 = Button(text='Button2')
        btn3 = Button(text='Button3')

        layout_button = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout_button.add_widget(btn1)
        layout_button.add_widget(btn2)
        layout_button.add_widget(btn3)

        # return layout_button

        # ---------------------------------------------------------------------

        # Images + Box Layout
        img = Image(source='cute.png')
        btn_img = Button(text='Login',
                         size_hint=(None, None),
                         width=100,
                         height=50,
                         pos_hint={'center_x': 0.5})

        layout_img = BoxLayout(orientation='vertical', spacing=100, padding=50)
        layout_img.add_widget(img)
        layout_img.add_widget(btn_img)

        # return layout_img

        # ---------------------------------------------------------------------

        # Grid System

        layout_grid = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        btn1_grid = Button(text='Hello 1', size_hint=(None, None), width=100, height=40)
        btn2_grid = Button(text='World 1')

        btn3_grid = Button(text='Hello 2', size_hint=(None, None), width=100, height=40)
        btn4_grid = Button(text='World 2')

        layout_grid.add_widget(btn1_grid)
        layout_grid.add_widget(btn2_grid)
        layout_grid.add_widget(btn3_grid)
        layout_grid.add_widget(btn4_grid)

        # return layout_grid

        # ---------------------------------------------------------------------

        # Text Input
        self.weight = TextInput(text= 'Enter Weight Here')
        self.height = TextInput(text= 'Enter Height Here')

        button_input = Button(text='Submit', on_press=self.submit)

        layout_input = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10, padding=20)

        layout_input.add_widget(self.weight)
        layout_input.add_widget(self.height)
        layout_input.add_widget(button_input)

        return layout_input


    def submit(self, obj):
        print("Weight: " + self.weight.text)
        print("Height: " + self.height.text)


    def printpress(self, obj):
        print("Button has been pressed")

    def printrelease(self, obj):
        print("Button has been released")


MainApp().run()
