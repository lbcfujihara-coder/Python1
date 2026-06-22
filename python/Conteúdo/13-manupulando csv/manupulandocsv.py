#Aula 17/06/26

import csv 

listaprodutos = [
    ['produto', 'quantidade', 'valor'],
    ['computador', '2', '1999.99'],
    ['camera', '10', '79.99'],
    ['microfone', '7', '39.99']
]

''' 
é possível tanto trazer uma planílha no excel quanto fazer no python e enviar pra lá
'''
#Escrita
'''
with open('lista de produtos.csv', 'w', newline= '') as arquivo:
    
    csv_writer = csv.writer(arquivo, delimiter= ';')
    
    for produto in listaprodutos:
        csv_writer.writerow(produto)
        print(produto) 
'''

'''
1. newline '': vai estar vazia pq vai substituir tudo - evita linha em branco 
2. csv.writer: vai escrever nesse arquivo, demilitado por ponto e vírgula por causa da linguagem
3. for in: passe por todos os produtos
4. writerow: vai escrever em formato de linha 
'''

#Aula 22/06

#Leitura
'''
with open ('lista de produtos.csv', 'r') as arquivo:
    csv_writer = csv.reader(arquivo, delimiter= ';')
    for line in csv_writer:
        print(line)
'''

'''
with open: abrir o arquivo
as arquivo: 'finalizar' quando acabar
r: read
csv.reader: para ler o arquivo 
delimiter: delimitadao por ;
'''

#Lê o que já existe no arquivo

produtos_existentes = set()

try:
    with open('lista de produtos.csv', 'r') as arquivo:
        reader = csv.reader(arquivo, delimiter= ';')
        for linha in reader:
            produtos_existentes.add(tuple(linha)) #Transforma em tupla para comparação
except FileNotFoundError:
    pass # se o arquivo ainda não existe 

#Agora grava só os dados q1ue não existirem 

with open('lista de produtos.csv', 'a', newline= '') as arquivo:
    writer = csv.writer(arquivo, delimiter= ';')
    for produto in listaprodutos[1:]: #ignora o cabeçalho, que é o índice 0 e começa no índice 1
        if tuple(produto) not in produtos_existentes: #se o produto não exite em produtos existentes
            writer.writerow(produto) 
            print(produto)
        
'''
a = append // atualização 
Ao atualizar a lista do começo do arquivo, o csv atualizou, manteve os primeiros itens (originais) e adicionou
os novos itens no arquivo 
'''

