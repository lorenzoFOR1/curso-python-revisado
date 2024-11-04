#coding utf-8

#Problema 1008

'''
NUMBER = int(input())
horastrabalhadas = int(input())
salariohora = float(input())
"{0:.2f}".format(salariohora)
salariototal = (horastrabalhadas*salariohora)
print("NUMBER =",NUMBER)
print("SALARY = U$ {0:.2f}".format(salariototal))
'''

#Problema 1009

'''
Nome = input()
salario = float(input())
vendas = float(input())
totalareceber = (salario + vendas*0.15)
print("TOTAL = R$ {0:.2f}".format(totalareceber))
'''

#Problema 1010

'''
valores = input().split(' ')
peca1 = int(valores[0])
quantidade1 = int(valores[1])
valor1 = float(valores[2])

valores = input().split(' ')
peca2 = int(valores[0])
quantidade2 = int(valores[1])
valor2 = float(valores[2])

total = (quantidade1*valor1 + quantidade2*valor2)
print("VALOR A PAGAR: R$ {0:.2f}".format(total))
'''

#Problema 1011

'''
pi = 3.14159
raio = float(input())
volume = (4/3) * pi * raio**3
print("VOLUME = {0:.3f}".format(volume))
'''

#Problema 1013
#colei de https://xtecna.gitbook.io/solucoes-da-beecrowd/iniciante/1013-o-maior

'''
maior = lambda a, b: (a + b + abs(a - b))//2
a, b, c = [int(x) for x in input().split(' ')]
resposta = maior(a, maior(b, c))
print(f"{resposta} eh o maior")
'''

#Problema 1015

'''
x1, y1 = list(map(float, input().split(' ')))
x2, y2 = list(map(float, input().split(' ')))
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f'{distancia:0.4f}')
'''

#Problema 1021

'''
reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

print('NOTAS:')
print(f'{centavos//10000}','nota(s) de R$ 100.00')
centavos %= 10000

print(f'{centavos//5000}','nota(s) de R$ 50.00')
centavos %= 5000

print(f'{centavos//2000}','nota(s) de R$ 20.00')
centavos %= 2000

print(f'{centavos//1000}','nota(s) de R$ 10.00')
centavos %= 1000

print(f'{centavos//500}','nota(s) de R$ 5.00')
centavos %= 500

print(f'{centavos//200}','nota(s) de R$ 2.00')
centavos %= 200

print('MOEDAS:')
print(f'{centavos//100}','moeda(s) de R$ 1.00')
centavos %= 100

print(f'{centavos//50}','moeda(s) de R$ 0.50')
centavos %= 50

print(f'{centavos//25}','moeda(s) de R$ 0.25')
centavos %= 25

print(f'{centavos//10}','moeda(s) de R$ 0.10')
centavos %= 10

print(f'{centavos//5}','moeda(s) de R$ 0.05')
centavos %= 5

print(f'{centavos//1}','moeda(s) de R$ 0.01')
centavos %= 1
'''

#Problema 2540

'''
def Beecrowd2540():
    while True: 
        try:
            n = int(input())
        except EOFError as err:
            break
        aprovacao = (2/3)*n
        votos = map(int, input().split(' '))
        soma = 0
        for voto in votos:
            soma>= voto
        #print(soma)
        if (soma>=aprovacao):
            print("impeachment")
        else:
            print("acusacao arquivada")
if __name__=="__main__":
    Beecrowd2540()
'''      

