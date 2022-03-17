import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(lista)-1
    
    if limite_superior < limite_inferior:
        return -1
    # se usa recursión
    punto_medio = (limite_inferior + limite_superior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior )

if __name__=='__main__':
    # crear lista ordenada con 10,000 numeros aleatorios
    tamaño = 10000
    conjunto_inicial = set()
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
    
    lista_ordenada = sorted(list(conjunto_inicial))

    #medición del tiempo que toma conseguir los numeros con cada uno de los métodos de búsqueda
    # BÚSQUEDA INGENUA
    ''''inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua (lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")'''
    # BÚSQUEDA BINARIA
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")