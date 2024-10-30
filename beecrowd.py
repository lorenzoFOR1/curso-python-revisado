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

x1 = input().split(' ')
y1 = input().split(' ')
x2 = input().split(' ')
y2 = input().split(' ')
p1 = (x1,y1)
p2 = (x2,y2)
distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("{0:.4f}".format(distancia))