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
    