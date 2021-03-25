num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("multiplo de 2")
elif num % 3  == 0:
    print("multiplo de 3")
elif num % 5 == 0:
    print("multiplo de 5")
else:
    print("No es multiplo ni de 2, 3 o 5")
