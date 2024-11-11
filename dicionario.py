#coding: utf-8

def dici():
    pessoa = dict(nome="batman", idade = 30, altura = 1.9)
    print("Retornando Dados Em Tupla :)")
    for elemento in pessoa.items():
        print(elemento)
    print("Retornando Dados Em Variaveis :)")
    for chave, valor in pessoa.items():
        print("Chave: ", chave, "Valor: ", valor)




if __name__=="__main__":
    dici()