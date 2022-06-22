def triangulo():
    base = float(input('Introduce la base del triangulo'))
    altura = float(input('Introduce la base del triangulo'))
    areaTriangulo = base*altura/2
    print('El area del triangulo es ', areaTriangulo)

triangulo()

def circulo():
    radio = float(input('Introduce el radio del circulo'))
    pi = 3.14
    areaCirculo = pi*radio**2
    print('El area del circulo es ', areaCirculo)

circulo()

def numeroEven():
    numero = int(input('Introduce un numero entero'))
    if numero % 2 == 0:
        print('El numero ', numero, ' es primo')
    else: print('El numero ', numero, ' no es primo')

numeroEven()

def añoBisiesto():
    año = int(input('Escribe el año para saber si es bisiesto'))
    if año % 4 != 0:
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 != 0:
        print("Es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        print("Es bisiesto")

añoBisiesto()