'''
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
e decide se ela está apta a ser do Exército.
Para entrar no Exército é preciso ter mais de 18 anos ou pesar ou igual
60 kilos e medir mais ou igual 1.70 metro.
'''
from time import sleep
print ()
print ('\033[1:33m******** Ficha de Inscrição ********\033[m')
idade = int(input('Digite sua IDADE: '))
peso = float(input('Digite sua PESO: '))
altura = float(input('Digite sua ALTURA: '))
print('\033[1:33mANALISANDO CADASTRO......\033[m')
sleep (3)
print('-=<>='*15)
if idade >= 18 and peso >= 60 and altura >= 1.70:
    print ('Você foi APROVADO para se apresentar ao EXÉRCITO BRASILEIRO')
else:
    print ('Você foi \033[1:31mREPROVADO\033[m')
print()
print('\033[1:32mEXÉRCITO BRASILEIRO, pátria amada \033[1:33mBRASIL.\033[m')
print('\033[1:32m*******   S E L V A  !!!  *******\033[m')
