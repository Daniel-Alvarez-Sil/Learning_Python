iNum = int(input("Ingresa un número entre 1 y 3: "))

cTexto = ""

if iNum == 1:
    cTexto = "Número Uno"
elif iNum == 2:
    cTexto = "Número Dos"
elif iNum == 3:
    cTexto = "Número Tres"
else:
    cTexto = "Valor Fuera de Rango"

print (f''' 
    
    Valor propocionado: {iNum} 
                        {cTexto}       
        
        ''')