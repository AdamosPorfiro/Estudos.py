#Coleções(Listas)


'''

preço_1 = 15
preço_2 = 30    Podemos armazenar dessa forma, porém por boa pratica e para um código mais limpo usamos o exemplo abaixo;
preço_3 = 200

preços = [20, 30, 50] # Podemos armazenar os mesmos valores em uma só variavel e acessa-los por meio do "indice";
indice ->    0 - 1 - 2

'''

'''

preco = [20, 30, 50]
print(preco[0])
print (preco.index(50))  # Ele vai buscar dentro da lista preço o indice que corresponde ao numero 50 (2).

diversos_itens = [20,'Adamos',True] # É possivel armazenar um diversidade de dados, numericos, strings, booleanos.
print(diversos_itens[0])
print(diversos_itens[1]) # Podemos imprimir esses valores de forma mais simples, usando um laço.
print(diversos_itens[2])

for diversidade in diversos_itens:
    print(diversidade)

'''

'''

Problema 1

Some os valores, dados uma coleção de idades [15, 46, 75, 34, 23] imprima na tela a soma desses valores.

1 - Quais são os dados de entrada?
input 15, 16, 75, 34, 23.
input total = 0 

2 - O que devo fazer com esses dados?
Devemos fazer com que o programa passe por cada idade somando-os utilizando coleções(Listas) e laço.


3 - Quais são as restrições desse problema?
Deve somar os valores e exibir na tela.

4 - Qual é o resultado esperado?
A exibição da soma desses valores.

5 - Qual a sequência de passos a ser feita para se alcançar o resultado?
1 - Armazenar os idades em uma variavel do tipo Lista;
2 - Criar outra variavel que vai armazenar o total das idades somada;
3 - Criar um laço "for" para que ele passe por cada item da lista somando-os, a cada soma ele armazena o resultado no total e soma novamente até
esgotar as idades disponivel na lista;
3 - Exibir na tela o resultado da soma.

'''
idades = [15, 16, 75, 34, 23] # Variavel idade
total = 0 # Variavel total (resultado)
for idade in idades: # Laço chado de idade que invoca a variavel idades
    total = total + idade # A cada vez que ele passa por um item da lista ele vai somar com o total que vai acumulando dentro dele Ex: 0 + 15 = 15...
print(total) # Exibi na tela para o usuario o total somado (Resultado).


