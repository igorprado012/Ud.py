"""informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar:
        par_impar_texto = 'par'

    print('Seu numero {} é {}.'.format(entrada, par_impar_texto))
else:
    print('Não foi digitaddo nada')

'''Ou'''

entrada = input('Digite um numero: ')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar:
        par_impar_texto = 'par'

    print('Seu numero {} é {}.'.format(entrada, par_impar_texto))
except:
    print('Não difitou um numero')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
