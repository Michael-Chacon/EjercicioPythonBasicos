import random


def llenarArray(lista):

    for i in range(9):
        lista.append(random.randint(1,10))


def listaAscendente(ascendente):
    for i in ascendente:
        for j in range(0,len(ascendente)-1):
            if ascendente[j] > ascendente[j + 1]:
                aux = ascendente[j]
                ascendente[j] = ascendente[j + 1]
                ascendente[j + 1] = aux
    return ascendente


def listaDescendente(descendente):
    for i in descendente:
        for j in range(0,len(descendente)-1):
            if descendente[j] < descendente[j + 1]:
                aux = descendente[j]
                descendente[j] = descendente[j + 1]
                descendente[j + 1] = aux
    return descendente


lista = []
descendente = lista
ascendente = lista

llenarArray(lista)

print('Lista base')
print(lista)
    
print('Lista ascendente')
print(listaAscendente(ascendente))


print('Lista descendente')
print(listaDescendente(ascendente))