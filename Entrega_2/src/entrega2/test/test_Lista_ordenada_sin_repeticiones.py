'''
Created on 9 nov 2024

@author: loren
'''

from entrega2.tipos.Lista_ordenada_sin_repeticion import ListaOrdenadaSinRepeticion

print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")

lista = ListaOrdenadaSinRepeticion.of(lambda x: -x)

lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)

print(f'Resultado de la lista ordenada sin repetición: ListaOrdenadaSinRepeticion ({lista._elements})')


def test1():
    removed_element = lista.remove()
    print(f'El elemento eliminado al utilizar revome(): {removed_element}')

def test2():
    removed_elements = lista.remove_all()
    print(f'Elementos eliminados utilizando remove_all: {removed_elements}')

def test3():
    lista.add(0)
    print(f'Lista después de añadirle el 0: ListaOrdenada({lista._elements})')
    lista.add(0)
    print(f'Lista después de añadirle el 10: ListaOrdenada({lista._elements})')
    lista.add(7)
    print(f'Lista después de añadirle el 7: ListaOrdenada({lista._elements})')
    

if __name__ == '__main__':
    
    test3()
    
