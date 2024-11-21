'''
Created on 21 nov 2024

@author: loren
'''
from __future__ import annotations
from typing import TypeVar, List, Callable, Generic
from abc import ABC, abstractmethod


E = TypeVar('E')


class AgregadoLineal2(ABC,Generic[E]):
    
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
    # He copiado el código de Agregado Lineal y ahora le añado las siguientes modificaciones:

    def contains(self, e:E) -> bool:
        return e in self._elements 
    
    def find(self, func: Callable[[E], bool]) -> E | None:
        for element in self._elements:
            if func(element):
                return element
        return None
    
    def filter(self, func: Callable[[E], bool]) -> list[E]: 
        return [element for element in self._elements if func(element)]

'''Voy a crear una clase llamada ColaConLimite que hereda de la clase AgregadoLineal'''

class ColaConLimite(AgregadoLineal2[E]):
    
    def __init__(self, capacidad: int):
        super().__init__()
        self._capacidad = capacidad # en el parámetro capacidad guarda el número máximo de elementos que puede tener la cola 
    
    @property
    def capacidad(self) -> int:
        return self._capacidad
    
    def add(self, e: E) -> None:
        if self.size >= self.capacidad:
            raise OverflowError("La cola está llena")
        self._elements.append(e)
    
    @classmethod
    def of(cls, capacidad: int) -> ColaConLimite[E]:
        return cls(capacidad)
    
    def is_full(self) -> bool:
        return self.size >= self.capacidad

''' Voy a modificar la clase AgregadoLineal añadiéndole las funciones contains, find y filter'''
   
        
    
'''Ahora voy implementar todas las pruebas'''
cola=ColaConLimite.of(3)
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")
#Pruebo add en cola
try:
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)
print(cola.remove()) #debe imprimir Tarea 1

#Pruebo el método contains en cola
print(cola.contains("Tarea 1"))
print(cola.contains("Tarea 2"))

#Pruebo el método find en cola
found = cola.find(lambda x: "Tarea" in x)
print(found)
    
#Pruebo el método filter en cola
filtered = cola.filter(lambda x: "Tarea" in x)
print(filtered)
