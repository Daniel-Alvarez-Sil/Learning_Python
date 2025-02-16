def imprimirNombres (*nombres):
    for c in nombres:
        print(c, end = " ")

print("Primera ronda de valores: ", end = "")
imprimirNombres("Daniel", "Gael", "Andres", "Andy")
print("\nSegunda ronda de valores: ", end = "")
imprimirNombres("Pedro", "Pablo", "Juan", "Mateo", "Marcos")