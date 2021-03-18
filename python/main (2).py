'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Escreva um programa que ordene uma lista numérica com três elementos. 

n1 = int(input("Digite um número: "))
n2 = int(input("Mais um: "))
n3 = int(input("Mais um, por favor: "))
n4 = int(input("Opa, o último: "))

lista = n1, n2, n3, n4

print("Vamos ordenar esses números...")

print(sorted(lista))
