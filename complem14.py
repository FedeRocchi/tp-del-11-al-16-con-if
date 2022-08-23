print("--------------------")
print("TP COMPLEM 14")
print("---------------------")


print("Ingrese valores: ")

NUM = int(input())
V = int(input("Ingrese V: "))

Funcion = {
    1 : 100*V,
    2 : 100**V,
    3 : 100/V
    }       

VAL = Funcion.get(NUM, 0)

print(VAL)