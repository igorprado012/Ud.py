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