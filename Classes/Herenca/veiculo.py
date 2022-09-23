class Veiculo:
    def __init__(self,preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self,preco):
        self.__preco = preco    
    