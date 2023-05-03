# Laço de repetição e Listas

'''
O que são laços de repetição?
- São maneiras de executar o mesmo comando varias vezes de forma mais simplificada

Problema 1 

Imprima a palavra "carregando" três vezes

for = para 
item
in = e
coleção:
comandos a executar
range: È uma forma de gerar listas no python 

1 - Exemplo(Especificação):

for item in range(1,21): -> Range vai imprimir 1 vez os numeros de 1 a 20 (1 = numero inicial / 21 = O numero que ele estará finalizando).
        print(item)

O range não inclui o ultimo numero especificado, por isso na execução ele imprimi até o 20

2 - Exemplo(Especificação)

for item in range(1,21,2) -> A ultima especificação indica os pulos que ele vai dar entre cada valor;
por exemplo a cada 2 numeros ele pula 1 sendo 1,3,5,7,9...

'''

for palavra in range (1,4):
    print('Carregando')

for item in range(1,21):
    print(item)

for item in range(1,21,2):
    print(item)

