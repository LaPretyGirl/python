print ("menú: \n")
print ("1. Suma ") 
print ("2. Resta ")
print ("3. Multiplicació ")
print ("4. Divisió ")
print ("0. Sortida \n")
opcio = input("Seleccioni l'opció que vulgui: ")
a = input("Indiqui el primer operand: ")
b = input("Indiqui el segon operand: ")
match opcio:
    case "1":
        c=int(a)+int(b)
        print("La suma de ",a," més ",b," és ",c)
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menos ",b," és ",c)
    case "3":
        c=int(a)*int(b)
        print("La multiplicació de ",a," per ",b," és ",c)
    case "4":
        c=int(a)/int(b)
        print("La divisió de ",a," dividid ",b," és ",c)
    case "0":
        print("Adeú")
    case other:
        print("Opció no vàlida!")
        