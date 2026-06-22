#Aula 03/06/2026 

'''As listas permitem armazenar e modificar dados que tem o mesmo tipo,
elas permitem adicionar e remover elementos.
Cada elemento têm uma posição, a qual é chamada de index e 
sua contagem inicia-se em 0, ou seja maçã é 0, banana é 1, Uva é 2'''

frutas=["maçã", "banana", "uva"]
print(frutas)
print()
#ver primeiro elemento da lista

print(frutas[0])
print()
#ver demais elementos da lista

print(frutas[1])
print()
print(frutas[2])
print()

#O comando print() permite pular uma linha no terminal 

# modificando // O frutas é o nome da lista; [1] é a posição = 'laranja' é o que vai substituir 

frutas[1] = 'laranja'
print(frutas)
print()

# adicionando itens // append significa que vai adicionar no final da lista pera // append = acrescentar

frutas.append('pera')
print(frutas)
print()
#adicionar no começo da lista // quando se usa insert, deve-se colocar a posição, nesse caso, 0, que vai fazer, todas as outras andarem para tras

frutas.insert(0, 'abacaxi')
print(frutas)
print()

#removendo itens // remove um valor da lista 
frutas.remove('uva')
print(frutas)
print()

#tamanho da lista
numeros = [1,2,4,3]
print(len(numeros))
print()

#ordenar
    #Em ordem crescente 

numeros.sort() 
print(numeros)
print()

    #Em ordem crescente 
numeros.reverse()
print(numeros)
print()

#verificar se existe 

print(2 in numeros)

# Para adicionar vários elementos ao mesmo tempo 
#  vc coloca o mesmo nome da lista, adiciona o que vc quer,
#  como se estivesse criando uma nova lista e repete o nome 

numeros = [10,20,30] + numeros 
print(numeros)


#percorrer com for // 
'''     
Serve para mostrar todos os itens de uma lista,
 um por vez, na ordem em que foi feita a ultima alterração
'''


for n in numeros:
    print(n)

for b in frutas:
    print(b)