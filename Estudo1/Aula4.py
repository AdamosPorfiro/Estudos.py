#Coleções(Listas)

'''
preço_1 = 15
preço_2 = 30    Podemos armazenar dessa forma, porém por boa pratica e para um código mais limpo usamos o exemplo abaixo;
preço_3 = 200

preços = [20, 30, 50] # Podemos armazenar os mesmos valores em uma só variavel e acessa-los por meio do "indice";
indice ->    0 - 1 - 2 
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