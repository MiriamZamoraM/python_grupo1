# EJERCICIO NUMERO 4
print ("****************************************")
print("EJERCICIO NUMERO 4")
print("el numero es divisible por 3 y 5 \n")
numero3=int(input("ingrese numero: "))
if numero3 % 3 ==0 and numero3 % 5==0:
    print("el numero ",numero3," es divisible por 3 y 5")
else :
    print("el numero ",numero3," no es divisible por 3 ó 5 \n")

print("---------------------")
def es_divisible_por_3_y_5(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False

# Ejemplos de uso
numero = int(input("ingrese numero: "))

if es_divisible_por_3_y_5(numero):
    print(f"{numero} es divisible por 3 y 5 \n")
else:
    print(f"{numero} no es divisible por 3 y 5 \n")