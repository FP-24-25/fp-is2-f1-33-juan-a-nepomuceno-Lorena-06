'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import TypeVar
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Recorrido import Recorrido
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Grafo import Grafo
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega2.tipos.Pila import Pila

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_en_profundidad(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E]) -> Recorrido_en_profundidad[V,E]: #crear una nueva instancia de la clase a partir de un grafo
        return Recorrido_en_profundidad
    
    def __init__(self,grafo:Grafo[V,E]) -> None:
        super().__init__(grafo)
    
    
    def traverse(self,source:V) -> None:
 
        #Realizo un recorrido en profundidad del grafo comenzando desde el vértice
        pila = Pila[V]()  
        pila.push(source)
        self._tree[source] = (None, 0.0)
        
        while not pila.is_empty():# Mientras la pila no esté vacía
            current = pila.pop()
        self._path.append(current)

        # Recorrer los sucesores (vecinos) del vértice actual
        for neighbor in self._grafo.successors(current):
            if neighbor not in self._tree:
                # Registrar el predecesor y el peso acumulado
                weight = self._tree[current][1] + self._grafo.edge_weight(current, neighbor)
                self._tree[neighbor] = (current, weight)
                pila.push(neighbor)


if __name__ == '__main__':
    pass