#Exercício 10:
#Os salários-base dos funcionários de determinada empresa
#estão tabelados segundo a a categoria profissional:

#Categoria       Salário-Base
#   A               2500
#   B               2000
#   C               1750
#   D               1250
#  Outra             750

#Elabore um programa que, a partir da leitura da categoria
#profissional, imprima o respetivo salário-base.

categoria = str(input("Insira a Categoria Profissional")).upper()

if categoria == "A":
    print("O salário é 2500")

elif  categoria == "B":
    print("O salário é 2000")

elif categoria == "C":
    print("O salário é 1750")

elif categoria == "D":
    print("O salário é 1250")

else:
    print("O salário é 750")

