'''
Created on 9 nov 2024

@author: loren
'''

from entrega2.tipos.Cola import Cola

print('TEST DE COLA:')

cola = Cola.of()

cola.add(23, 47, 1, 2, -3, 4, 5)
print(f"Resultado de la cola: {cola}")

elementos_eliminados = cola.remove_all()
print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")



if __name__ == '__main__':
    pass