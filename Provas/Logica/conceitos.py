#QUESTÃO 1 
'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela.'''
nome = input("Digite seu nome: ")
print(f'Olá {nome}, seja muito bem-vindo!')

#QUESTÃO 2
'''Faça um programa que leia um número de ponto flutuante (Número Real) e mostre na tela o seu dobro e a sua terça parte.'''
num = float(input("Digite um número: "))
dobro = 2*num
tercaParte = num/3
print(f'Dobro: {dobro:.1f}')
print(f'Terça Parte : {tercaParte:.2f}')

#QUESTÃO 3
'''Crie um programa que calcule sua velocidade dado o espaço e o tempo.'''
espaco = int(input('Digite o valor do espaço: '))
tempo = int(input('Digite o valor do tempo: '))
velocidade = espaco/tempo
print(f'Velocidade: {velocidade}')

#QUESTÃO 4 
'''O salário líquido corresponde ao salário bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
a. Desconto do IR;
b. Salário Bruto ate R$900,00 (inclusive) – Isento;
c. Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
d. Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
e. Salário bruto acima de 2500 – Desconto de 20%.
Imprima na tela as informações.'''
valor = float(input("Insira o valor da hora de trabalho: R$"))
horas = float(input("Insira a quantidade de horas trabalhadas no mês: "))
salario = valor * horas
if salario > 2500.0:
    ir = salario * 0.20
    percentual = "(20%)"
elif salario <= 2500.0 and salario > 1500:
    ir = salario * 0.10
    percentual = "(10%)"
elif salario <= 1500.0 and salario > 900:
    ir = salario * 0.05
    percentual = "(5%)"
else:
    ir = 0.0
    percentual = "(Isento)"
inss = salario * 0.10
fgts = salario * 0.11
sindicato = salario * 0.03
descontos = ir+inss+sindicato
salario_liq = salario - descontos
print(f'Salário bruto ({horas} * R${valor}): R${salario:.2f}')
print('IR ' + percentual + f': R${ir:.2f}')
print(f'INSS (10%): R${inss:.2f}')
print(f'Sindicato (3%): R${sindicato:.2f}')
print(f'FGTS (11%): R${fgts:.2f}')
print(f'Total de descontos: R${descontos:.2f}')
print(f'Salário líquido é: R${salario_liq:.2f}')

#QUESTÃO 5
'''Faça um programa que recebe o salário de um colaborador,
e calcule o reajuste segundo os critérios abaixo, que deverá exibis o novo salário, baseado no salário atual. 
Salários até R$ 280,00 (incluindo): aumento de 20%,
Salários entre R$ 280,00 e R$700,00: aumento de 15%;
Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
Salários de R$ 1500,00 em diante: aumento de 5%'''
salario = float(input("Insira o valor do salário: "))
if salario > 1500.0:
    salarioReajustado = salario*1.05
    percentual = "5%"
elif salario <= 1500.0 and salario > 700.0:
    salarioReajustado = salario*1.10
    percentual = "10%"
elif salario <= 700.0 and salario > 280.0:
    salarioReajustado = salario*1.15
    percentual = "15%"
else:
    salarioReajustado = salario*1.20
    percentual = "20%"
print(f'Salário após aumento: R$ {salarioReajustado:.2f}')