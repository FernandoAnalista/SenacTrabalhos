class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

nome = input("Digite o nome do aluno: ")
idade = int(input(" Digite a idade do aluno: "))
matricula = input("Digite a matricula do aluno: ")
meu_aluno = Aluno(nome, idade, matricula)

print("\nDados do aluno cadastro: ")
print("Nome: ", meu_aluno.nome)
print("Idade: ", meu_aluno.idade)
print("Matricula: ", meu_aluno.matricula)
