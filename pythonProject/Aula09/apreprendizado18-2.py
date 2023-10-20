class Carro:
    def __init__(self, cor, capacidade_tanque, consumo_medio):
        self.cor = cor
        self.capacidade_tanque = capacidade_tanque
        self.combustivel = 0
        self.consumo_medio = consumo_medio

    def previsao_de_autonomia(self):
        return self.combustivel * self.consumo_medio

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo_medio
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            return f"O carro percorreu {distancia} Km."
        else:
            return "O carro não tem combustível suficiente."

carro = Carro("Vermelho", 60.0, 10.0)
carro.combustivel = 40.0

print(f"Autonomia estimada: {carro.previsao_de_autonomia():.2f} Km")
print(carro.andar(200))
