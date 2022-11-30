# Definició de funcions
def longitut(a):
    l = 0
    for i in a:
        l +=1
    return l 

# Aplicació principal
a = input("Introdueix una cadena: ")
b = longitut(a)
print("La longitut ", a, " és ", b)




# Apuntes :)
# a=[1,2,3,[4,5,7],8,9]
# b= "Pere"
# c=len(a)=>6
# d=len(b)=>4
# x=longitut(a)=>6
# y=longitut(b)=>y

