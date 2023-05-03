# Condicionais
# if , elif , else

"""
Problema 1 -

E ae Adamos, bora jogar hoje?
Se eu terminar meu trabalho aqui a gente joga!


trabalho_terminado = False
if trabalho_terminado == True:
    print('Opa, bora jogar!')
else:
    print('Mano, não posso jogar agora!')
"""
"""
Problema 2 -

Ei você consegue me ajudar a levar essas caixa lá para fora hoje?
Se eu estiver livre sim, mas, se não der pede para o meu irmão ajudar.


estou_livre = input('Pode me ajudar a carregar essas caixa hoje a tarde? sim ou não:  ')
if estou_livre == 'sim':
    print('Ok, Posso ajudar hoje sim!')
elif estou_livre == 'Sim':
    print('Ok, Posso ajudar hoje sim!')
elif estou_livre == 'SIM':
     print('Ok, Posso ajudar hoje sim!')
else:
    print('Desculpe, peça ao meu irmão para te ajudar!')
"""
"""
Problema 3 - 

Eu cheguei na aula atrasado, eu posso entrar?
Se essa não for a sua terceira vez que chega atrasado pode sim, caso contrário irá tomar um suspensão.

1 - Quais são os dados de entrada?
input numero_de_atrasos

2 - O que deve ser feito com os dados de entrada?
- Precisamos comparar a quantidade de atrasos para definir se o aluno pode entrar na sala ou se tomará uma suspensão

3 - Quais são as restrições do problema?
- Se o aluno pode entrar ou não com base em seus atrasos;
- Se for acima de 3 ele não tomará um suspensão.

4 - Qual a sequencia de passos que devem ser feitas para chegar ao resultado?
-input Quantos atrasos você já possui?

if atraso == 1
    print pode entrar
if atraso == 2
    print pode entrar
else
    print Vai tomar suspensão!


numero_de_atrasos = int(input("Quantos atrasos você possui?"))
if numero_de_atrasos >= 3:
    print("Você está suspenso")
elif numero_de_atrasos == 1:
    print("Ok, Você pode entrar, porém caso tome mais 2 faltas você será suspenso!")
elif numero_de_atrasos == 2:
    print("Ok, Você pode entrar, porém caso tome mais 1 falta você será suspenso")
else:
    print("Você pode entrar")
"""

"""
Problema - 4

Identifique o maior entre os 2 numeros digitados pelo usuario

1 - Quais são os dados de entrada?
input valor_1;
input valor_2;

2 - O que devo fazer com esses numeros?
Devem ser comparados e o programa deve dizer qual é o maior entre eles.

3 - Qual a restrição deste problema?
Um dos numeros deve ser maior que outro.

4 - Qual o resultado esperado?
A comparação dos numeros, indicando qual deles é o maior.

5 - Qual é a sequencia de passos a ser feita para se alcançar o resultado?
input valor_1
input valor_2
if valor_1 > valor_2
    print O valor_1 é o maior numero
if valor_1 < valor_2
    print O valor_2 é o maior numero
if valor_1 == valor_2
    print Ops,por favor digite valores diferentes    
"""

valor_1 = int(input('Digite um valor:  ')) # Obs.: Comparações não podem ser feitas com strings e precisam ser convertidos para numéricos (int, float)
valor_2 = int(input('Digite outro valor:  '))
if valor_1 == valor_2:
    print('Ops, por favor digite valores diferentes')
elif valor_1 > valor_2:
    print('O primeiro valor digitado é o maior, sendo ele o numero:', valor_1)
else:
    print('O segundo valor digitado é o maior, sendo ele o numero:', valor_2)