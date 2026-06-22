#Aula 3 - 01/06/26

numero = int(input('Informe o número:'))

resultado = int(numero % 2)

print('se o resultado for 0 é par e se for 1 é impar, o resultado é:', resultado)
input('Digite ENTER para continuar')

# IF é usado para uma tomada de decisão

if resultado == 0:
    resultado = 'O número é par'
else:
    resultado = 'O número é impar'

print(resultado)

input('Digite ENTER para continuar')

from os import system, name
system('cls') if(name =='nt') else system('clear')

#Entrada de nota

nota= float(input("Digite a nota de um estudante:"))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

