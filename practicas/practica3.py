'''
Escribe una función para verificar que un número se encuentra en un rango de números determinado. El resultado de esa función debe ser booleano
'''
def checkNumberRange(min_number, max_number, number):
    return number in range(min_number, max_number)

# Testing Function
print(checkNumberRange(1,10,5))
print(checkNumberRange(1,10,20))