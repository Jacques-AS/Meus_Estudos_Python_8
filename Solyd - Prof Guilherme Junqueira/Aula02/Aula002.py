'''Faça um formulário que pergunte o nome, cpf, endereço, idade, altura e telefone.
Imprima isso em um relatório organizado.'''
from time import sleep
print()
print('-=<>='*15)
nome = str(input('Digite seu NOME: '))
cpf = str(input('Digite seu CPF: '))
endereco = str(input('Digite seu ENDEREÇO: '))
idade = int(input('Digite sua IDADE: '))
altura = float(input('Digite sua ALTURA: '))
telefone = str(input('Digite seu TELEFONE: '))
print()
print('-=<>='*15)
print()
print('\033[33mPROCESSANDO ........\033[m')
print()
sleep(3)
print (f'Seu nome é: {nome}\nVocê tem {idade} anos de idade\n'
       f'Sua altura é: {altura}\n'
       f'Seu CPF: {cpf} e Seu Contato Telefônico: {telefone}\n'
       f'Seu endereço: {endereco}')
print('-=<>='*15)