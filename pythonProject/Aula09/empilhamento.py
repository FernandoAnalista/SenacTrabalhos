def criar_pilha():
    return []
def acrescentar_elementos(pilha, elementos):
    pilha.extend(elementos)

def verificar_quantidade(pilha):
    return len(pilha)

def verificar_se_vazia(pilha):
    return len(pilha) == 0

if __name__ == "__main__":
    pilha = criar_pilha()
    elementos = [1, 2, 3, 4, 5]

    acrescentar_elementos(pilha, elementos)

    quantidade_elementos = verificar_quantidade(pilha)
    if verificar_se_vazia(pilha):
        print("A pilha está vazia.")
    else:
        print("A pilha não está vazia.")
        print(f"Quantidade de elementos na pilha: {quantidade_elementos}")