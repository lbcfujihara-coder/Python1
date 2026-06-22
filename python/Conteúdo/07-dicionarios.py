#Aula 03/06/26

'''
É uma lista que tem relação chave valor, podendo utilizar mais de um tipo de dados, ex: str - int
'''
pessoa= {
    "nome": "Lavínia",
    "idade": 19
}

print(pessoa)

print(pessoa["nome"])

#Alterando valores 
pessoa["idade"] = 20
print(pessoa)

#Adicionando novos dados 

pessoa['cidade'] = 'São Paulo'
print(pessoa)

#Removendo dados
del pessoa['idade']
print(pessoa)

#Aula 08/06/2026

PessoaNova = {
    "primeiro nome": "Vânia",
    "idade": 50
}

#Ver chaves 
print(PessoaNova.keys())

#Ver valores

print(PessoaNova.values())

#Ver chaves e valores

print(PessoaNova.items())

#Verificar se a chave existe

print("nome" in PessoaNova)

print("primeiro nome" in PessoaNova)

#Usar GET

print(PessoaNova.get("primeiro nome"))

#Percorrer 

for chave, valor in PessoaNova.items ():
    print(chave, ":", valor)