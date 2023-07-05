'''
Escribe una función que permita identificar si un número dado es primo o no.
'''
def checkPrimeNumber(num):
 if num < 2:
   return False
 for i in range(2, num):
   if num % i == 0:
    return False
 return True

#Testing Function
print(checkPrimeNumber(10))
print(checkPrimeNumber(9))
print(checkPrimeNumber(100))
print(checkPrimeNumber(50))
print(checkPrimeNumber(7))
print(checkPrimeNumber(1))
print(checkPrimeNumber(5))
print(checkPrimeNumber(35))