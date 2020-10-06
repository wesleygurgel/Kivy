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
            jogadores: jogadores

            MDCard:
                size_hint: 0.9, 0.9
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                BoxLayout:
                    orientation:'vertical'
                    padding: dp(25)
                    spacing:20

                    MDLabel:
                        text: 'Connexion'
                        theme_text_color: 'Custom'
                        font_style: 'Button'
                        text_color: (1, 0, 0, 1)
                        halign: 'center'
                        size_hint_y: None
                        height: dp(10)

                    MDSeparator:
                        height: dp(1)

                    MDTextField:
                        id: jogadores
                        multiline: True
                        hint_text: "Nome dos Jogadores"
                        mode: "rectangle"
                        helper_text_mode: "on_focus"
                        helper_text: "Insira o nome e aperte 'Enter'"

                    
                    MDRectangleFlatIconButton:
                        icon: 'soccer'
                        text: "Formar Times"
                        text_color: 1, 1, 1, 1
                        pos_hint: {'center_x': 0.5}
                        md_bg_color: 1, 0, 0, 1
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
