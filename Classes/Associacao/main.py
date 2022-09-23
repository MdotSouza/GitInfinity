from escola import Escola
from curso import Curso
from aluno import Aluno
from endereco import Endereco

print("|------------------ Cadastro da Escola ------------------|")
nome = input("Digite o nome da escola: ")
cnpj = input("Digite o CNPJ da escola: ")
escola = Escola(nome,cnpj,[])  #instância do objeto ESCOLA

print("|------------------ Cadastro de Cursos ------------------|")
while True:
    nome = input("Digite o nome do curso: ")
    curso = Curso(nome,[]) #instância do objeto CURSO


    print(f"|-------- Cadastro dos Alunos no Curso {curso.nome} --------|")
    while True:
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        rua = input("Digite o nome da rua: ")
        bairro = input("Digite o nome do bairro: ")
        cidade = input("Digite o nome da cidade: ")

        endereco = Endereco(rua,bairro,cidade) #instância do objeto ENDEREÇO
        aluno = Aluno(nome,matricula,endereco) #instância do objeto ALUNO

        #adição na lista de alunos do objeto ALUNO
        curso.alunos.append(aluno) 

        op = input("Deseja adicionar outro aluno? (S/N): ").upper()
        if op == "N": break

    #adição na lista de cursos do objeto ESCOLA
    escola.cursos.append(curso) 

    op = input("Deseja adicionar outro curso? (S/N): ").upper()
    if op == "N": break

print(f'''|------------------ Resultados ------------------|
Escola: {escola.nome}
''')
for curso in escola.cursos:
    print(f'Curso: {curso.nome}\n')
    print("------- Alunos-------")
    for aluno in curso.alunos:
        print(f'''
Aluno: {aluno.nome}.
Matrícula: {aluno.matricula}
Endereço: {aluno.endereco.rua},{aluno.endereco.bairro}, {aluno.endereco.cidade}
''')