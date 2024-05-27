# EJERCICIO NUMERO 2
"""2. Escribe un programa que solicite al usuario un número entero y calcule
su cuadrado y su cubo."""

print("EJERCICIO NUMERO 2")

print("cuadrado y cubo de un numero \n")

numero1= int(input("ingrese numero entero: " ))

cuadrado1=numero1**2
cuadrado2=pow(numero1,2)
cubo1 =numero1**3
cubo2=pow(numero1,3)
print("resultado 1 del cuadrado de ",numero1," es: ", cuadrado1)
print("resultado 2 del cuadrado de ",numero1," es: ", cuadrado2)
print("resultado 1 de cubo de ",numero1," es: ", cubo1)
print("resultado 2 de cubo de ",numero1," es: ", cubo2,"\n")