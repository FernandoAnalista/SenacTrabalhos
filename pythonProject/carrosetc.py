class Carro:
    def __init__(self, modelo, cor) :
        self.modelo = modelo
        self.cor = cor
        self.capacidade_tanque = 0
        self.quantidade_combustivel = 0
        self.consumo_medio = 0

    def previsaoKm(self):
        if self.consumo_medio > 0:
            return self.quantidade_combustivel * self.consumo_medio
        else:
            return 0
        
    def andar_km(self, km):
        consumo = km / self.consumo_medio
        if consumo <= self.quantidade_combustivel:
            self.quantidade_combustivel -= consumo
        else:
            print("Não há combustivel suficiente para percorrer essa distancia.")

    def modelo_cor(self):
        
        print(f"Nome: {self.modelo}\nCor: {self.cor}")


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


carro1 = Carro("Sedan", "Prata")
carro1.set_capacidade_tanque(50)
carro1.set_consumo_medio(10) 
print("")
carro1.modelo_cor()
carro1.quantidade_combustivel = 30
print(f"Previsao de KM: {carro1.previsaoKm()} Km")
carro1.andar_km(100)
print(f"Quantidade de combustivel restante: {carro1.quantidade_combustivel} litros\n")

carro2 = Carro("Fusca", "Azul")
carro2.set_capacidade_tanque(80)
carro2.set_consumo_medio(30)
carro2.modelo_cor()
carro2.quantidade_combustivel = 30
print(f"Previsao de KM: {carro2.previsaoKm()} Km")
carro2.andar_km(200)
print(f"Quantidade de combustivel restante: {carro2.quantidade_combustivel} litros\n")

carro3 = Carro("Palio", "Vermelho")
carro3.set_capacidade_tanque(80)
carro3.set_consumo_medio(30)
carro3.modelo_cor()
carro3.quantidade_combustivel = 30
print(f"Previsao de KM: {carro2.previsaoKm()} Km")
carro3.andar_km(200)
print(f"Quantidade de combustivel restante: {carro2.quantidade_combustivel} litros\n")
