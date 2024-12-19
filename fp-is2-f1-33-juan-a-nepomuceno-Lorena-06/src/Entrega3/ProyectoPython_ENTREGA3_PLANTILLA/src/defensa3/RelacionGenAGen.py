'''
Created on 19 dic 2024

@author: loren
'''
from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass

@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1:str
    nombre_gen2:str
    conexion:float 
    
    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> RelacionGenAGen:
        if not (-1 <= conexion <= 1):
            raise ValueError('La conexión debe estar entre -1 y 1')
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)
    
    @staticmethod
    def parse(linea: str) -> RelacionGenAGen:
        partes = linea.split(",")
        nombre_gen1 = partes[0]
        nombre_gen2 = partes[1]
        conexion = float(partes[2])
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, conexion)
    
    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75
    
    @property
    def antiexpresados(self) -> bool:
        return self.conexion < 0.75
    
    def __str__(self):
        return f"{self.nombre_gen1} - {self.nombre_gen2}: {self.conexion}"


if __name__ == '__main__':
    lineas = ["TP53,EGFR,0.8","BRAF,KRAS,0.6","CCND1,MYC,-0.9"]

    for linea in lineas:
        try:
            relacion = RelacionGenAGen.parse(linea)
            print(f"Relación creada: {relacion}")
            print(f"Coexpresados: {relacion.coexpresados}")
            print(f"Antiexpresados: {relacion.antiexpresados}")
            print("-" * 50)
        except ValueError as e:
            print(f"Error: {e}")
            