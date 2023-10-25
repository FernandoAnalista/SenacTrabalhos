class Pesquisa:
    def __init__(self, nome):
        self.nome = nome
        self.listaEntrevistados = []

    def adicionarEntrevistado(self, entrevistado):
        self.listaEntrevistados.append(entrevistado)

    def imprimirEntrevistados(self):
        for entrevistado in self.listaEntrevistados:
            entrevistado.imprimirDados()

class Entrevistado:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimirDados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Criar a pesquisa
pesquisa = Pesquisa("Pesquisa de Opinião")

# Criar e adicionar entrevistados à pesquisa
entrevistado1 = Entrevistado("Alice", 30)
entrevistado2 = Entrevistado("Bob", 25)
pesquisa.adicionarEntrevistado(entrevistado1)
pesquisa.adicionarEntrevistado(entrevistado2)

# Imprimir os dados dos entrevistados na pesquisa
pesquisa.imprimirEntrevistados()