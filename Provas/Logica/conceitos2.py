#QUESTÃO 1
'''Crie um algoritmo que recebe como entrada o dia e o mês de nascimento e retorna o signo.'''
dia = int(input("Digite o dia de nascimento (valores entre 1 e 31): "))
mes = input("Digite o mês de nascimento (exemplo: janeiro): ").lower()
if (dia>=21 and dia<=31 and mes=="março") or (dia>=1 and dia<=20 and mes=="abril"): print("Áries")
elif (dia>=21 and dia<=30 and mes=="abril") or (dia>=1 and dia<=20 and mes=="maio"): print("Touro")
elif (dia>=21 and dia<=31 and mes=="maio") or (dia>=1 and dia<=20 and mes=="junho"): print("Gêmeos")
elif (dia>=21 and dia<=30 and mes=="junho") or (dia>=1 and dia<=22 and mes=="julho"): print("Câncer")
elif (dia>=23 and dia<=31 and mes=="julho") or (dia>=1 and dia<=22 and mes=="agosto"): print("Leão")
elif (dia>=23 and dia<=31 and mes=="agosto") or (dia>=1 and dia<=22 and mes=="setembro"): print("Virgem")
elif (dia>=23 and dia<=30 and mes=="setembro") or (dia>=1 and dia<=22 and mes=="outubro"): print("Libra")
elif (dia>=23 and dia <=31 and mes=="outubro") or (dia>=1 and dia<=21 and mes=="novembro"): print("Escorpião")
elif (dia>=22 and dia<=30 and mes=="novembro") or (dia>=1 and dia<=21 and mes=="dezembro"): print("Sagitário")
elif (dia>=22 and dia<=31 and mes=="dezembro") or (dia>=1 and dia<=20 and mes=="janeiro"): print("Capricórnio")
elif (dia>=21 and dia<=31 and mes=="janeiro") or (dia>=1 and dia<=18 and mes=="fevereiro"): print("Aquário")
elif (dia>=19 and dia<=29 and mes=="fevereiro") or (dia>=1 and dia<=20 and mes=="março"): print("Peixes")
else: print("Informação de dia ou mês inválida!")

#QUESTÃO 2
'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
Considerar ano com 365 dias e mês com 30 dias'''
anos = int(input("Informe quantos anos: "))
meses = int(input("Informe quantos meses: "))
dias = int(input("Informe quantos dias: "))
idadeDias = (anos*365) + (meses*30) + dias
print(idadeDias)

#QUESTÃO 3
'''Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo.'''
base = float(input("Informe a dimensão da base: "))
altura = float(input("Informe a dimensão da altura: "))
area = base * altura
print(f'{area:.2f}')

#QUESTÃO 4
n = int(input("Digite um número (entre 1 e 100): "))
if (n < 1 or n > 100):
    print("Entrada inválida!")
else:
    if n == 1:
        print(f'O número {n} não é primo.')
    elif (n == 2) or (n == 3) or (n == 5) or (n == 7):
        print(f'O número {n} é primo.')
    elif (n%2 == 0) or (n%3 == 0) or (n%5 == 0) or (n%7 == 0):
        print(f'O número {n} não é primo.')
    else:
        print(f'O número {n} é primo.')
