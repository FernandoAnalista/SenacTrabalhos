class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            print("Nome inválido. O nome não foi alterado.")

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if len(novo_cpf) == 11:
            self.__cpf = novo_cpf
        else:
            print("CPF inválido. O CPF não foi alterado.")

    def __str__(self):
        return f'Nome: {self.__nome}, CPF: {self.__cpf}'

# Demonstração
pessoa = Pessoa("Alice", "12345678901")

print(pessoa)  # Imprimir os valores iniciais

# Alterando o nome e CPF usando os métodos de acesso
pessoa.nome = "Bob"
pessoa.cpf = "98765432109"

print(pessoa)  # Imprimir os novos valores

# Tentar definir um nome vazio e um CPF com comprimento inválido
pessoa.nome = ""
pessoa.cpf = "12345"

print(pessoa)  # Imprimir os valores após as tentativas inválidas

    