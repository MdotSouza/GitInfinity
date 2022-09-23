'''
class Concessionaria:
    def __init__(self,nome,veiculos=[]):
        self.__nome = nome
        self.__veiculos = veiculos

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome    
    
    @property
    def veiculos(self):
        return self.__veiculos
    @veiculos.setter
    def veiculos(self,veiculos):
        self.__veiculos = veiculos

class Veiculo:
    def __init__(self,preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self,preco):
        self.__preco = preco    

from veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, preco,eixos):
        super().__init__(preco)
        self.__eixos = eixos
    
    @property
    def eixos(self):
        return self.__eixos
    @eixos.setter
    def eixos(self,eixos):
        self.__eixos = eixos

class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome 
        self.__cpf = cpf 
        self.__compras = 0
        self.__total = 0.0
        self.__tipo = "Básico"

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
    def compras(self):
        return self.__compras
    @compras.setter
    def compras(self):
        self.__compras += 1

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self,total):
        self.__total += total

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self):
        if (self.__compras > 10 or self.__total == 10000): 
            self.__tipo = "Premium"

class Aluno:
    def __init__(self,nome,matricula,endereco):
        self.__nome = nome
        self.__matricula = matricula
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula = matricula
    
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self,endereco):
        self.__endereco = endereco

class Curso:
    def __init__(self,nome,alunos):
        self.__nome = nome
        self.__alunos = alunos

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def alunos(self):
        return self.__alunos
    @alunos.setter
    def alunos(self,alunos):
        self.__alunos = alunos
    
class Endereco:
    def __init__(self,rua,bairro,cidade):
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade

    @property
    def rua(self):
        return self.__rua
    @rua.setter
    def rua(self,rua):
        self.__rua = rua

    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self,bairro):
        self.__bairro = bairro
    
    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self,cidade):
        self.__cidade = cidade

class Escola:
    def __init__(self,nome,cnpj,cursos):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__cursos = cursos

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
    def cursos(self):
        return self.__cursos
    @cursos.setter
    def cursos(self,cursos):
        self.__cursos = cursos

from time import sleep
class Pessoa():
    def __init__(self,name,age,height,weight):
        self.nome = name
        self.idade = age
        self.altura = height #unidade: centímetros
        self.peso = weight #unidade: kg

    def engordar(self,novoPeso):
        self.peso += novoPeso
    
    def emagrecer(self,novoPeso):
        if novoPeso >= self.peso: print("Valor de entrada inconsistente!")
        else: self.peso -= novoPeso
    
    def crescer(self,novaAltura):
        if self.idade <= 21:
            self.altura += novaAltura

    def envelhecer(self,anos):
        start = self.idade
        stop = start+anos
        for i in range(start,stop):
            self.idade += 1
            if self.idade <= 21:
                self.crescer(0.5)
                print(f'Idade: {self.idade} anos. Altura {self.altura:.2f} cm. Envelhecendo e crescendo...')
            else: print(f'Idade: {self.idade}. Envelhecendo...')
            sleep(1)

class Carro():
    def __init__(self,modelo,ano,velocidade=0,ligado=False,automatico="MANUAL"):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico
 
    def ligar(self):
        if self.velocidade == 0: 
            print("Partida")
            self.ligado = True
        
    def desligar(self):
        if self.velocidade == 0: 
            print("Parada")
            self.ligado = False
        
    def acelerar(self,incVel):
        if self.velocidade < 120:
            self.velocidade += incVel
            print(f'Acelerando: {self.velocidade} km/h')
        
    def desacelerar(self,incVel):
        if self.velocidade > 0:
            self.velocidade -= incVel
            print(f'Desacelerando: {self.velocidade} km/h')

    def verificarMarcha(self):
        if self.velocidade == 0: print("Neutro")
        elif self.velocidade < 20 : print("Primeira Marcha")
        elif self.velocidade >= 20 and self.velocidade < 30: print("Segunda Marcha")
        elif self.velocidade >= 30 and self.velocidade < 35: print("Terceira Marcha")
        elif self.velocidade >= 35 and self.velocidade < 45: print("Quarta Marcha")
        else: print("Quinta Marcha")

class CarrinhoCompras():
    def __init__(self, isVip = False):
        self.dicItem = {}
        self.vip = isVip
        self.totalCompra = 0.0

    def setItem(self,nome,preco):
        self.dicItem[nome] = preco

    def setVip(self,isVip):
        if isVip == False and  self.vip == False: print("O usuário ")

    def setTotalCompra(self):
        self.totalCompra = sum(self.dicItem.values())

'''