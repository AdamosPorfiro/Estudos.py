# Projeto 2 - Chute um numero

'''
Escreve um programa que ao iniciar el vai gerar um numero aleatório de 1 a 10 que permita o usuario chutar um numero até que
o valor gerado no inicio do programa seja chutado corretamente.

O programa deve informa se o chute foi, acima, abaixo ou igual ao valor aleatório gerado no inicio do programa

# Utilize o metodo dos 5q's;
# Analise criticamente o problma e descubra;
# Tente explicar o problema para você mesmo em voz alta e peça mais informações / 
investigue mais até você entender completamente o programa.


1- Quais são os dados necessarios?
-> Valor aleatorio de 1 até 10;
-> Um chute do usuario.

2- O que devo fazer com esses dados?
-> Eu devo comparar o chute do usuario com o valor aleatório que foi gerado no inicio do programa e dizer se o chute foi maior, menor ou igual ao valor gerado no inicio do programa.

3- Quais são as restrições desse problema?
-> Gerar um valor aleatorio de 1 a 10;

4- Qual é o resultado esperado?
-> O programa deve informa se o chute foi, acima, abaixo ou igual ao valor aleatório gerado no inicio do programa

5 - Quais são os passos a serem feitos para chegar ao resultado esperado?

-Pseudocódigo
input valor_aleatorio de 1 a 10
input chute_usuario
if chute_usuario > valor_aleatorio
    print O chute  foi maior que o gerado
if chute_usuario < valor_aleatorio
    print O chute foi menor que o valor gerado
if chute_usuario = valor_gerado
    print Você acertou!!! O chute é igual ao valor gerado

'''
# Para gerar um valor aleatorio em python é necessario importar uma biblioteca chamada "random" usando comandos (import random)

import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int (input ('Digite um chute de 1 a 10:  '))
    if chute > valor_aleatorio:
        print ('O valor',chute, 'digitado é maior que o valor gerado')
    elif chute < valor_aleatorio:
        print ('O valor', chute, 'digitado é menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print ('Acertou!!! O valor', chute,  'digitado é igual ao numero gerado', valor_aleatorio)


