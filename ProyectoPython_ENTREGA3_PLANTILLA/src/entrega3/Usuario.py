'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
import re


@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date

    @staticmethod
    def of(dni:str, nombre:str, apellidos:str, fecha_nacimiento:date) -> Usuario:
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    
    @staticmethod
    def parse(linea:str) -> Usuario:
        """Parses a CSV string into a Usuario object."""
        # Usamos una expresión regular para validar y extraer los datos
        regex = r"^(\d{8}[A-Za-z]),([^,]+),([^,]+),(\d{4}-\d{2}-\d{2})$"
        match = re.match(regex, linea)
        
        if match:
            dni = match.group(1)
            nombre = match.group(2)
            apellidos = match.group(3)
            fecha_nacimiento = datetime.strptime(match.group(4), "%Y-%m-%d").date()
            return Usuario.of(dni, nombre, apellidos, fecha_nacimiento)
        else:
            raise ValueError(f"Formato inválido para la línea: {linea}")

        
    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellidos}, DNI: {self.dni}"
    
if __name__ == '__main__':
    linea:str = "45718832U,Carlos,Lopez,1984-01-14"
    usuario: Usuario = Usuario.parse(linea)
    print(usuario)