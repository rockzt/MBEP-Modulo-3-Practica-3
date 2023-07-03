'''
Escribe un programa que emule el funcionamiento de una calculadora simple.
'''

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Selecciona una opreacion.")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")

while True:

    choice = input("Elige una opción(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ingresa primer digito: "))
            num2 = float(input("Ingresa segundo digito: "))
        except ValueError:
            print("Número no valido, ingresa un digito válido.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Quieres hacer un nuevo calculo? (s/n): ")
        if next_calculation == "n":
          break
    else:
        print("Invalid Input")