change_screen = """
MyLayout:
    scr_mngr: scr_mngr
    orientation: 'vertical'

    ScreenManager:
        id: scr_mngr
        screen1: screen1
        jogadores: jogadores

        Screen:
            id: screen1
            name: 'screen1'
            jogadores: jogadores
            
            MDBoxLayout:
                orientation:'vertical'
                padding: 20
                spacing: 20

                MDLabel:
                    text: 'Pelada Jiqui'
                    theme_text_color: 'Custom'
                    font_style: 'Button'
                    text_color: (1, 0, 0, 1)
                    halign: 'center'
                    size_hint: None, None
                    size: 100, 10
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
                MDTextField:
                    id: jogadores
                    hint_text: 'Digite o nome dos Jogadores'
                    helper_text: 'Digite o nome e pressione "ENTER"'
                    helper_text_mode: 'on_focus'
                    current_hint_text_color: 1, 1, 1, 1
                    multiline: True
                    mode: "rectangle"            
                                    
                MDRectangleFlatIconButton:
                    icon: 'soccer'
                    text: "Formar Times"
                    pos_hint: {'center_x': 0.5}
                    text_color: 1, 1, 1, 1
                    md_bg_color: 1, 0, 0, 1
                    on_release: root.pegar_jogadores()
                        
                Widget:
                    
                    
             
        Screen:
            id: screen2
            name: 'screen2'
            time1: time1

            ScrollView:
                do_scroll_x: False
                do_scroll_y: True
            
                BoxLayout:
                    orientation:'vertical'
                    padding: 20
                    spacing: 20
                    
                    MDToolbar:
                        id: toolbar
                        title: "Times Formados!"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.90}
                        md_bg_color: app.theme_cls.primary_color
                        background_palette: 'Brown'
                        background_hue: '50'

                    MDLabel:
                        id: time1
                        theme_text_color: 'Primary'
                        text: 'Time 1: '
                        height: self.texture_size[1] + dp(3)
                        halign: 'center'
                        pos_hint: {'center_x': 0.1, 'center_y': 0.80}
                        
                    MDLabel:
                        theme_text_color: 'Primary'
                        text: 'Time 2: '
                        height: self.texture_size[1] + dp(3)
                        halign: 'center'
                        pos_hint: {'center_x': 0.1, 'center_y': 0.80}
                    
                    MDLabel:
                        theme_text_color: 'Primary'
                        text: 'Time 3: '
                        height: self.texture_size[1] + dp(3)
                        halign: 'center'
                        pos_hint: {'center_x': 0.1, 'center_y': 0.80}
                    
                    MDLabel:
                        theme_text_color: 'Primary'
                        text: 'Time 4: '
                        height: self.texture_size[1] + dp(3)
                        halign: 'center'
                        pos_hint: {'center_x': 0.1, 'center_y': 0.80}
                    
                    MDLabel:
                        theme_text_color: 'Primary'
                        text: 'Time 5: '
                        height: self.texture_size[1] + dp(3)
                        halign: 'center'
                        pos_hint: {'center_x': 0.1, 'center_y': 0.80}
                    
                    MDLabel:
                        theme_text_color: 'Primary'
                        text: 'Time 6: '
                        height: self.texture_size[1] + dp(3)
                        halign: 'center'
                        pos_hint: {'center_x': 0.1, 'center_y': 0.80}
                    
                    MDLabel:
                        theme_text_color: 'Primary'
                        text: 'Time 7: '
                        height: self.texture_size[1] + dp(3)
                        halign: 'center'
                        pos_hint: {'center_x': 0.1, 'center_y': 0.80}

"""
