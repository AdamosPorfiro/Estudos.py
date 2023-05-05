# Variaveis

velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 #float (valor com demais)

#Valores booleanos (True ou False)
porta_esta_aberta = True #False

#Strings (Conjunto de caracteres) utliza aspas simples
nome_do_curso = 'Lógica de programação'

#Como variaveis seriam usada em um programa real?

#Problema 1 - Valor hora
# Escreva um programa que retorne o valor hora de um funcionario com base no seu salario mensal e horas trabalhas no mês.

'''
input salario_mensal
input horas_mensal
valor_hora = salario_mensal / horas_mensal
print valor_hora
'''
salario_mensal = input('Qual o seu salario mensal?  ')
horas_mensal = input('Quantas horas trabalhadas no mês?  ')
valor_hora = int (salario_mensal) / int (horas_mensal)
print(valor_hora)