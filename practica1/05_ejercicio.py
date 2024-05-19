# EJERCICIO NUMERO 5
"""5. Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F"""

print("EJERCICIO NUMERO 5 \n")
print("Calificacion numerica A,B,C,D,F \n")
nota = int(input("ingrese nota: "))

if nota <= 100 and nota >=90 :
    print("calificacion es 'A' \n")
elif nota < 90 and nota >=80 :
    print("calificacion es 'B' \n ")
elif nota < 80 and nota >=70 :
    print("calificacion es 'C' \n")
elif nota < 70 and nota >=60 :
    print("calificacion es 'D' \n")
elif nota < 60 and nota >=0 :
    print("calificacion es 'F' \n")
else: 
    print("el numero ingresado no es valido \n")