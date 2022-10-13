# b = "Hola"
from typing import final


try:
    print(b)

except NameError:
    print("la variable b no esta definida")


try:
    print(5/0)
except ZeroDivisionError:
    print("no es posible dividir por 0")


try:
    print("{0} va a arrojar un error {1}".format(25))
except IndexError:
    print("Debe proveer al menos dos valores")


try:
    # raise Exception("El error ocurrio porque el programador lo quiso asi", " Corrigelo hablando con el administrador")
    pass
except Exception as e:
    print("Hubo un error voluntariamente")
    print(e.args)
    valor1, valor2 = e.args
    print("El error es: {0}".format(valor1))
    print("la solución es: ", valor2)
finally:
    print("Ya salimos del bloque try except")

