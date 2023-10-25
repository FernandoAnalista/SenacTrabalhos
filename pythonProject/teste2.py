class Retangulo:

  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def area(self):
    return self.base * self.altura

  def perimetro(self):
    return 2 * (self.base + self.altura)


# Cria um objeto da classe Retangulo
base = float(input("Digite o valor da base do retângulo: "))
altura = float(input("Digite o valor da altura do retângulo: "))
meu_retangulo = Retangulo(base, altura)

# Calcula a área e o perímetro do retângulo
area_retangulo = meu_retangulo.area()
perimetro_retangulo = meu_retangulo.perimetro()

# Exibe na tela a área e o perímetro do retângulo
print("Área do retângulo: ", area_retangulo)
print("Perímetro do retângulo: ", perimetro_retangulo)