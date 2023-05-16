# Ejemplo de un diccionario sencillo:
estudiante = {'Nombre': 'Jaimito'}
# Se imprime el diccionario
print(estudiante)
# Ejemplo de un diccionario complejo:
estudiante = {
    'Nombre': 'Jaimito',
    'Edad': 18,
    'Notas': [7, 8, 5, 6, 7],
    'Familia':
        {
            'Pablo':
                {
                    'Relación': 'Padre',
                    'Edad': 50
                }
        }
}
# Se imprime el diccionario
print(estudiante)
# Se añade una nueva clave y valor "pais" (agregar)
estudiante['País'] = 'España'
# Se imprime el diccionario
print(estudiante)
# Se cambiar el valor de la clave "Nombre" (editar)
estudiante['Nombre'] = 'diego'
# Se busca el valor de "Nombre" (buscar)
print(estudiante['Nombre'])
# Se eliminar el valor de "Familia" (eliminar)
del estudiante["Familia"]
# Se imprime el diccionario
print(estudiante)
# Devuelve el valor de todas las claves
print(estudiante.keys())
# Devuelve una vista de los valores del diccionario.
print(estudiante.values())
# Devuelve una vista de pares (clave, valor) del diccionario.
print(estudiante.items())