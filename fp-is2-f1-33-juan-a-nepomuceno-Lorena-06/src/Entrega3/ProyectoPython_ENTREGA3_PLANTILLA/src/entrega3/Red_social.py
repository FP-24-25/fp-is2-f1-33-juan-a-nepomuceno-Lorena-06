'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Usuario import Usuario
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Relacion import Relacion
from us.lsi.tools.File import lineas_de_fichero
from datetime import datetime


class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self,graph_type:Graph_type,traverse_type:Traverse_type) -> None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = {}
        
    
    @staticmethod
    def of(graph_type: Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social:
        return Red_social(graph_type, traverse_type)
        
    
    @staticmethod
    def parse(f1:str, f2:str, graph_type:Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social:
        usuarios = lineas_de_fichero(f1)
        relaciones = lineas_de_fichero(f2)
        
        # Crear la instancia de Red_social
        red_social = Red_social(graph_type, traverse_type)
        
        # Agregar los usuarios
        for linea in usuarios:
            dni, nombre, apellidos, fecha_nacimiento = linea.split(",")
            usuario = Usuario(dni, nombre, apellidos, datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date())
            #usuario = Usuario.parse(linea)
            red_social._Red_social__usuarios_dni[dni] = usuario
            #red_social.__usuarios_dni[dni] = usuario
            red_social.add_vertex(usuario)  # Añadir el usuario como vértice al grafo

        # Agregar las relaciones
        for linea in relaciones:
            dni1, dni2, interacciones, dias_activa = linea.split(",")
            interacciones = int(interacciones)
            dias_activa = int(dias_activa)
            relacion = Relacion.of(interacciones, dias_activa)
            #usuario1 = red_social._Red_social__usuarios_dni.get(dni1)
            #usuario2 = red_social._Red_social__usuarios_dni.get(dni2)
            usuario1 = red_social.__usuarios_dni[dni1]
            usuario2 = red_social.__usuarios_dni[dni2]
            red_social.add_edge(usuario1, usuario2, relacion)  # Añadir relación como arista
        return red_social

    @property
    def usuarios_dni(self)->dict[str,Usuario]:
        return self.__usuarios_dni



if __name__ == '__main__':
    # 
    rrss: Red_social = Red_social.parse(('../resources/usuarios.txt'),('../resources/relaciones.txt')) #'resources/usuarios.txt', 'resources/relaciones.txt')
    print(rrss.plot_graph())