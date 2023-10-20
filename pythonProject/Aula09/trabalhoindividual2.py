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

def main():
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

if __name__ == "__main__":
    main()