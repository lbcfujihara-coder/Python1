

#Aula 17/06/26

'''
1. Acessar a biblioteca json que já exite no python
2. pede para abrir o arquivo dados.json
3. Faça uma leituta - utf-8 - portugues 
4. Guarde os dados desse arquivo e guarde na variavel arquivos 
'''
'''
Esse r, é de read, leia
'''
import json 
with open ('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)

#Para ver dados específicos desse arquivo
'''Se houvessem vários nomes, ele mostraria uma lista de vários nomes'''

print(dados['nome'])

#Convertendo json em str
'''
json.dumps: É uma funçãom para converter um json para string, em formato de dict
1. dados: nome da variavel
2. indent 4, relacionado a dentação 
3. ensure_ascii=false permite mostrar carateres especiais 
'''
texto = json.dumps(dados, indent=4, ensure_ascii=False)
print(texto)


#Convertendo str em json

'''Nessa caso, não pode deixar espaço no doct se não irá dar erro
As aspas de fora devem ser opostas a de fora'''

PessoaNova = '{"nome": "Vânia", "idade": 50 }'

dados = json.loads(PessoaNova)
print(dados)

'''As respostas de um formulário são string 
O banco de dados que o armazena é json
Logo a tansição desses ambiente, deve ser realizada a conversão '''

#Atualizado dados

import json 
with open ('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

'''
Esse r, é de read, leia
'''

dados['idade'] = 35 # alteração

with open ('dados.json', 'w', encoding='utf-8') as arquivo:
    dados = json.dump(dados, arquivo, indent=4, ensure_ascii=False)

'''
Esse w, é de write, escreva
'''















































































































































































