glossario = {
    "variável": "Um local na memória que armazena dados.",
    "função": "Um bloco de código que realiza uma tarefa específica quando chamado.",
    "loop": "Uma estrutura de controle que permite executar um bloco de código repetidamente.",
    "condicional": "Uma estrutura de controle que permite tomar decisões com base em condições.",
    "lista": "Uma coleção ordenada de elementos."
}

palavra_buscada = input("Digite uma palavra relacionada à programação para buscar em seu glossário: ")

if palavra_buscada in glossario:
    significado = glossario[palavra_buscada]
    print(f"O significado de '{palavra_buscada}' é: {significado}")
else:
    print(f"A palavra '{palavra_buscada}' não foi encontrada no glossário.")