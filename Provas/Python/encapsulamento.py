'''
Você foi convidado a desenvolver um sistema para registro de um estacionamento, onde mantém informações sobre os veículos que entram e saem do local.
Os veículos são cadastrados com tipo do veículo (carro, moto, caminhão, etc.), placa, modelo, data e horário de entrada e data e horário de saída, com um valor total a pagar.
O sistema deve receber como input o valor da hora e só deve atribuir o total a pagar no momento que receber a informação do horário de saída, 
que não é obrigatório inserir na hora do registro do veículo. 
Para isso, deve-se encapsular todos os atributos e ter mapeado a regra que a saída do veículo não poderá ser mais antiga que a entrada dele no estacionamento
'''
from os import system
system('cls')
from datetime import datetime
class Veiculo:
    def __init__(self,tipo,placa,modelo,dtEntrada):
        self.__tipo = tipo
        self.__placa = placa
        self.__modelo = modelo
        self.__dtEntrada = datetime.strptime(dtEntrada, "%H:%M %d/%m/%Y")
        self.__dtSaida = ''
        self.__valorTotal = 0.0

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo

    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self,placa):
        self.__placa = placa

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo

    @property
    def dtEntrada(self):
        return self.__dtEntrada
    @dtEntrada.setter
    def dtEntrada(self,dtEntrada):
        self.__dtEntrada = dtEntrada

    @property
    def dtSaida(self):
        return self.__dtSaida
    @dtSaida.setter
    def dtSaida(self,dtSaida):
        dtSaida = datetime.strptime(dtSaida, "%H:%M %d/%m/%Y")
        if (self.__dtEntrada < dtSaida):
            self.__dtSaida = dtSaida
        else:
            print("A data de saída não pode ser menor que a de entrada.")

    @property
    def valorTotal(self):
        return self.__valorTotal
    @valorTotal.setter
    def valorTotal(self,valorHora):
        dias = (self.__dtSaida - self.__dtEntrada).days
        segundos = (self.__dtSaida - self.__dtEntrada).seconds
        horas = (dias*24)+(segundos/3600)
        print(dias,segundos,horas)
        self.__valorTotal = valorHora * horas


'''TRECHO PARA TESTE DA CLASSE'''
tipo = "Carro"
placa = "XXXXX"
modelo = "HB20"
dtEntrada = input("Informe a hora e data de entrada (formato hh:min dd/mm/aaaa):\n")

veiculo1 = Veiculo(tipo,placa,modelo,dtEntrada)

op = input("Deseja realizar a saída do veículo(S/N):\n").upper()
if op == "S":
    veiculo1.dtSaida =  input("Informe a hora e data de entrada (formato hh:min dd/mm/aaaa):\n")
    veiculo1.valorTotal  = float(input("Informe o valor cobrado por hora:\n"))

print(veiculo1.valorTotal)