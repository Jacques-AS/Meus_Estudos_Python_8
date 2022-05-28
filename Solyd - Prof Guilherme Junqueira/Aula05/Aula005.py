'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista

from time import sleep
print('\033[1:33m*\033[m'*45)
print('\033[1:34m ===== PREPARANDO A LISTA DE CONVIDADOS =====\033[m')
print('\033[1:33m*\033[m'*45)
quant_convidados = int(input('Digite a Quantidade de Convidados para FESTA: '))
lista_convidados = []
convidados = 1
while convidados <= int(quant_convidados):
    nome_convidado = str(input('Digite seu Convidado nº' + str(convidados) + ': '))
    lista_convidados.append(nome_convidado)
    convidados += 1
print('\033[1:33m-=<>=\033[m'*9)
print('\033[1:36mANALISANDO A LISTA DE CONVIDADOS.....\033[m')
sleep(3)
print(f'Serão {quant_convidados} Convidados para FESTA nos quais são:')
for grupo_convidado in lista_convidados:
        print(grupo_convidado)'''


'''EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista'''

quant_convidados = int(input('Informe a quant de convidados: '))
lista_convidados = []
convidados = 1
while convidados <= int(quant_convidados):
    nomes =  str(input('Digite nome do seu convidado nº'+ str(convidados)+':'))
    lista_convidados.append(nomes)
    convidados += 1
print(f'Nesta festa haverá {quant_convidados} de convidados, que são eles:')
for grupo_convidados in lista_convidados:
    print(grupo_convidados)