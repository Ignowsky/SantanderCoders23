# > DICIONARIOS

# Criando Dicionarios

dicionario = {}
dicionario = dict()

dicionario = {"nome": "João", "idade": 23, "altura": 1.78}

print(dicionario)
print(dicionario["idade"])


# Adicionando elementos a um dicionario

dicionario["programador"] = True
print(dicionario)

dicionario["altura"] = 2
print(dicionario)

# Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existencia de uma chave

print("altura" in dicionario)
