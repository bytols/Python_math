import math

class formula:
    def __init__ (self, number, opname, opformula):
        self.number = number
        self.opname = opname
        self.opformula = opformula

    def calculo(self):
        number = 0
        number = int(input("escolha o valor de " + self.opname + " =" ))
        print("o valor de " , self.opname , " escolhido em radianos é: " , (self.opformula(number)))
        opdegree = (self.opformula(number))
        print("O valor do ", self.opname , "em Graus é: " , math.degrees(opdegree))


        #(math.sin(number))
        #(math.degrees(opdegree)30

op = 0
number = 0

seno = formula ( number , "seno" , math.sin)
cosseno = formula ( number , "cosseno" , math.cos )
tangente = formula ( number , "tangente" , math.tan)

print("Bem vindo a calculadora!")


print("Escolha a operação que deseja fazer ")
print("[1] seno")
print("[2] cosseno")
print("[3] tangente")
print("[0] Encerrar Operação")
op = int(input("Escolha a operação:" ))
 
if op == 1:{
    print(seno.calculo())
}
if op == 2:{
    print(cosseno.calculo())
}
if op ==3:{
    print(tangente.calculo())
}
else:{
    print("Operação encerrada")
}


