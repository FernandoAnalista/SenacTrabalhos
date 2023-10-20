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
    candidatos_compativeis = []

    for i, resultado in enumerate(resultados_candidatos, start=1):
        partes = resultado.split('_')

        # Extrair valores numéricos das partes
        e_valor = int(partes[0][1:])  # Remove o 'e' e converte para inteiro
        t_valor = int(partes[1][1:])  # Remove o 't' e converte para inteiro
        p_valor = int(partes[2][1:])  # Remove o 'p' e converte para inteiro
        s_valor = int(partes[3][1:])  # Remove o 's' e converte para inteiro

        # Verifique se as notas são maiores ou iguais aos critérios
        if e_valor >= e and t_valor >= t and p_valor >= p and s_valor >= s:
            candidatos_compativeis.append(i)

    return candidatos_compativeis

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




