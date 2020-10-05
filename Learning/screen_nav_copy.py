change_screen = """
MyLayout:
    scr_mngr: scr_mngr
    orientation: 'vertical'

    ScreenManager:
        id: scr_mngr
        screen1: screen1

        Screen:
            id: screen1
            name: 'screen1'
            username: username
            password: password

            MDCard:
                size_hint: None, None
                size: dp(520), dp(340)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                BoxLayout:
                    orientation:'vertical'
                    padding: dp(20)
                    spacing:20

                    MDLabel:
                        text: 'Connexion'
                        theme_text_color: 'Secondary'
                        size_hint_y: None
                        height: dp(36)

                    MDSeparator:
                        height: dp(1)

                    MDTextField:
                        id: username
                        hint_text: "Username "
                        helper_text_mode: "on_focus"

                    MDTextField:
                        id: password
                        hint_text: "Password "
                        helper_text_mode: "on_focus"
                        password: True

                    MDFlatButton:
                        text: "Connexion"
                        pos_hint: {'center_x': 0.5}
                        on_release: root.check_data_login()
        Screen:
            name: 'screen2'

            MDToolbar:
                id: toolbar
                title: "Welcome ! "
                pos_hint: {'center_x': 0.5, 'center_y': 0.97}
                md_bg_color: app.theme_cls.primary_color
                background_palette: 'DeepPurple'
                background_hue: 'A400'
                right_action_items: [['animation', lambda x: MDThemePicker().open()]]

            MDLabel:
                theme_text_color: 'Primary'
                text: "Data :"
                height: self.texture_size[1] + dp(3)
                halign: 'center'
                pos_hint: {'center_x': 0.5, 'center_y': 0.85}
"""
