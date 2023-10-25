# Variável global para armazenar resultados dos candidatos
resultados_candidatos = [
    "e5_t6_p7_s8",
    "e7_t8_p6_s9",
    "e6_t7_p7_s8",
    "e8_t9_p8_s7",
    "e4_t4_p8_s8",
]

# Função para buscar candidatos com base nos critérios
def buscar_candidatos_com_critérios(e, t, p, s):
    return [i + 1 for i, resultado in enumerate(resultados_candidatos)
            if all(int(valor[1:]) >= crit
                   for valor, crit in zip(resultado.split('_'), (e, t, p, s)))]

def adicionar_candidato():
    e = int(input("Digite a nota na entrevista: "))
    t = int(input("Digite a nota no teste teórico: "))
    p = int(input("Digite a nota no teste prático:"))
    s = int(input("digite a nota nas soft skills: "))

    novo_candidato = f"e{e}_t{t}_p{p}_s{s}"
    resultados_candidatos.append(novo_candidato)
    print("Candidato adicionado com sucesso!")

def main():
    while True:
        print("\nOpções:")
        print("1. Buscar candidatos com base em critérios")
        print("2. Adicionar candidato à lista")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Solicite os critérios ao usuário
            e = int(input("Digite a nota mínima na entrevista: "))
            t = int(input("Digite a nota mínima no teste teórico: "))
            p = int(input("Digite a nota mínima no teste prático: "))
            s = int(input("Digite a nota mínima nas soft skills: "))

            # Chame a função para buscar candidatos compatíveis
            candidatos_compativeis = buscar_candidatos_com_critérios(e, t, p, s)

            # Exiba os candidatos compatíveis
            if candidatos_compativeis:
                print("Candidatos compatíveis:")
                for candidato in candidatos_compativeis:
                    print(f"Candidato {candidato}")
            else:
                print("Nenhum candidato compatível encontrado com base nos critérios fornecidos.")
        elif escolha == "2":
            adicionar_candidato()
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()