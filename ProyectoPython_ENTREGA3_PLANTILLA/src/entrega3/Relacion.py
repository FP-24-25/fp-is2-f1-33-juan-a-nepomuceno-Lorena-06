'''
Created on 17 nov 2024

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Relacion:
    interacciones: int
    dias_activa: int
    id: int  # Atributo que representa el identificador único de la relación

    # Variable estática para generar identificadores únicos
    __xx_num: int = 0
    
    @staticmethod
    def of(interacciones: int, dias_activa: int)->Relacion:
        Relacion.__xx_num+=1 # De esta manera creamos identificadores únicos
        return Relacion(interacciones, dias_activa, Relacion.__xx_num)  # Devuelve la nueva instancia con el id único
    
    def __str__(self):
        return f"Relacion ID: {self.id}, Interacciones: {self.interacciones}, Días Activa: {self.dias_activa}"
    

if __name__ == '__main__':
    pass