'''
Escribe una función qué reciba varios números y devuelva el mayor de ellos.
'''
def get_max_number(*args):
  return f'Número mayor -> {max(args)}'

# Testing Function
print(get_max_number(10,250,300,4000000,50))