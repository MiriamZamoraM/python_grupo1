# EJERCICIO NUMERO 3
"""3. Escribe un programa que lea un número entero y determine si es
positivo, negativo o cero."""

print("EJERCICIO NUMERO 3")
print("resolver si el numero es positivo, negativo o cero \n")

numero2=int(input("ingrese numero: "))
if numero2 < 0:
    print("el numero ",numero2,"es negativo \n")
elif numero2 == 0:
    print("el numero ",numero2," es cero \n")
else: 
    print("el numero ",numero2," es positivo \n")