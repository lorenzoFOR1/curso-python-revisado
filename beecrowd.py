#coding: utf-8

#Problema 1000
'''
print("Hello World!")
'''

#Problema 1001
'''
import math as mt

A = int(input())
B = int(input())
X = A + B
print("X =", X)
'''

#Problema 1002
'''
import math as mt

R = float(input())
π = 3.14159
A = π*(R*R)
print(f"A={A:.4f}")
'''

#Problema 1003
'''
import math as mt

A = int(float(input()))
B = int(float(input()))
SOMA = A+B
print(f"SOMA =", SOMA)
'''

#Problema 1004
'''
import math as mt

A = int(input())
B = int(input())
PROD = A*B
print(f"PROD =", PROD)
'''

#Problema 1005
'''
A = float(input())
B = float(input())

media = (3.5 * A + 7.5 * B)/11

print(f"MEDIA = {media:.5f}")
'''

#Problema 1006
'''
import math as mt

notaa = float(input())
notab = float(input())
notac = float(input())
peso1 = 2
peso2 = 3
peso3 = 5
media_ponderada = (notaa*2+notab*3+notac*5)/(2+3+5)
saida = "MEDIA = {0:.1f}".format(media_ponderada)
print(saida)
'''

#Problema 1007
'''
A = int(input())
B = int(input())
C = int(input())
D = int(input())
diff = A * B - C * D
print(f"DIFERENCA =", diff)
'''

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

#Problema 1012
'''
import math as mt

valor = input().split()
A = float(valor[0])
B = float(valor[1])
C = float(valor[2])
pi = 3.14159
ARTRI = A*C/2
ARCI = pi*(C*C)
ARTRA = (A + B)*C / 2
ARQUA = B*B
ARRECT = A*B

print("TRIANGULO: {0:.3f}".format(ARTRI)) 
print("CIRCULO: {0:.3f}".format(ARCI))
print("TRAPEZIO: {0:.3f}".format(ARTRA))
print("QUADRADO: {0:.3f}".format(ARQUA))
print("RETANGULO: {0:.3f}".format(ARRECT))
'''

#Problema 1013
#colei de https://xtecna.gitbook.io/solucoes-da-beecrowd/iniciante/1013-o-maior 
'''
maior = lambda a, b: (a + b + abs(a - b))//2
a, b, c = [int(x) for x in input().split(' ')]
resposta = maior(a, maior(b, c))
print(f"{resposta} eh o maior")
'''

#Problema 1014
'''
X = int(input())
Y = float(input())
consumo = X/Y
print("{0:.3f}".format(consumo),"km/l")
'''

#Problema 1015
'''
x1, y1 = list(map(float, input().split(' ')))
x2, y2 = list(map(float, input().split(' ')))
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f'{distancia:0.4f}')
'''

#Problema 1016
'''
distancia = int(input())
tempo = distancia*2
print(tempo, "minutos")
'''

#Problema 1017
'''
tempo = int(input())
vel = int(input())
gasto = tempo*vel/12
print("{0:.3f}".format(gasto))
'''

#Problema 1018
'''
N = int(input())

print(N)

print(f"{N//100} nota(s) de R$ 100,00")
N %= 100
print(f"{N//50} nota(s) de R$ 50,00")
N %= 50
print(f"{N//20} nota(s) de R$ 20,00")
N %= 20
print(f"{N//10} nota(s) de R$ 10,00")
N %= 10
print(f"{N//5} nota(s) de R$ 5,00")
N %= 5
print(f"{N//2} nota(s) de R$ 2,00")
N %= 2
print(f"{N} nota(s) de R$ 1,00")
'''

#Problema 1019
'''
seg = int(input())
horas = seg//3600
seg %= 3600
minutos = seg//60
seg %= 60
print(f"{horas}:{minutos}:{seg}")
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











#Problema 1180
'''
N = int(input())

valores = list(map(int, input().split())) 

menorValor = min(valores)
menorPosicao = 0

for i in range(N): 
    if valores[i] == menorValor:
        menorPosicao = i

print(f"Menor valor: {menorValor}")
print(f"Posicao: {menorPosicao}")
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