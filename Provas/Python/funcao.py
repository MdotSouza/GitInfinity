def encontraSeculo(ano):
    resposta = ""
    seculoArabico = 0 
    #ENCONTRA SÉCULO EM ALGORISMOS ARÁBICOS
    if ano < 0:
        resposta = "Entrada Inválida"
    elif ano%100 == 0:
        seculoArabico = ano//100
    else:
        seculoArabico = (ano//100)+1

    #CONVERTE SÉCULO EM ALGORISMOS ROMANOS
    seculoRomano = seculoArabico
    dicRomanos= {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
    for numero, simbolo in dicRomanos.items():
        while (seculoRomano/numero) >= 1:
            resposta += simbolo
            seculoRomano -= numero
    
    return resposta

ano = int(input("Informe o ano: "))
seculo = encontraSeculo(ano)
print(seculo)