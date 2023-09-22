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
    print('Não digitou um numero')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Digite a hora em números interios: ')

try:
    hora_int = int(entrada)
    if hora_int >= 0 and hora_int <= 11:
        print('Ola, Bom dia!!!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Ola, Boa tarde!!!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Ola, boa noite!!!')
    else:
        print('Hora desconhecida')
except:
    print('Não digitou um numero')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Escreva seu nome:')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print(' Seu nome é muito curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else: 
        print('Nome grande que issoooo')
else:
    print('Digite apenas letras')