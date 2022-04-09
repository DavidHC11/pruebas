if __name__ == "__main__":
    print("Estoy en el principal")
else:
    print("Estoy en el modulo", __name__)

counter = 10
hola = "hola mundo"

def sumalista(lista = [1,2,3,4,5]):
    suma = 0
    for x in lista:
        suma+=x

    return suma


