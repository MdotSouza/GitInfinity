#QUESTÃO 1
'''Dada uma lista de pessoas que moram em uma cidade, definir a quantidade de homens e mulheres.   '''
N = int(input("Informe o número de pessoas que moram na cidade: "))
homem = mulher = 0
for i in range(N):
    while True:
        S = int(input("Informe o sexo (1=homem,2=mulher) "))
        if S == 1:
            homem += 1
            break
        elif S == 2:
            mulher += 1
            break
        else: print('Seleção inválida!')
print(f'Homens: {homem}')
print(f'Mulheres: {mulher}')

#QUESTÃO 2
'''Faça um programa que receba a idade de 15 pessoas, que calcule e mostre:
a) A quantidade de pessoas em cada faixa etária;
b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas: 
    Até 15 anos
    De 16 a 30 anos
    De 31 a 45 anos
    De 46 a 60 anos
    Acima de 61 anos'''
N = 15
faixa0_15 = faixa16_30 = faixa31_45 = faixa46_60 = faixa61 = 0
for i in range(N):
    while True:
        idade = int(input("Informe a idade da pessoa: "))
        if idade >= 0 and idade <= 15:
            faixa0_15 += 1
            break
        elif idade >= 16 and idade <=30:
            faixa16_30 += 1
            break
        elif idade >= 31 and idade <=45:
            faixa31_45 += 1
            break
        elif idade >= 46 and idade <=60:
            faixa46_60 += 1
            break
        elif idade >= 61:
            faixa61 += 1
            break
        else:
             print('Valor inválido!')
print(f'''Até 15 anos: {faixa0_15}
De 16 a 30 anos: {faixa16_30}
De 31 a 45 anos: {faixa31_45}
De 46 a 60 anos: {faixa46_60}
Acima de 61 anos: {faixa61}
Porcentagem da faixa até 15 anos, em relação ao total: {(faixa0_15/15)*100:.2f}%
Porcentagem da faixa acima de 61 anos, em relação ao total: {(faixa61/15)*100:.2f}%''')

#QUESTÃO 3
'''Faça um código de um sistema avaliativo, de uma determinada disciplina, obedecer aos seguintes critérios: 
    Durante o semestre são dadas três notas;
    A nota final é obtida pela média aritmética das três notas;
    É considerado aprovado, o aluno que obtiver a nota final superior ou igual a 6, e que tiver comparecido a um mínimo de 40 aulas.'''
somatorio = 0
for i in range(1,4):
    nota = float(input(f"Insira a {i}ª nota do aluno: "))
    somatorio += nota
aulas = int(input("Informe a quantidade de aulas que o aluno assistiu: "))
media = somatorio/3
if media >= 6 and aulas >= 40:
    print(f'Aluno aprovado. Média: {media:.2f}')
else:
    print(f'Aluno reprovado. Média: {media:.2f}')

#QUESTÃO 4
'''Faça um programa que desenvolva uma tabela de descontos utilizando o formato abaixo, você deve atribuir o valor de compra de cada cliente.'''
compra = float(input("Informe o valor da compra: R$"))
i = 0
if compra >= 3000:
    i = 25
elif compra < 500:
    i = 1
else:
    while i < 26:
        if (compra//100) - 4 == i:
            porcentagem = i
            break
        i += 1
valornovo = compra*(1-(i/100))
print(f'{compra:.2f} ( Valor da compra ) - {i}% ( Porcentagem ) = {valornovo:.2f} ( Valor final )')

#QUESTÃO 5
'''crie um programa que receba um número inteiro e calcule seu fatorial.'''
n = int(input("Insira um número: "))
fatorial = 1
retorno = ""
for i in range (n,0,-1):
    fatorial *= i
    if i != 1:
        retorno += f'{i} . '
    else:
        retorno += f'{i} ='
print(f'{n}! = {retorno} {fatorial}')