print("---------------------------")
print("TP COMPLEM 16")
print("----------------------------")

A = int(input("Inngrese A: "))
B = int(input("Inngrese B: "))
C = int(input("Inngrese C: "))

print("Salida: ")

if A>B:
    if A>C:
        if B>C:
            print(A,B,C)
        else:
            print(A,C,B)
    else:
        print(C,A,B)         
else:
    if B>C: 
        if A>C:
            print(B,A,C)
        else:
            print(B,C,A)
    else:
        print(C,B,A)
