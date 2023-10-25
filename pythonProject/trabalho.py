class Entrevista:
    def __init__(self, idade, cidade, estado, salario, escolaridade):
        self.idade = str(idade)
        self.cidade = str(cidade)
        self.estado = str(estado)
        self.salario = float(salario)
        self.escolaridade = str(escolaridade)

    def mostraEntrevista(self):
        print(
            f'Idade: {self.idade}, cidade: {self.cidade}, estado: {self.estado}, escolaridade: {self.escolaridade}')




  
Entrevistado1 = Entrevista('20', 'São Paulo', "SP", 2.500, 'Cursando Administração')
Entrevistado2 = Entrevista('32', 'São Bernardo', "SP",  2.500, 'Cursando Engenharia')
Entrevistado3 = Entrevista('20', 'São Paulo', "SP",  2.500, 'Cursando Ciência da computação')
print()
Entrevistado1.mostraEntrevista()
Entrevistado2.mostraEntrevista()
Entrevistado3.mostraEntrevista()

print()