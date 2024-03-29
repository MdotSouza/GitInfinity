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