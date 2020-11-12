# Fecha: 11/11/20
# Tema: Lambda
# En Python, las funciones lambda son también conocidas como funciones anónimas
# porque se definen sin un nombre.

# Función para duplicar un número
def doblar_1(numero_1):
   resultado = numero_1*2
   return resultado

numero_1 = doblar_1(2)
print(numero_1)


# Redución líneas
def doblar_2(numero_2): return numero_2*2

numero_2 = doblar_2(3)
print(numero_2)


# Función LAMBDA doblar
doblar = lambda num: num*2
print(doblar(5))


# Función LAMBDA impar

def impar(numero):
    if numero % 2 != 0:
        return "Número Impar"
    else:
        return "Numero Par"

ingresar_num = impar(17)
print(ingresar_num)

impar = lambda numero : numero % 2 != 0
print(impar(5))

revertir = lambda cadena: cadena[::-1]
print(revertir("Antuko"))

sumar = lambda x,y : x + y
print(sumar(3,10))