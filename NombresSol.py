import numpy as np
nombres = [
    'María del Rosario Estupiñan Hernández',
    'Ana Gabriela Martinez Martinez',
    'Gabriela Muñoz Pérez',
    'Claudia González Aguirre',
    'Denise Martínez Garcia',
    'Ana Karenina Macías Flores',
    'Roberta Pulido Díaz',
    'Yolanda Eréndira Ibarra Márquez',
    'Carmen Ochoa Escandón',
    'Josefina Salinas Martínez',
    'Hilda María Bañuelos Cortés',
    'Eunice Romero Garza',
    'María Margadalena Sanchez Sanchez',
    'Ana Carolina Junco Treviño',
    'Paula Ivette Durán Rosas',
    'Sandra Maldonado Barrón',
    'Amparo Armendáriz Ruiz',
    'Nadia Leticia Carranza Téllez',
    'Cinthia Ontiveros Garza'
]
#Lo primero que hago es crear una lista de listas con 2 'columnas', una para nombres y otra para apellidos.
NuevoNombre=[['' for x in range(2)] for y in range(len(nombres))]
#Comienzo el for, en este caso numeronombre nos da el numero del nombre que estamos cambiando.
for nombre in range(len(nombres)):
    #Se divide el nombre
    NombreDiv=nombres[numeronombre].split(' ')
    #Se asignan nombres y apellidos a la columna de nombres y apellidos.
    NuevoNombre[numeronombre][1]=' '.join(NombreDiv[-2:])
    NuevoNombre[numeronombre][0]=' '.join(NombreDiv[:-2])
#Como np array se imprime mas bonito, convierto la salida en ese formato para ver la lista resultante.
print(np.array(NuevoNombre))
