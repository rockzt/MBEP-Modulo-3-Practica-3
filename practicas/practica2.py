'''
Escribe una función que permita multiplicar varios números
'''

def muitiplyNumbers(*args):
  result = 1
  for n in args:
      result *=  n

  return f"Reslultado de multiplicar -> {args} - {result}"

# Testing Function
print(muitiplyNumbers(1,5,1))