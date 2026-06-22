#Requisição

import requests

#Biblioteca que transforma objeto em python

from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text,'html.parser')

'''##(print(dados_pagina.prettify())) - esse traz toda a programação da página '''

#------------------------------------------------------------------------------------------------#

# vai trazer todas as frases classificadas como quote, vem o texto, o autor, tudo que estiver dentro daquela class


'''
todas_frases = dados_pagina.find_all('div', class_="quote") 
#Faz um loop para mostrar todas as frases


for div in todas_frases:
    print(div)

#------------------------------------------------------------------------------------------------#
    
# para trazer somente o texto das frase

for div in todas_frases:
    texto = div.find('span', class_="text").text
    print(texto)

'''

# Quando vc olha no site, a caixa que armazena somente a citação, é texto, contido em span

#------------------------------------------------------------------------------------------------#

#Para achar todas as sitações de forma rápida

todas_frasesrapida = dados_pagina.find_all('span', itemprop="text")

for div in todas_frasesrapida:
    print(div.text)
#.text serve para pegar o texto da tag beautiful (ou seja, o texto do site e não de uma string )


