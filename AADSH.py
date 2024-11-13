#dicionario para: As Aventuras De Sherlock Holmes

def dicionario():
    Dicionario = {}
    SzLimit = 4
    caracteresRemovidos = '",.!?: -;()'
    while True:
        try:
            Linha = input().split()
            if Linha != "":
                for i in range (len(Linha)):
                    Palavra = Linha[i].strip(caracteresRemovidos)
                    if (Palavra)>=4:
                        k = Dicionario.get(Linha[i])
                        if k == None:
                            Dicionario[Linha[i]]=0
                        else:
                            Dicionario[Linha[i]]+=1
        except EOFError as Er:
            break
    for chave, valor in Dicionario.items():
        print(chave, valor)

if __name__=="__main__":
 dicionario()