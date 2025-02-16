#Imprimir números pares del 0 al 10

##FORMA 1
#for i in range(11):
#    if i % 2 == 0:
#        print(f'Valor: {i}')
#else:
#    print("Fin del Ciclo")

#FORMA 2
for i in range(11):
    if i % 2 != 0:
        continue
    print (f'Valor: {i}')
else:
    print ("Fin del Ciclo")
