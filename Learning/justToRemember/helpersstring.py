username_helper = """
MDTextField: 
    hint_text: "Enter username"
    helper_text: "Forgot your username?"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None 
    width: 300
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color

"""
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Pelada Jiqui'
            icon: 'play'
            elevation: 10
        MDLabel:
            text: 'Hello World'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["soccer", lambda x: app.navigation_draw()]]
                mode: 'center'
                type: 'bottom'
                on_action_button: app.navigation_draw()
                icon: 'play'

"""