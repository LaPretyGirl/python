# Definició de funcions
def gran_de_tres(a,b,c):
    d=a
    if (a>b): # a>b
        if(c>a): # a>b and a>c
            d=c 
        elif(c>a): # a>b and c>a => c és el major
            d=c
        else: # Aquí a=c>b => a,c són els majors
            d=b
    elif(b>a): # b>a
        if(b>c): # b>a and b>c => y és el major
            d=b
        elif(c>b): # b>a and c>b => c és el major
            d=c
        else: # Aquí b>a and c=b => c,b són els majors
            d=b
    else: # a=b
        if(a>c): # a=b and a>c => a,b són els majors
            d=a
        elif(c>a): # a=b and c=a => c és el major
            d=c
        else: # a=b=c => a,b,c són iguals
            d=a
    
    return d

# Aplciació principal
a = int(input("Escriure el primer valor: "))
b = int(input("Escriure el segon valor "))
c = int(input("Escriure el tercer valor "))
d = gran_de_tres(a,b,c)
print("El major de ", a, " , ",b, " i ",c," és ", d)