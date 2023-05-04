'''
Fatorial de um numero

O que é um fatorial de uma numero?
- É o produto de numeros positivos menores ou igual ao numero, ele é representado por !;
Ex.: Fatorial de 5:

5! = 5 x 4 x 3 x 2 x 1 = 120

Crie um programa que vai receber um numero e vai exibir o seu fatorial. 

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
Ele usa apenas multiplicação, multiplica o numero digitado pelo usuario por ele mesmo e os seus antecessores;
Deve ser um valor positivo inteiro.


4 - Qual é o resultado esperado?
O produto da multiplicação dos dados de entredada por ele mesmo e seus antecessores;
Fatorial do dado de entrada seja exibido;


5 - Quais são as sequencias de passos a serem feitas para se alcançar o resultado esperado?
1 - Pedir para o usuario dado de entrada;
2 - Deve ser comparado para saber se o numero é positivo inteiro;
3 - Esse dado deve ser armazenado e convertido para numeral usando variaveis e int;
4 - Deve ser criado uma variavel que armazenara o resultado e inicializada ccom 1 que será o numero inicial multiplicado pelo dado de entrada;
5 - Deve ser criado um laço de repetição "for" com especificador range indicando:

-> 1 = Ele sempre vai começar a multiplicação de 1 até o dado de entrada estabelecido;
-> dado de entrada = Variavel que armazena o numero digitado pelo usuario + 1; 
-> + 1 = O range nunca inclui o ultimo numero, dessa forma ele incluirá, incrementando +1 na operação;

6- Por fim deve imprimir na tela para o usuario o resultado final que 

'''
numero = int (input('Digite um numero para ser calculado o seu fatorial ')) # Recebe o numero digitado que é convertido em numeral int;
if numero > 0: # Vai definir que o para continuar o numero deve ser positivo e em seguida vai definir o fatorial = 1 para iniciar a multiplicação do dado de entrada;
    print ('O numero é inteiro positivo, vamos continuar...')
    fatorial = 1 # Variavel que inicia com 1, será usada para iniciar a operação;
else: # Caso seja valores negativos ele exibe uma mensagem e falha, parando o código;
      print('O numero deve ser inteiro positivo, tente novmamente...')    
for numeros in range(1, numero + 1): # Laço de repetição com range com especificação 1 que vai dizer que ele irá começar a partir do 1 até o dado de entrada estabelecido;
        fatorial = fatorial*numeros # Fatorial iniciado em 1 vai multiplicar de 1 até o dado de entrada obtido que passara pelo laço for numeros fatorial*numeros Ex.: !5 = 1*1=1*2=2*3=6*4=24*5=;
print ('Fatorial do numero', numero, 'é', fatorial) # Em seguida ele vai printar a mensagem indicando o dado de entrada mas o fatorial desse dado.