import math


def seno():
    sen = 0
    sen = int(input("escolha o valor de seno"))
    print(" o valor de seno escolhido em radianos é:" , (math.sin(sen)))
    degreesen = (math.sin(sen)) 
    print("O valor do seno em Graus:" , math.degrees(degreesen))

def cosseno():
    coss = 0
    coss = int(input ("escolha o valor do cosseno"))
    print(" o valor do cosseno escolhido em radianos é:" , (math.cos(coss)))
    degreecos = (math.cos(coss)) 
    print("O valor do cosseno em Graus:" , math.degrees(degreecos))

def tangente():
    tgxx = 0
    tgxx = int(input ("escolha o valor da tangente"))
    print(" o valor da tangente escolhido em radianos é:" , (math.tan(tgxx)))
    degreetgxx = (math.tan(tgxx)) 
    print("O valor da tangente em Graus:" , math.degrees(degreetgxx))

op = 0

print("Bem vindo a calculadora")
print("Escolha a operação que deseja fazer ")
print("[1] seno")
print("[2] cosseno")
print("[3] tangente")
print("[0] Encerrar Operação")
op = int(input("Escolha a operação:" ))
 
if op == 1:{
    seno()
}
if op == 2:{
    cosseno()
}
if op ==3:{
    tangente()
}
else:{
    print("Operação encerrada")
}