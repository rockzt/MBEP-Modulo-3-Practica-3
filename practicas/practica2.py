'''
Escribe una función que permita multiplicar varios números
'''

def muitiplyNumbers(numbers: list):
  result = 1
  for n in numbers:
      result = result * n

  return f"Reslultado de multiplicar -> {numbers} - {result}"

# Testing Function
print(muitiplyNumbers([1, 5, 1]))