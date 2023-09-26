print('1. (1,0 ponto) escreva um programa em Python que mostre os números de uma lista após\n'
'remover os números pares dela.\n')

print('--------------------------------------------------------------------------------------')
print('2. (1,0 ponto) escreva um programa em Python que aceite uma lista de inteiros. Calculen\n'
'o comprimento da lista e a quantidade de ocorrências do quinto elemento da lista.\n'
'Retorne True se o comprimento da lista for 8 e o quinto elemento ocorrer três vezes\n'
'na referida lista.\n')

print('--------------------------------------------------------------------------------------')
print('3. (1,0 ponto) escreva um programa em Python para verificar se uma determinada chave\n'
'já existe em um dicionário.\n')

dicionario = {'nome': 'Flavio', 'idade': 30, 'professor': 'analise e desenvolvimento de sistema por amor'}
opcao = input('Qual chave você que saber? 1, 2 ou 3. \n 1 - Nome \n 2 - Idade \n 3 - Professor \n = ')

if opcao == '1':
    chave = 'nome'
elif opcao == '2':
    chave = 'idade'
elif opcao == '3':
    chave = 'professor'
else:
    print('opcao invalida')
    chave = None

if chave is not None:
    if chave in dicionario:
        print('A chave {} existe no dicionário.\n'.format(chave))
    else:
        print('A chave {} não existe no dicionário.\n'.format(chave))
print('--------------------------------------------------------------------------------------')
print('4. (1,0 ponto) escreva um programa em Python para remover um item de uma tupla.\n')

tupla_n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print('Minha tupla é: {}'.format(tupla_n))

try:
    remover = int(input('Qual número você deseja remover? '))
    
    if remover in tupla_n:
        tupla_n2 = tuple(x for x in tupla_n if x != remover)
        print('Minha nova tupla é: {}\n'.format(tupla_n2))
    else:
        print('Número não está na tupla.\n')
except:
    print('Não digitou um número.\n')

print('--------------------------------------------------------------------------------------')
print('5. (1,0 ponto) escreva uma função em Python que receba uma lista como parâmetro e\n'
'retorne uma nova lista que contenha somente elementos distintos da primeira lista.\n')
def lista_dif(lista):
    lista_1= []
    
    for elemento in lista:
        if elemento not in lista_1:
            lista_1.append(elemento)
    
    return lista_1

minha_lista = [1, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7,]
print('Minha lista atual: \n{}'.format(minha_lista))
lista_2 = lista_dif(minha_lista)
print('Minha lista sem numero repeditos: \n{}'.format(lista_2))