# Else --> Y si no es verdad?
# Ejecutar ejercio x ejercicio

print("Verificar edad")

edad_usuario = int(input("Ingresar edad: "))

if edad_usuario < 18:
    print("No puede pasar")
if edad_usuario > 100:
        print("Edad incorrecta")
else:
    print("Puedes pasar")
print("El programa finalizó")


print("Verificar edad")

nota = float(input("Ingresar nota: "))

if nota < 5:
    print("Insuficiente")
elif nota < 13:
        print("Aprobado")
elif nota < 17:
    print("Bien")
elif nota < 19:
    print("Notable")
else:
    print("Sobresaliente")

#Ejercicio 1:
#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.

pri_num = int(input("Ingresar primer número: "))
seg_num = int(input("Ingresar segundo número: "))

def DevuelveMax(num1, num2):
    if pri_num > seg_num:
        return pri_num
    elif seg_num > pri_num:
        return seg_num
    else:
        mensaje = "Son iguales"
        return mensaje

#pri_num = int(input("Ingresar primer número: "))
#seg_num = int(input("Ingresar segundo número: "))
print(f'Número mayor es {DevuelveMax(pri_num, seg_num)}')

#Ejercicio 2:
#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

nombre = input("Ingresar nombre: ")
direccion = input("Ingresar dirección: ")
telefono = input("Ingresar teléfono: ")

datos_personales = [nombre, direccion, telefono]
print('Los datos personales son: ' + datos_personales[0]
                             + ' ' + datos_personales[1]
                             + ' ' + datos_personales[2])


#Ejercicio 3:
#Crea un programa que pida tres números por teclado. El programa imprime en consola
#la media aritmética de los números introducidos

num1 = int(input("Ingresar primer número: "))
num2 = int(input("Ingresar segundo número: "))
num3 = int(input("Ingresar tercer número: "))

def promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

print(f'El promedio es: {promedio(num1, num2, num3)}')