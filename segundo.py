# print("Hola mundo")
# print("Hola")


# import matplotlib
# import matplotlib.pyplot as plt

def sum(x, y):
    """esta función suma dos números"""
    return x + y

# print(sum(7, 3))
# print(sum(22, 1))
# print(sum(1, 5))
# print(sum(1, 1))

xCuadrado = lambda x: x**2
# print(xCuadrado(9))

def multiplicar(x=5, y=7):
    """Esta función sirve para multiplicar"""
    return x * y

# print(multiplicar(y = 1))


mi_string = "Hola mundo"
mi2_string = "Chao Mundo"

mis_string_juntos = mi_string + mi2_string

print(mis_string_juntos)

print("{0} como estan {1}".format(mi_string, mi2_string))
print(f"{mi_string} que estan haciendo {mi2_string}" )