from sys import path

print(path)
path.append('/Users/davidhdz/Documents/Github/pruebas/Modulos')
#path.append('C:\\Users\\user\\py\\modules') Windows 
print('\n')
print(path)

from modulo1 import sumalist, prodlist

print("La suma de la lista: ", [1,2,3,4,5], "es :", sumalist([1,2,3,4,5]))

print("El producto de la lista: ", [1,2,3,4,5], "es :", prodlist([1,2,3,4,5]))

