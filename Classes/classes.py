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
'''