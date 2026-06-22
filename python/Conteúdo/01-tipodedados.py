#comentário em uma linha - Aula 01 
'''comentários auxiliam a deixar "anotações" no código fonte'''

#Concatenação
print('boas vindas a aula de'+' Python')

#interpolação
print('Olá {}'.format(input('Qual é seu nome?'))) 

#Aula 02 // 27/05/26

#Tipo de dados em python - Números (Int, Float, Complex)
#Inteiro
idade1 = 30
idade2 = 19

print(idade2)

#Decimal (float)
altura=1.75
print(altura)

#Complexos 
numero_complexo = 2+3j
print(numero_complexo)

#String (str) - Texto

nome = "Lavínia" 
print(nome)

#booleano (bool)
ativo=True
print(ativo)

logado=False
print(logado)

#nenhum valor (NoneType)
valor = None
print(valor)

#Lista (list) mutável
frutas = ["maçã", "banana", "uva"]
print(frutas)

#Tuplas (tuple) imutável
cores=("vermelho", "amarelo", "azul", "verde")
print(cores)

#conjunto (set)
numeros={1,2,3,4}
print(numeros)
 
 #dicionário (dict) - Pares chave valor 
pessoa={
    "nome": "Lavínia",
    "idade": 19
    }
print(pessoa)

'''Python não têm constantes verdadeiras, 
mas usamos uma convenção
 para indicar que o valor não deve ser alterado'''

PI = 3.14159
GRAVIDADE = 9.8

print("O valor de PI é", PI, "\nO valor de Gravidade é", GRAVIDADE)
print("O valor de PI é", PI)
print("O valor de Gravidade é", 9.8)

# Aula 3 - 01/06/26

