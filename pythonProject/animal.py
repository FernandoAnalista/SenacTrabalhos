# Defina a classe "Animal"
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"O {self.nome} faz algum som")

# Crie um objeto "animal" a partir da classe "Animal" e defina um nome para ele
animal = Animal("Garfield")

# Chame o método "falar" do objeto "animal" para exibir a mensagem com o som do animal
animal.falar()