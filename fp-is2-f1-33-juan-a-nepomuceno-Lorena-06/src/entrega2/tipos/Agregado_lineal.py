'''
Created on 9 nov 2024

@author: loren
'''
from __future__ import annotations
from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

#Definimos un tipo genérico para los elementos

E = TypeVar('E')

class AgregadoLineal(ABC,Generic[E]):
    
    def __init__(self):
        self._elements: List[E] = []
        
    @property
    def size(self) -> int:
        return len(self._elements)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property 
    def elements(self) -> list[E]:
        return self._elements 

    @abstractmethod 
    def add(self,e:E) -> None:
        pass
    
    def add_all(self, ls: List[E]):
        for e in ls:
            self.add(e)
    
    def remove(self) -> E:
        assert self.size > 0, 'El agregado está vacío'        
        return self._elements.pop(0)
    
    def remove_all(self) -> list[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements 


if __name__ == '__main__':
    pass