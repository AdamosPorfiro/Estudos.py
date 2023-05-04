# Laço de repetição e Listas

'''
O que são laços de repetição?
- São maneiras de executar o mesmo comando varias vezes de forma mais simplificada

Problema 1 

Imprima a palavra "carregando" três vezes

for item in coleção:

for = para 
item = nome
in = de, a, em
range = coleção
comandos a executar

range: È uma forma de gerar listas no python 

1 ° Exemplo(Especificação):

for item in range(1,21): -> Range vai imprimir 1 vez os numeros de 1 a 20 (1 = numero inicial / 21 = O numero que ele estará finalizando).
        print(item)

O range não inclui o ultimo numero especificado, por isso na execução ele imprimi até o 20

2 ° Exemplo(Especificação)

for item in range(1,21,2) -> A ultima especificação indica os pulos que ele vai dar entre cada valor;
por exemplo a cada 2 numeros ele pula 1 sendo 1,3,5,7,9.

for palavra in range (1,4):
    print('Carregando')

for item in range(1,21):
    print(item)

for item in range(1,21,2):
    print(item)


'''


'''

Como podemos criar uma lista em python?
- nome_da_variavel = ['Quais','quer','valores','que','queira','armazenar'];
cada nome deve estar preenchido por aspas simples e separados por virgula.

usar um laço de repetição para imprimir todos os nomes

nomes = ['Adamos', 'Alesson', 'Vilma', 'Pamela']
for nome in nomes: # Para ajudar a entender melhor, ue o nome da variavel no plural e o nome do for no singular.
    print(nome) # Ele vai imprimir a variavel for que possui o nome chamado "nome".
'''

'''
Problema 2

Imprima os valores de 1 a n

1 - Quais são os dados necessarios?
- input valor_maximo - Digitado pelo usuario.

2 - O que devo fazer com esses dados?
- Devemos exibi-lo na tela de 1 ao valor_maximo

3 - Quais são as restrições do problema?
- Deve imprimir para o usuario de 1 ao numero digitado

4 - Qual é o resultado esperado?
-  Exibição de 1 ao numero digitado

5 - Qual é a sequencia de passos a ser feita?
1 - O programa deve exibir uma mensagem para o usuario pedindo que digite o um numero;
2 - Esse numero deve ser armazenado e convertido de string para numérico;
3 - Devemos definir um valor_inicial que será 1 para que ele conte de 1 ao valor digitado pelo usuario;
4 - Montamos um laço com range e especificação com o valor_inicial (onde a contagem vai começar) e valor_maximo (onde a contagem vai terminar)
+ 1 já que range não inclui o ultimo numero;
5 - Em seguida um print da função for, para o usuario ver o resultado na tela;

'''
valor_maximo = int(input('Digite um valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo + 1):
    print(numero)


