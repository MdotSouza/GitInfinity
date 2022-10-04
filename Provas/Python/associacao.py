'''Fazendo parte de um time de desenvolvedores, foi atribuído a você o desenvolvimento de um módulo de um sistema de empresas que pagam tributos às prefeituras.
Cada empresa cadastrada com o nome, cnpj, média de funcionários, e média de lucro mensal.
As prefeituras devem ser cadastradas com cidade, prefeito(a) e valor total de impostos.
O(a) prefeito(a) deve ser cadastrado também com nome, cpf e formação.
A prefeitura pode ter várias empresas as quais coleta impostos.
Cada empresa deve fornecer 1.6% de seus lucros mensais para a prefeitura associada e deve ser feito o cálculo a partir desta informação de todas
as empresas de uma prefeitura, quanto pagam mensalmente, pois este será o valor total de impostos.'''

''' IMPLEMENTAÇÃO DA CLASSE EMPRESA '''
class Empresa:
    def __init__(self,nome,cnpj,mediaFunc,mediaLucro):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__mediaFunc = mediaFunc
        self.__mediaLucro = mediaLucro

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome    
    
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self,cnpj):
        self.__cnpj = cnpj
    
    @property
    def mediaFunc(self):
        return self.__mediaFunc
    @mediaFunc.setter
    def mediaFunc(self,mediaFunc):
        self.__mediaFunc = mediaFunc
    
    @property
    def mediaLucro(self):
        return self.__mediaLucro
    @mediaLucro.setter
    def mediaLucro(self,mediaLucro):
        self.__mediaLucro = mediaLucro

''' IMPLEMENTAÇÃO DA CLASSE PREFEITURA '''
class Prefeitura:
    def __init__(self,cidade,prefeito,empresas=[],totalImpostos = 0):
        self.__cidade = cidade
        self.__prefeito = prefeito
        self.__empresas = empresas
        self.__totalImpostos = totalImpostos
    

    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self,cidade):
        self.__cidade = cidade    
    
    @property
    def prefeito(self):
        return self.__prefeito
    @prefeito.setter
    def prefeito(self,prefeito):
        self.__prefeito = prefeito
    
    @property
    def empresas(self):
        return self.__empresas
    @empresas.setter
    def empresas(self,empresas):
        self.__empresas = empresas
    
    @property
    def totalImpostos(self):
        return self.__totalImpostos
    @totalImpostos.setter
    def totalImpostos(self,totalImpostos):
        self.__totalImpostos = totalImpostos

''' IMPLEMENTAÇÃO DA CLASSE PREFEITO '''
class Prefeito:
    def __init__(self,nome,cpf,formacao):
        self.__nome = nome
        self.__cpf = cpf
        self.__formacao = formacao

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome    
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf
    
    @property
    def formacao(self):
        return self.__formacao
    @formacao.setter
    def formacao(self,formacao):
        self.__formacao = formacao

'''TRECHO DO CÓDIGO MAIN'''
print("|---------- Cadastro da Cidade ----------|")
cidade = input("Insira o nome da cidade: ")
nome = input(f"Insira o nome do prefeito de {cidade}: ")
cpf = input(f"Insira o cpf do prefeito de {cidade}: ")
formacao = input(f"Insira o formacao do prefeito de {cidade}: ")

prefeito1 = Prefeito(nome,cpf,formacao)
prefeitura1 = Prefeitura(cidade,prefeito1)

print(f"|---------- Empresas de {cidade} ----------|")
while True:
    empresa = input("Insira o nome da empresa: ")
    cnpj = input(f"Insira o cnpj da empresa {empresa}: ")
    mediaFunc = float(input(f"Insira a média de funcionários da empresa {empresa}: "))
    mediaLucro = float(input(f"Insira a média de lucro da empresa {empresa}: "))

    empresa1 = Empresa(empresa,cnpj,mediaFunc,mediaLucro)

    prefeitura1.empresas.append(empresa1)
    prefeitura1.totalImpostos += (empresa1.mediaLucro)*(1.6/100)

    op = input("Deseja cadastrar nova empresa?(S/N): ").upper()
    if op == "N": break