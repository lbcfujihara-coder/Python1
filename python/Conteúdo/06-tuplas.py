# Aulas 03/06/26

''' Tuplas não podem ser modificadas, sendo impossível, 
adicionar ou remover algo  que já foi registrado nela,
ela é muito usada nos semáforos,
no qual é determinado um tempo x para que print uma cor,
por exemplo: o sinal verde vai printar durante 3 minutos, 
depois a amamrela, printa 1 minuto 
e o vermelho printa seis minutos
'''
cores=('vermelho', 'azul',' verde')
print(cores)
print(cores[1])

#contar elementos

'''
Faz a contagem da repetição de elementos (.count), nesse caso o número que ele quer achar, seria o dois
'''
valores = (1,2,2,3)
print(valores.count(1))
print(valores.count(2))
print(valores.count(3))


#Encontrar posição

print(valores.index(1))
print(valores.index(2))

'''
Encontra a posição (index) de um determinado número,
no caso de numeros repetidos, ele acha somente a primeira posição
'''

#percorrer

for v in valores:
    print(v)
