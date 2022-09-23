#QUESTÃO 1
'''Faça um programa que receba 2 (Dois) números inteiros e positivos e imprima na tela todos os números primos que existem entre eles.'''
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
if n1 > n2:
 n1, n2 = n2, n1
if n1 == 1: start = 2
else: start = n1
stop = n2 + 1
primo = True
for j in range(start,stop):
    i = 2
    while i < j:
        if j%i == 0:
            primo = False
            break
        else:
            primo = True
        i += 1
    if primo == True: print(j,end=" ")

#QUESTÃO 2
'''O programa deve receber a quantidade de vazamentos notificados a prefeitura no dia e para cada um deles deve pedir a quantidade de água perdida por hora
e a quantidade de horas que o vazamento ficou aberto e ao final da execução exibir o total de água desperdiçada '''
vazamentos = int(input("Informe a quantidade de vazamentos notificados: "))
somatorio = 0
stop = vazamentos +1
for i in range(1,stop):
    vazao = int(input(f"Vazamento {i} - Informe a quantidade de água perdida por hora: "))
    tempo = int(input(f"Vazamento {i} - Informe a quantidade de horas que o vazamento ficou aberto: "))
    somatorio += vazao*tempo
print(f'{somatorio} litros')

#QUESTÃO 3
'''O programa deve receber um número indefinido de direções que o carro está seguindo, e a cada uma delas atribui-se o valor percorrido de 100.
Quando for digitado "parar", o programa deve exibir distância percorrida em Km.'''
distancia = 0.0
while (True):
    op = int(input("Informe a direção (1=siga em frente/2=vire a esquerda/3=vire a direita/4=pare): "))
    if op == 4: break
    elif op >= 1 and op <= 3: distancia += 0.1
    else: print('Seleção inválida!')
print(f'Distância percorrida = {distancia} km')

