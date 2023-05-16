# los sets son no ordenados y sin índices, por lo que no podemos acceder a un elemento por su posición.
# También son no modificables,
# por lo que al contrario que en las listas, una vez hemos añadido un nuevo elemento no podemos cambiar su valor.
# Tampoco admiten elementos repetidos.

# Creamos Un set/conjunto de estudiantes
estudiantes = {'Jaimito', 'Juan', 'Carla', 'Valeria', 'Irene'}
# Se imprime el set
print(estudiantes)
# Se Agrega un nuevo estudiante (agregar
estudiantes.add('Paco')
# Se imprime el set
print(estudiantes)
# Se elimina un  estudiante (eliminar)
estudiantes.remove('Juan')
# Se imprime el set
print(estudiantes)
# Saber si un elemento esta en el set (buscar)
print('Jaimito' in estudiantes)
