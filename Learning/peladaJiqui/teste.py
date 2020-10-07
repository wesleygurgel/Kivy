import random

jogadores = "Wesley\n" \
            "André\n" \
            "Pedro\n" \
            "João\n" \
            "Feijão\n" \
            "Gabriel\n" \
            "Andrecio\n" \
            "Hilton\n" \
            "Pinto\n" \
            "Julio\n"

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

time1 = []
time2 = []
time3 = []
time4 = []
time5 = []
time6 = []
time7 = []

for key, value in time.items():
    if 'Time1' == value:
        time1.append(key)
    if 'Time2' == value:
        time2.append(key)
    if 'Time3' == value:
        time3.append(key)
