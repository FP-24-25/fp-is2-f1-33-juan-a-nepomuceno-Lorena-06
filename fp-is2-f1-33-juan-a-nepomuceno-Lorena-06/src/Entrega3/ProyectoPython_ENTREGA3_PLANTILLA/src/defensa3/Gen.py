'''
Created on 19 dic 2024

@author: loren
'''
from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass
from us.lsi.tools.GraphicsMaps import tipo

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> Gen:
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual que cero")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(linea: str) -> Gen:
        partes = linea.split(",")
        nombre = partes[0]
        tipo = partes[1]
        num_mutaciones = int(partes[2])
        loc_cromosoma = partes[3]
        return Gen.of(nombre, tipo, num_mutaciones, loc_cromosoma)

    def __str__(self):
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosoma})"

if __name__ == '__main__':
    # Ejemplo de línea de texto para crear un Gen
    linea = "TP53,supresor tumoral,256,17p13.1"
    linea_mal = "TP53,supresor tumoral,-256,17p13.1"
    
    try:
        gen = Gen.parse(linea)
        print("Gen creado correctamente:")
        print(gen)
    except ValueError as e:
        print(f"Error: {e}")
        
    try:
        gen = Gen.parse(linea_mal)
        print("Gen creado correctamente:")
        print(gen)
    except ValueError as e:
        print(f"Error: {e}") 
