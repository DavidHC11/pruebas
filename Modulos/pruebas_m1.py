import modulo1
from modulo1 import sumalist, prodlist

print("La variable a es: ",modulo1.a)
print("La variable b es: ",modulo1.b)

x = modulo1.a + modulo1.b
print("El valor de x es: ",x)

print("Actualizando el valor de a en el modulo1",modulo1.a + 10)


print("La suma de la lista: ", [1,2,3,4,5], "es :", sumalist([1,2,3,4,5]))

print("El producto de la lista: ", [1,2,3,4,5], "es :", prodlist([1,2,3,4,5]))

