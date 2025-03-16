from Estudiantes import Estudiante
from CalculadoraNotas import CalcularNotas


diccionarioEstudiantes = dict()

id_estudiante = 1
while True:
    opcion = input("1. Agregar estudiante\n0. No agregar mas\nSelecciona 1 o 0: ")
    if opcion == "1":
        nombre = input("Digite el nombre del estudiante: ")
        apellido = input("Digite el apellido del estudiante: ")
        identificacion = input("Digite el numero de identificacion: ")
        notas = [2.8, 3.9, 4.5, 4.0]
        estudiante = Estudiante(nombre, apellido, identificacion, notas)
        diccionarioEstudiantes[id_estudiante] = estudiante
        id_estudiante += 1
    else:
        break

buscar_estudiante = input("Digite la cedula a buscar: ")
for estudiante in diccionarioEstudiantes.values():
    if estudiante.identificacion == buscar_estudiante:
        print(f"Las notas de {estudiante.nombre} son: {estudiante.notas}")
        calcular_notas_estudiante = CalcularNotas(estudiante.notas)
        calcular_notas_estudiante.promedioNotas()#no retorna


"""
print(diccionarioEstudiantes[1].nombre)
print(f"Las notas de {diccionarioEstudiantes[2].nombre} son: {diccionarioEstudiantes[2].notas}")
"""

"""
estudiante1 = Estudiante("Diego", "Pachon", "1073333260", [2.8, 3.9, 4.5, 4.0])
estudiante2 = Estudiante("Pedro", "Ramos", "1078883260", [2.8, 3.9, 4.5, 4.0])
estudiante3 = Estudiante("Yasmi", "Cabezas", "1079993260", [2.8, 3.9, 4.5, 4.0])
estudiante4 = Estudiante("Carlos", "Gomez", "1071113260", [2.8, 3.9, 4.5, 4.0])
print(estudiante1.nombre)
print(estudiante3.nombre, "sus notas son: ", estudiante3.notas)

estudiante3.asistir_clase("09-03-2025", True)
print(estudiante3.enviar_tarea("Actividad S5"))

calcularNotaEstudiante3 = CalcularNotas(estudiante3.notas)
calcularNotaEstudiante3.promedioNotas()
calcularNotaEstudiante3.nota_mas_baja()
calcularNotaEstudiante3.nota_mas_alta()"

"""