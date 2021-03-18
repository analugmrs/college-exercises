'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.  

print("Olá, vamos calcular?")
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
op = input("Escolha um operador (+, -, /, *): ")

if op == "+":
    calc = n1 + n2

elif op == "-":
    calc = n1 - n2
    
elif op == "/":
    calc = n1 / n2

elif op == "*":
    calc = n1 * n2

else:
    print ("Operação inválida")
    
print("Seu resultado é: ", calc)
