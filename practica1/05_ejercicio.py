# EJERCICIO NUMERO 5
print ("**************************************** ")
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