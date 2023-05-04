'''
Fatorial de um numero

O que é um fatorial de uma numero?
- É o produto de numeros positivos menores ou igual ao numero, ele é representado por !;
Ex.: Fatorial de 5:

5! = 5 x 4 x 3 x 2 x 1 = 120

Crie um programa que vai receber um numero e vai exibir o fatorial de uma numero

# Utilize o metodo dos 5q's;
# Analise criticamente o problma e descubra;
# Tente explicar o problema para você mesmo em voz alta e peça mais informações / 
investigue mais até você entender completamente o programa.

1 - Quais são os dados de entrada necessarios?
input valor_digitado_pelo_usuario

2 - O que devo fazer com estes dados?
Deve multiplicar o numero digitado pelo usuario, pelos numeros positivos igual e
menores que ele.

3 - Quais são as restrições desse problema?
Ele usa apenas multiplicação, multiplica o numero digitado pelo usuario por ele mesmo e os seus antecessores.


4 - Qual é o resultado esperado?
O produto da multiplicação dos dados de entredada por ele mesmo e seus antecessores.


5 - Quais são as sequencias de passos a serem feitas para se alcançar o resultado esperado?
1 - Pedir para o usuario dado de entrada;
2 - Esse dado deve ser armazenado e convertido para numeral usando variaveis e int;
3 - Deve ser criado uma variavel que armazenara o resultado e inicializada ccom 1 que será o numero inicial multiplicado pelo dado de entrada;
4 - Deve ser criado um laço de repetição "for" com especificador range indicando:

-> 1 = Ele sempre vai começar a multiplicação de 1 até o numero digitado pelo usuario;
-> dado de entrada = Variavel que armazena o numero digitado pelo usuario + 1; 
-> + 1 = O range nunca inclui o ultimo numero, dessa forma ele incluirá, incrementando +1 na operação;

5- Por fim deve imprimir na tela para o usuario o resultado final que 

'''
numero = int (input('Digite um numero para ser calculado o seu fatorial '))
fatorial = 1
for numeros in range(1, numero + 1):
    fatorial = fatorial*numeros
print ('Fatorial do numero', numero, 'é', fatorial)