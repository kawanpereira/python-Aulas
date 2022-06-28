"""
condições IF, ELIF e ELSE - Operadores Relacionais
==, >, >=, <, <= e !=
"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

idade_mínima = 18
idade_máxima = 60

if idade >= idade_mínima and idade <= idade_máxima:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'NÃO pode pegar o empréstimo.')