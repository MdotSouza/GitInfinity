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