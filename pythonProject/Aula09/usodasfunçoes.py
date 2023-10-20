from Aula09.exercicio import acrescentar_elementos, quantidade_elementos, fila_vazia

if __name__ == "__main__":
    # Criar uma fila vazia
    fila = []

    # Adicionar elementos à fila
    acrescentar_elementos(fila, [1, 2, 3, 4, 5])

    # Verificar a quantidade de elementos na fila
    print(f"Quantidade de elementos na fila: {quantidade_elementos(fila)}")

    # Verificar se a fila está vazia ou não
    if fila_vazia(fila):
        print("A fila está vazia.")
    else:
        print("A fila não está vazia.")