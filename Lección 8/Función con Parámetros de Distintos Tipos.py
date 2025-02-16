def imprimeColeccion (cS):
    for c in cS:
        print(c, end = " ")

print(f'Impresión de Lista: ', end = "")
imprimeColeccion(["Daniel", "Gabriela", "Guillermo"])
print(f'\nImpresión de Tupla: ', end = "")
imprimeColeccion(("Mariana", "Pablo", "Arturo"))
print(f'\nImpresión de SET (Conjunto): ', end = "")
imprimeColeccion({"Julio", "Carlos", "Demetrio"})