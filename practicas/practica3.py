'''
Escribe una función para verificar que un número se encuentra en un rango de números determinado. El resultado de esa función debe ser booleano
'''
def checkNumberRange(number):

  if number in range(1, 1000):
    return True
  else:
    return False

# Testing Function
print(checkNumberRange(999))
print(checkNumberRange(1))
print(checkNumberRange(343))
print(checkNumberRange(1000))
print(checkNumberRange(0))