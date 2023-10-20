
fila = []

def acrescentar_elementos(fila, elementos):
    fila.extend(elementos)

def quantidade_elementos(fila):
    return len(fila)

def fila_vazia(fila):
    return len(fila) == 0

if __name__ == "__main__":

    acrescentar_elementos(fila, [1, 2, 3, 4, 5])


    print(f"Quantidade de elementos na fila: {quantidade_elementos(fila)}")


    if fila_vazia(fila):
        print("A fila está vazia.")
    else:
        print("A fila não está vazia.")