#Aula 08/06/26

'''
Imagine que você tem um robô chamado Funcy. 
Sempre que você quer que ele faça alguma coisa, você dá uma receita pra ele: 
entradas → ele faz a mágica → devolve a saída.
Em programação, essa “receita” é a função.
Entrada (parâmetros): o que você dá para a função. Ex: um número, um texto…
Processo (corpo da função): o que a função faz com a entrada. Ex: soma, multiplica, imprime na tela…
Saída (return): o que a função devolve. Ex: o resultado da soma.
💡 Analogia divertida:
Se você quer um suco de laranja, a função é o espremedor de frutas.
 Você coloca laranja (entrada), ele mistura (processo) e sai suco (saída). Fácil, né?
 Se vc reutiliza várias vezes o mesmo código, ele se torna uma função
'''

#Função (def - definir função, essa funçaõ é do tipo vazia, ela não recebe nada, só mostra o que está programado)
#Ela sozinha não faz nada, então deve ser 'invocada'
def saudacao():
    print("Olá, tudo bem?")

#Acessando a função // Como se tivesse apertado um botão, onde ele vai na função e busca a resposta
saudacao()

#Função com parametro
def saudacao(nome):
    print("Olá,", nome)

#Acessando a função 

saudacao("Lavínia")

#Função de retorno 
def soma (a,b):
    return a + b 

resultado = soma (3,5)
print(resultado)

'''def descontoA (valor1, desc)
    return valor1 - desc '''

#Exemplo com tratamento de erro 
try:
    num = int(input("Insira um número:"))
    print(num)
except:
    print("Você digitou algo inválido")



