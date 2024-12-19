'''
Created on 9 nov 2024

@author: loren
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

class Cola(AgregadoLineal[E]):
    
    @staticmethod 
    def of() -> Cola[E]:
            return Cola()
    
    def add(self, *e:E) -> None:
        self._elements.extend(e)
        
    def __str__(self) -> str:
        return f'Cola({",".join(map(str, self._elements))})'


