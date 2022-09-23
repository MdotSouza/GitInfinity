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
'''