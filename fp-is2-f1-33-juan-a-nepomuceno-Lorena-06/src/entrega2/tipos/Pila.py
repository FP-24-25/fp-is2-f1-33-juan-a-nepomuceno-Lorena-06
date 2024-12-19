'''
Created on 9 nov 2024

@author: loren
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

class Pila(AgregadoLineal[E]):
    
    @staticmethod 
    
    def of() -> Pila[E]:
        return Pila()
    
    def add(self, e:E) -> None:
        self.elements.insert(0,e)


if __name__ == '__main__':
    pass