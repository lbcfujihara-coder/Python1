
#Base
num1=input('informe o primeiro número:')
num2=input('informe o segundo número:')

#soma
soma= int(num1) + int(num2)
print(soma)

#Subtração
subtração= int(num1) - int(num2)
print(subtração)

#Divisão
divisão= int(num1) / int(num2)
moduloresto= int(num1) % int(num2)
print(divisão)
print(moduloresto)

#Mutiplicação
mutiplicação= int(num1) * int(num2)
print(mutiplicação)

#Potenciação
potenciação= int(num1) ** int(num2)
print(potenciação)

# O comando type retorna o tipo da variável
print(type(num1))
print(type(soma))

#Calculr área 

lado1 = input('informe o primeiro lado:')
lado2 = input('informe o segundo lado:')

#O método isnumeric valida se uma variável é um número inteiro 

print('lado1 é numerico?', lado1.isnumeric())
print('lado2 é numerico?', lado2.isdecimal())

area= float(lado1) * float(lado2)

print('A área do quadrado é: {}' .format(area))

#Aula3 01/06/26

# função len retorna a quantidade de caracteres de uma variável

nomecompleto = input ('informe seu nome completo: ')
print('1. Quantidade de caracteres:', len(nomecompleto))

#Metodods utilizados:
#Upper: transforma um texto em letras maiusculas 
#Lower: transforma um texto em minusculo
#Capitaliza: Somente a primeira letra em maiuscula

print('2. Nome em maiusculo:', nomecompleto.upper())
print('3. Nome em minusculo:', nomecompleto.lower())
print('4. Primeira letra em maiusculo:', nomecompleto.capitalize())

nome= input ('insira seu nome:')
sobrenome= input ('insira seu sobrenome:')
print('5. Primeira letra maiuscula:', nome.capitalize(), sobrenome.capitalize())
