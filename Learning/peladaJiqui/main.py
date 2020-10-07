from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
import random

from peladaJiqui.screen_nav import change_screen

Window.size = (360, 600)

time1 = []
time2 = []
time3 = []
time4 = []
time5 = []
time6 = []
time7 = []

# No builder as classes são importadas automaticamente
# Builder.load_string(screen_helper)

class ScrollableLabel(ScrollView):
    pass


class MyLayout(MDBoxLayout):
    scr_mngr = ObjectProperty(None)

    def pegar_jogadores(self):
        jogadores = self.scr_mngr.screen1.jogadores.text

        text_file = open("jogadores.txt", "w+", encoding="utf-8")
        n = text_file.write(jogadores)
        text_file.close()

        file1 = open('jogadores.txt', 'r', encoding="utf-8")
        linhas_file1 = file1.readlines()

        count = 1
        lista_jogadores = []
        for line in linhas_file1:
            line = line.strip()
            lista_jogadores.append(line)
            print(f'Jogador {count}: {line}')
            count += 1

        random.shuffle(lista_jogadores)

        time_atual = 1
        quantidade_jogadores = 1
        time = {}
        for jogador in lista_jogadores:
            if quantidade_jogadores == 6:
                time_atual += 1
                quantidade_jogadores = 1

            time[jogador] = "Time" + str(time_atual)
            quantidade_jogadores += 1

        print(time.items())

        for key, value in time.items():
            if 'Time1' == value:
                time1.append(key)
            if 'Time2' == value:
                time2.append(key)
            if 'Time3' == value:
                time3.append(key)
            if 'Time4' == value:
                time4.append(key)
            if 'Time5' == value:
                time5.append(key)
            if 'Time6' == value:
                time6.append(key)
            if 'Time7' == value:
                time7.append(key)

        if jogadores != "":
            self.jogadores_time1()
            self.change_screen("screen2")

    def jogadores_time1(self):
        self.scr_mngr.screen2.time1.text = 'time1'

    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"

        screen = Builder.load_string(change_screen)

        return screen


DemoApp().run()
