'''
Projeto 3 - Medidor de velocidade

Levando em consideração a velocidade máxima  permitida de 80 km em uma determinada rua.
Crie um programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade diga se ele tomou
uma multa leve, grave ou gravissima. 
Levando em consideração que se a pessoa estiver abaixo da velocidade máxima, então deve exibir "Não houve multa", caso esteja até 
10 km acima deve exibir, "levou multa leve", caso esteja de 11 km a 20 km da velocidade máxima exiba, "levou multa grave" e
caso esteja acima de 20 km da velocidade máxima exiba, "levou multa gravissima"

# Utilize o metodo dos 5q's;
# Analise criticamente o problma e descubra;
# Tente explicar o problema para você mesmo em voz alta e peça mais informações / 
investigue mais até você entender completamente o programa.

1- Quais são os dados necessarios?
-> input velocidade_maxima de 80 km;
-> input velocidade_usuario.

2- O que devo fazer com esses dados?
-> Com base na velocidade_usuario diga se ele tomou uma multa leve, grave ou gravissima;
-> Levando em consideração que se a pessoa estiver abaixo da velocidade máxima, então deve exibir "Não houve multa", caso esteja até 
10 km acima deve exibir, "levou multa leve", caso esteja de 11 km a 20 km da velocidade máxima exiba, "levou multa grave" e
caso esteja acima de 20 km da velocidade máxima exiba, "levou multa gravissima"

3- Quais são as restrições desse problema?

4- Qual é o resultado esperado?
-> Com base na velocidade inserida exibir se ele tomou uma multa leve, grave ou gravissima. 

5 - Quais são os passos a serem feitos para chegar ao resultado esperado?

velocidade_maxima = 80
input velocidade_usuario
if velocidade_usuario <= velocida_maxima:
    print não houve multa
if velocidade_usuario > velocidade_maxima e velocidade_usuario <= velocidade_maxima + 10: 
    print Levou uma multa leve
if velocidade_usuario > velocidade_maxima + 11 e velocidade_usuario <= velocidade_maxima + 20:
    print Levou uma multa grave
if velocidade_usuario > velocidade_maxima + 21:
    print levou uma multa gravissima

'''

velocidade_maxima = 80
continuar = 1
while continuar == 1:
    velocidade_usuario = int (input('Digite a velocidade que você estava:  '))
    if velocidade_usuario < velocidade_maxima:
        print('Não levou multa')
    elif velocidade_usuario > velocidade_maxima and (velocidade_usuario <= velocidade_maxima + 10):
        print('Levou multa leve')
    elif velocidade_usuario > velocidade_maxima+11 and (velocidade_usuario <= velocidade_maxima + 20):
        print('Levou multa grave')
    elif velocidade_usuario > velocidade_maxima+21:
        print('Levou multa gravissima') 
    continuar = int (input('Deseja digitar outra velocidade?  1 - Sim e 2 - Não:  '))
    


        
