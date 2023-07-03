'''
Escribe una función que genere una lista con los números de la serie de fibonacci. La función debe recibir la cantidad de números a generar
'''
def fibonacciGenerator(numberSize):
  n1, n2 = 0, 1
  count = 0


  if numberSize <= 0:
      print("Debes ingresar un numero positivo")
  elif numberSize == 1:
      print("Secuencia Fibonacci hasta",numberSize,":")
      print(n1)
  else:
    print("Secuencia Fibonacci:")
    while count < numberSize:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


fibonacciGenerator(10)
fibonacciGenerator(7)
fibonacciGenerator(15)
fibonacciGenerator(26)
fibonacciGenerator(88)