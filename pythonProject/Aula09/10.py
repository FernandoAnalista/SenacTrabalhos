def inserenaFila(fila, elemento):
        return fila.append(elemento)

def retiradaFila(fila):
        return fila.pop(0)


fila = []

for i in range(1, 10):
        inserenaFila(fila, i)

print(fila)
print(retiradaFila(fila))