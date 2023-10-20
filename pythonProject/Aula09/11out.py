tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla2 = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

tupla_resultado = ()

for i in range(10):
    resultado = tupla1[i] * tupla2[i]
    tupla_resultado += (resultado,)

print("Tupla Resultado:", tupla_resultado)