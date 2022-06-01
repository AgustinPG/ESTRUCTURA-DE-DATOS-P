def factorial(numero):
    if numero>1:
        numero=numero*factorial(numero-1)
    return numero

print("El factorial:",factorial(5))