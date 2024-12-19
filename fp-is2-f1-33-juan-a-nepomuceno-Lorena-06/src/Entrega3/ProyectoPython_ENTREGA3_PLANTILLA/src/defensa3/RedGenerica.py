'''
Created on 19 dic 2024

@author: loren
'''
from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.E_grafo import E_grafo,Graph_type,Traverse_type
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.defensa3.Gen import Gen
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.defensa3.RelacionGenAGen import RelacionGenAGen
from us.lsi.tools.File import lineas_de_fichero


V = TypeVar('V')
E = TypeVar('E')

class RedGenica(E_grafo[Gen, RelacionGenAGen]):
    def __init__(self, graph_type: Graph_type, traverse_type: Traverse_type) -> None:
        super().__init__(graph_type, lambda r: r.conexion, traverse_type)
        self.genes_por_nombre: dict[str, Gen] = {}

    @staticmethod
    def of() -> RedGenica:
        return RedGenica(Graph_type.UNDIRECTED, Traverse_type.FORWARD)
    
    @staticmethod
    def parse(f1: str, f2: str) -> RedGenica:

        red = RedGenica.of()

        genes = lineas_de_fichero(f1)
        for linea in genes: #leo los genes del primer archivo
            gen = Gen.parse(linea.strip())
            red.genes_por_nombre[gen.nombre] = gen
            red.add_vertex(gen)

        relaciones = lineas_de_fichero(f2)
        for linea in relaciones: #leo los genes del segundo archivo
            relacion = RelacionGenAGen.parse(linea.strip())
            gen1 = red.genes_por_nombre.get(relacion.nombre_gen1)
            gen2 = red.genes_por_nombre.get(relacion.nombre_gen2)

            if gen1 and gen2:
                red.add_edge(gen1, gen2, relacion)

        return red

    def __str__(self):
        sep = "\n"
        Vertices = sep.join(str(v) for v in self.vertex_list())
        Aristas = sep.join(str(e) for e in self.edge_set())
        return f"Vertices:\n{Vertices}\nAristas:\n{Aristas}"
                
if __name__ == '__main__':
        
    try:
        red_genica = RedGenica.parse(('../resources/genes.txt'),('../resources/red_genes.txt'))

        print("\nRed Génica:")
        print(red_genica)

    except Exception as e:
        print(f"Error: {e}")