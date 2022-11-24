# Definició de funcions
def gran(z,e):
    a=z
    if (z>e): # Si entra sabem que x és major que y
        print(z, "Es major que", e)
    elif(e>z):
        print(e, "Es major que", z)
        a=e
    else:
        print(z, "és igual que", e)
    return a

# Aplciació principal
a = int(input("Primer número "))
b = int(input("Segundo número "))
c = gran(a,b)
print("El major de ", a, " i ",b, " és ", c)
