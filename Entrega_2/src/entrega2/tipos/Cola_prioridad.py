'''
Created on 9 nov 2024

@author: loren
'''

from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple

E = TypeVar('E')
P = TypeVar('P')


class ColaPrioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[Tuple[E, P]] = []

   
    def elements(self) -> List[E]:
        return [element for element, _ in self._elements]


    def priorities(self) -> List[P]:
        return [priority for _, priority in self._elements]

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @staticmethod
    def of() -> ColaPrioridad[E, P]:
        return ColaPrioridad()

    def add(self, e: E, priority: P) -> None:
        index = self._index_order(priority)
        self._elements.insert(index, (e, priority))

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)[0]

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def _index_order(self, priority: P) -> int:
        for index, (_, p) in enumerate(self._elements):
            if priority < p:
                return index
        return len(self._elements)

    def decrease_priority(self, e: E, new_priority: P) -> None:
        for index, (element, priority) in enumerate(self._elements):
            if element == e:
                if new_priority < priority:
                    self._priorities[index] = new_priority
                    self._elements.pop(index)
                    self.add(e, new_priority)
                break

    def __str__(self) -> str:
        return f"ColaPrioridad({', '.join([f'({e}, {p})' for e, p in self._elements])})"


    
    
if __name__ == '__main__':
    pass