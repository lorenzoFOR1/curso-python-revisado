#coding: utf-8


def Funcao_Maior(Var):
    if type(Var)==str:
        print(max(Var))

    if isinstance(Var, str):
        print(max(Var))

    if type(Var)==list:
        print(max(Var))
    if type(Var)==dict:
        print("Maior chave: ", max(Var))
        Maior = None
        for valor in Var.values():
            x = valor
            if Maior == None:
                Maior = valor
        else:
            if x>Maior:
                Maior = x
        print("Maior valor: ",Maior)
if __name__=="__main__":
    #Var = "Palavra"
    #Var = [-2,4,3,-1,0,9]
    Var = {"mamão": 12, "pepino":14, "maçã": 18}
    Funcao_Maior(Var)