# NOTA: No existe cómo tal la función unZIP, pero podemos usar otros métodos para simular dicha función

mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]

print(*mezcla)
print(list(zip(*mezcla))) # zip(*mezcla) = unzip(mezcla)