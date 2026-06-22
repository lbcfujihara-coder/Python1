#Aula 08/06/26

''' 
Repetir o mesmo processo de acordo com
a quantidade de vezes que for programado ou 
até a sentença se tornar verdadeira.
Uma linha de montagem, robos de limpeza são exemplos de loop

O que são Loops?
Um loop é como uma máquina de repetição. 🤖
Ele repete um bloco de código várias vezes
até que uma condição seja verdadeira ou falsa.
Imagine que você está lavando pratos:
Enquanto houver pratos sujos → você lava.
Cada prato lavando é uma repetição do loop.
'''

#Loop for
print("loop for")
for i in range (1,6):
    print(i)

frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)

input('Digite ENTER para continuar')

from os import system, name
system('cls') if(name =='nt') else system('clear')

'''
🔁 continue → pula a iteração atual e vai para a próxima
⛔ break → interrompe completamente o loop
Se uma peça está em falta ou com defeito, você pula ela e continua o processo. (continue)
Entretanto, se mesmo assim, o problema continua, vc para o processo inteiro. (break)
'''

#Loop for Continue (ignora o 5)
print("loop for continue")
for j in range (1,11):
    if j == 5:
        continue
    print(j)


input('Digite ENTER para continuar')

from os import system, name
system('cls') if(name =='nt') else system('clear')

#Loop for Break (para no 4)
print("loop for break")
for m in range (1,11):
    if m == 5:
        break
    print(m)

input('Digite ENTER para continuar')

from os import system, name
system('cls') if(name =='nt') else system('clear')

# Usando continue ou break juntos
print("loop for continue e break")
for n in range (1,11):
    if n == 5:
        continue #pular o número 5 - falta uma peça, depois vc cria um código para instalar a peças faltantes 
    print(n)
    if n == 8:
        break #para o loop quando chegar no 8 - faltam várias peças 

input('Digite ENTER para continuar')

from os import system, name
system('cls') if(name =='nt') else system('clear')

#Loop while -->enquanto o valor no contador for menor ou igual a 5, imprima contador e 
print("loop for while")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1 #encremento, vai somar 1 no contador 

texto = ""

while texto != "sair":

    texto = input("Digite algo (ou 'sair' para parar)")

''' Não devemos fazer loop infinito
while True:
    print("Esse loop é infinito")
'''


#Enumerate

print("loop for enumerate")
frutas = ["maçã", "banana", "uva"]
for indice, fruta in enumerate (frutas, start=1):
    print(f"{indice}.{fruta}")

input('Digite ENTER para continuar')

from os import system, name
system('cls') if(name =='nt') else system('clear')

