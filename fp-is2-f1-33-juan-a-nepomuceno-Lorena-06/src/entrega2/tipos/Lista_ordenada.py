'''
Created on 9 nov 2024

@author: loren
'''

from __future__ import annotations
from typing import Callable, TypeVar, Generic
from entrega2.tipos.Agregado_lineal import AgregadoLineal

E = TypeVar('E')
R = TypeVar('R')

class ListaOrdenada(AgregadoLineal[E], Generic[E,R]):
    
    def __init__(self, order:Callable[[E],R]):
        super().__init__()
        self._order = order 
        
    @staticmethod 
    
    def of(order: Callable[[E], R]) -> ListaOrdenada[E, R]:
        return ListaOrdenada(order)
    
    def __index_order(self, e: E) -> int:
        for i, element in enumerate(self._elements):
            if self._order(e) < self._order(element):
                return i
        return self.size

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index,e)
        
    def __str__(self) -> str:
        return f'ListaOrdenada({self._elements})'


