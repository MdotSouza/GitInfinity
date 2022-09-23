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