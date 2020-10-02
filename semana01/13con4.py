#distancia = int(input("Indicar distancia en Km: "))
#hermanos = int(input("Inducar números de hermanos: "))
#salario = int(input("Indicar salarios familiar anual: "))

def obtener_beca(km, her, sal):
    if km >= 40 and her > 2 or sal <= 20000:
        print("Obtienes beca")
    else:
        print("No calificas para la beca")

#obtener_beca(distancia, hermanos, salario)


print("--Asignaturas Optativa--")
print("Seleccionar asignaturas: SQL, Access, MySql")
#print("1 , para 'Historia de la Programación'")
#print("2 , para 'Pruebas de software'")
#print("3 , para 'Usabilidad y Accesibilida'")
print(" ")
curso = input("Ingresar opción: ")
asignatura = curso.lower()

if asignatura in ("sql", "access", "mysql"):
    print("Asinatura elegida " + asignatura )
else:
    print("La asignaturo no se encuentra registrada")