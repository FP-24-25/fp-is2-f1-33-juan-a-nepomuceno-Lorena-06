'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

V = TypeVar('V') #Vértices (vertex)
E = TypeVar('E') #Aristas (edge)

class Grafo(ABC,Generic[V,E]):
    
    @abstractmethod
    def successors(self,vertex:V) -> set[V]: #devuelve todos los vértices a los que se llega a partir de un vértice
        pass
    
    @abstractmethod
    def edge_weight(self,sourceVertex:V, targetVertex:V) -> float: #devuelve algo(distancia) de la arista entre 2 vértices
        pass
    
    @abstractmethod
    def edge(self,sourceVertex:V, targetVertex:V) -> E: #devuelve la arista que conecta los 2 vértices dados
        pass

if __name__ == '__main__':
    pass