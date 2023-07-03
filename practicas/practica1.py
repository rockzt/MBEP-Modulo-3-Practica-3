'''
Escribe una función qué reciba varios números y devuelva el mayor de ellos.
'''
def MaxNum(numberList: list):
  print(type(numberList))
  maxNum = max(numberList)
  return f'Número mayor -> {maxNum}'

# Testing Function
print(MaxNum([150, 253, 569628, 0, 6, 10000000000, 20365985]))