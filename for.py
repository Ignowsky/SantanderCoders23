
'''
for variavel in range(10):
    print(variavel)
'''


'''
for variavel in range(10):
    print(variavel)
'''

'''
for variavel in range(1, 12, 3):
    print(variavel)

nota1 = float(input("Informe a sua nota 1: "))
nota2 = float(input("Informe a sua nota 2: "))
nota3 = float(input("Informe a sua nota 3: "))
'''

media = 0

for i in range(1, 4):
    nota = float(input(f"Informe sua nota {i}: "))

    media = media + nota

media = media / 3

print(f"Sua media foi {media}")
