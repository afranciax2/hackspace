def suma (a, b):
    return a + b


def operacion(funcion, a, b):
    return funcion(a, b)


funcion_suma = suma
resultado = operacion(funcion_suma, 10, 2)

#print(resultado)


def operacion():
    def suma(a, b):
        return a + b
    
    return suma

resultado = operacion()(10,20)
#print(resultado)


# Funciones anidadas
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        nonlocal b

        c = 'c'
        print(b)
        b = 'Cambios de valor'
        
    funcion_anidada()
    print(b)

#funcion = funcion_principal()
#print(funcion)

def saludar_usuario(username):
    mensaje = 'Hola ' + username

    def saludar():
        print(mensaje)
    
    return saludar


hola = saludar_usuario('Fibeth')
hola()

#En este caso nuestra función saludar_usuario no es más que un closure,
# una función la cual crea a su vez a otra de forma dinámica.
# Esta nueva función tiene memoria, siendo capaz de recordar,
# y utilizar, las variables lo locales y no locales definidas previamente.