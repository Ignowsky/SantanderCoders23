# > ESTRUTURAS CONDICIONAIS

'''
idade = int(input("Qual a sua idade? "))


if idade >= 18:
    print("Você é maior de idade.")

else:
    print("Você é menor de idade.")
'''


'''
Imagine que você queira imprimir "Aprovada(o)", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7   
'''

'''
nota1 = float(input("Qual foi a sua primeira nota? "))
nota2 = float(input("Qual foi a sua segunda nota? "))
nota3 = float(input("Qual foi a sua terceira nota? "))

media = (nota1+nota2+nota3) / 3

if media >= 7:
    print("Sua média foi", media, "e você foi APROVADO.")

elif media >= 5.5:
    print("Sua média foi", media, "mas você pode fazer a RECUPERAÇÃO.")

else:
    print("Sua média foi", media, "e você foi REPROVADO.")
'''

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print("APROVADO(a)")

else:
    print("REPROVADO(a)") 