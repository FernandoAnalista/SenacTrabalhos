# Defina a classe "Produto"
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Crie um objeto "arroz" a partir da classe "Produto" com o nome "Arroz" e o preço "5.99"
arroz = Produto("Arroz", 5.99)

# Exiba o nome e o preço do objeto "arroz" na tela
print("Nome: ", arroz.nome)
print("Preço: ", arroz.preco)