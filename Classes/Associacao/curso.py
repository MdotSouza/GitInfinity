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
    