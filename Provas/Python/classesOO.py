class Computador():
    def __init__(self, modelo : str, fabricante : str, processador : str, memoria : str, hd : float, espaco : float, ligado : bool):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.memoria = memoria
        self.hd = hd
        self.espaco = espaco
        self.ligado = ligado
    
    def liga(self):
        #verifica status antes de realizar a operação
        if self.ligado == True: print('O computador já está ligado')
        else: self.ligado = True
    
    def desliga(self):
        #verifica status antes de realizar a operação
        if self.ligado == False: print('O computador já está desligado')
        else: self.ligado = False
    
    def limparHD(self,espacoLib : float):
        #verificações iniciais
        if espacoLib < 0:print('Entrada inválida!')
        elif self.espaco == 0: print('O HD já está vazio!')
        else:
            #vericação de segurança
            if (self.espaco-espacoLib <= 0):
                while True:
                    op = input('ATENÇÃO: A operação irá limpar completamente o HD!\nDeseja continuar?(S/N): ').upper()
                    if op == "S":
                        self.espaco = 0
                        break
                    elif op == "N":
                        print('Operação cancelada!')
                        break
                    else:
                        print('Seleção incorreta!')
            else:
                self.espaco -= espacoLib
            
    def ocupadrHD(self,espacoOcp : float):
        #verificações iniciais
        if espacoOcp < 0: print('Entrada inválida!')
        elif self.espaco == self.hd: print('O HD já está cheio!')
        else:
            #vericação de segurança
            if self.espaco+espacoOcp >= self.hd:
                while True:
                    op = input('ATENÇÃO: A operação irá ocupar completamente o HD!\n Deseja continuar?(S/N): ').upper()
                    if op == "S":
                        self.espaco = self.hd
                        break
                    elif op == "N":
                        print('Operação cancelada!')
                        break
                    else:
                        print('Seleção incorreta!')
            else:
                self.espaco += espacoOcp

