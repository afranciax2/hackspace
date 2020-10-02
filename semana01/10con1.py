# Condiciones: IF

# Función evaluación, en función de la nota alumno aprobado o desaprobado
"""
def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Desaprobado"
    return valoracion

print(evaluacion(4))
"""

# Programa con ingresos de datos
print("Programa de evaluación de notas")
nota_alumno = int(input("Ingresar nota: "))

def evaluacion(nota):
    valoracion = "Aprobado"
    if nota <= 5:
        valoracion = "Desaprobado"
    return valoracion

print(evaluacion(nota_alumno))