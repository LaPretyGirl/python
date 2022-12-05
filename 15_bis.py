# Sumar
def sumar_llista(a): 
    sumatori=0
    for i in a : 
        sumatori +=(i*i)
    return sumatori

# Multiplicar
def multiplicar_llista(llista):
    multiplicado = 1
    for x in llista :
        multiplicado *=x
    return multiplicado

# Programa principal
i = [3,2,4]
print("La suma dels elements és: ", sumar_llista(i))
print("La multiplicació és: ", multiplicar_llista(i))