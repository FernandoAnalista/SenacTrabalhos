class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f'{self.nome}, {self.idade} anos'

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.moradores = []
        
    def adicionar_morador(self, pessoa):
        self.moradores.append(pessoa)
        
    def __str__(self):
        moradores_str = ', '.join([str(morador) for morador in self.moradores])
        return f'Casa em {self.endereco} com moradores: {moradores_str}' 
    
class Fatura:     
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor
    
    def __str__(self):
        return f'Fatura = {self.descricao}, Valor: R${self.valor:.2f}'
    
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 28)

casa = Casa("123 Main St")
casa.adicionar_morador(pessoa1)
casa.adicionar_morador(pessoa2)

fatura = Fatura("conta de água", 100.0)

casa.fatura = fatura

print(casa)
print(casa.fatura)    
    
    
            
        