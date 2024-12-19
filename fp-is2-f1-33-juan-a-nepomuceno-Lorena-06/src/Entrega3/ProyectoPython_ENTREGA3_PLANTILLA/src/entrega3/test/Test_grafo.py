'''
Created on 17 nov 2024

@author: belen
'''
from Entrega3.ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Red_social import Red_social
from us.lsi.tools.File import absolute_path


if __name__ == '__main__':
    rrs: Red_social = Red_social.parse(absolute_path('Entrega3/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/usuarios.txt'), absolute_path('Entrega3/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/relaciones.txt'))
    
    sep = '\n'
    print("************** Nº Predecesores de cada vértice")
    print(sep.join(f'{v} -- {len(rrs.predecessors(v))}'  for v in rrs.vertex_set()))

    print("\n************** Nº Vecinos de cada vértice")
    print(sep.join(f'{v} -- {len(rrs.neighbors(v))}'  for v in rrs.vertex_set()))
    