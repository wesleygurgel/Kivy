change_screen = """
Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                    
                    Widget:



        MDNavigationDrawer:
            id: nav_drawer
    
"""