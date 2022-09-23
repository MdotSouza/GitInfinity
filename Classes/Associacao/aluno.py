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