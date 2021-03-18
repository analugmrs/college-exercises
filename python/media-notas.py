'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Faça um programa que receba duas notas digitadas pelo usuário.
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 

print("Olá, seja bem-vindo!")

n1 = int(input("Qual foi a nota da sua primeira prova? "))

print("Hmmm, certo...")

n2 = int(input("E qual foi a nota da sua segunda prova? "))

print("Certo... Só um instante...")

nFinal = (n1+n2)/2

if nFinal >= 6:
    print("Parabéns, você foi aprovado e já pode curtir suas férias! ;D ")
else:
    print("Xiii... você foi reprovado. Continue tentanto, tenho certeza que da próxima vai!! ")

