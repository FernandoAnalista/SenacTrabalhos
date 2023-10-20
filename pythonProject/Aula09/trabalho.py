import pandas as pd


def realizar_pesquisa():
    resposta = []
    respostas = []

    while True:
        nome = input("Digite o nome do entrevistado( ou 'sair' encerrar): ")

        if nome.lower() == 'sair':
            break

        cidade = input("Digite a cidade do entrevistado: ")
        idade = input("Digite a idade do entrevistado: ")
        resposta = input("Digite a resposta da pergunta da pesquisa: ")

        respostas.append([nome, cidade, resposta, idade])

    colunas = ["Nome", "Cidade", "Idade", "Resposta"]
    df = pd.DataFrame(respostas, columns=colunas)

    df.to_csv("dados_pesquisa.csv", index=False)

    print("Dados da pesquisa foram salvos com sucesso!")


if __name__ == "__main__":
    realizar_pesquisa()
