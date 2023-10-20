class Cachorro:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def latir(self):
        return "O cachorro latiu"

    def comer(self):
        return "O cachorro comeu"


def main():
    nome = input("Digite o nome do cachorro: ")
    data_nascimento = input("Digite a data de nascimento do cachorro: ")

    cachorro = Cachorro(nome, data_nascimento)
#continua
while True:
        print("\nEscolha uma ação para o cachorro:")
        print("1 - Latir")
        print("2 - Comer")
        print("3 - Exibir informações do cachorro")
        print("4 - Sair")

        escolha = input("Digite o número da ação desejada: ")

        if escolha == "1":
            print(cachorro.latir())
        elif escolha == "2":
            print(cachorro.comer())
        elif escolha == "3":
            print(f"Nome: {cachorro.nome}")
            print(f"Data de Nascimento: {cachorro.data_nascimento}")
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()