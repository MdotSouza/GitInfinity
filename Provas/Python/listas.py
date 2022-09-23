print('''REGISTROS DE ASTERÓIDES DA NASA (Agência Espacial dos Estados Unidos)''')
dicAsteroides = {}
dicAsteroides2 = {}
while True:
    op = (input('Desejar realizar um cadastro? (S/N): ')).upper()
    listaDistancias = []
    if op == "S":
        asteroide = input("Insira o nome do asteróide: ")
        for i in range(1,6):
            distancia = float(input(f'Iforme a distância {i}/5 do asteróide *{asteroide}* até a Terra (km): '))
            dicAsteroides[asteroide] = listaDistancias.append(distancia)
            dicAsteroides2[asteroide] = sum(listaDistancias)/len(listaDistancias)
    elif op == "N":
        break
    else:
        print("Seleção inválida!")
print('-------------------------------------------------------')
somatorio = 0
for asteroide, mediaDistancias in dicAsteroides2.items():
    print(f'Asteróide: {asteroide} / Distância Média (km): {mediaDistancias:.2f}')
    somatorio += mediaDistancias
mediaGeral = somatorio/len(dicAsteroides2)
print(f'DISTÂNCIA MÉDIA GERAL DE TODOS OS ASTERÓIDES (km): {mediaGeral:.2f}')
print('-------------------------------------------------------')