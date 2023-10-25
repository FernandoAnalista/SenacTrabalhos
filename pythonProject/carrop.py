class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.capacidade_tanque = 0  # Capacidade do tanque em litros
        self.quantidade_combustivel = 0  # Quantidade de combustível no tanque em litros
        self.consumo_medio = 0  # Consumo médio em Km por litro

    def previsao_de_km(self):
        if self.consumo_medio > 0:
            return self.quantidade_combustivel * self.consumo_medio
        else:
            return 0

    def andar_km(self, km):
        consumo = km / self.consumo_medio
        if consumo <= self.quantidade_combustivel:
            self.quantidade_combustivel -= consumo
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

    # Getters e Setters
    def get_cor(self):
        return self.cor

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def get_capacidade_tanque(self):
        return self.capacidade_tanque

    def set_capacidade_tanque(self, capacidade):
        self.capacidade_tanque = capacidade

    def get_consumo_medio(self):
        return self.consumo_medio

    def set_consumo_medio(self, consumo):
        self.consumo_medio = consumo

# Exemplo de uso
carro = Carro("Sedan", "Prata")
carro.set_capacidade_tanque(50)
carro.set_consumo_medio(10)
carro.quantidade_combustivel = 30
print(f"Previsão de KM: {carro.previsao_de_km()} Km")
carro.andar_km(100)
print(f"Quantidade de combustível restante: {carro.quantidade_combustivel} litros")