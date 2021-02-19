# merge sort o busqueda por mezcla

import random

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

    # Llamada recursiva en cada mitad 
    merge_sort(izquierda)
    merge_sort(derecha)
    
    # Iteradores para recorer las 2 sublistas
    i = 0
    j = 0 
    # Iterador para la lista principal
    k = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else: 
            lista[k] = derecha[j]
            j += 1
        k += 1 
    


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera tu lista?'))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    print(lista)
    print('-' * 20)

    lista_ordenada = merge_sort(lista)
    print(lista_ordenada)


