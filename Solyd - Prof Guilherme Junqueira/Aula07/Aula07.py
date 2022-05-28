'''
EXERCICIO: Escreva uma funcao que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa colecao
faça outra funcao que retorna o menor numero dessa coleçao
'''
from time import sleep
print('\033[1:33m*\033[m'*45)
print('SEJA BEM VINDO...............................')
print('\033[1:33m*\033[m'*45)
print()
def maior_valor(estrutura):
    maior_numero = 0
    for numero in estrutura:
        if int(numero) > int(maior_numero):
            maior_numero = numero
    print(f'O MAIOR valor desta COLEÇÃO é: {maior_numero}')

def maior_valor1(estrutura):
    maior_numero = 0
    for numero in estrutura:
        if int(numero) > int(maior_numero):
            maior_numero = numero
    return int(maior_numero)


def menor_valor(estrutura):
    menor_numero = maior_valor1(estrutura) + 1
    for numero in estrutura:
        if int(numero) < int(menor_numero):
            menor_numero = numero
    print(f'O MENOR valor desta COLEÇÃO é: {menor_numero}')


colecao_de_numeros = set()
quantidade = input('QUANTOS NÚMEROS VOCÊ IRÁ DIGITAR ?:')

contador = 0

while contador < int(quantidade):
    colecao_de_numeros.add(input(f'Digite o {contador + 1}° Número:'))
    contador += 1

print('\033[1:36mANALISANDO.............\033[m')
sleep(3)
print(f'Você digitou a quantidade {quantidade} vezes, segue abaixo a LISTA: ')
print(colecao_de_numeros)

maior_valor(colecao_de_numeros)
menor_valor(colecao_de_numeros)