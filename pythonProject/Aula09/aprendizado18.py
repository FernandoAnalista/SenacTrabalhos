# classe

class Dog:
    def __init__(self, nome, data_nascimento):
        self.nome = str(nome)
        self.data_nascimento = str(data_nascimento)


    def latir(self):
        print(f"O cachorro {self.nome} latiu")

    def comer(self):
        print("O cachorro comeu {self.data_nascimento}")

dog1 = Dog('Mel', '25/10/2020')

dog1.latir()
dog1.comer()


