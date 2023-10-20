import csv

# Passo 1: Crie uma lista de pessoas
lista_pessoas = ["Maria", "Roberto", "Claudia", "Willian", "Marco"]

# Passo 2: Monte um dicionário com as respostas da enquete
enquete_respostas = {pessoa: "" for pessoa in lista_pessoas}

# Passo 3: Percorra a lista de pessoas e peça que respondam à enquete com detalhes
for pessoa in lista_pessoas:
    x = input(f"{pessoa}, você deseja responder à enquete? (sim/não): ").strip().lower()
    if x == "não":
        continue  # Pula para a próxima pessoa

    resposta = input(f"Qual é a sua linguagem de programação favorita? Digite o nome da linguagem: ")
    enquete_respostas[pessoa] = resposta

# Abra um arquivo CSV para escrever
with open('enquete.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Escreva um cabeçalho no CSV
    writer.writerow(['Nome', 'Linguagem de Programação Favorita'])

    # Escreva os dados das respostas da enquete no CSV
    for pessoa, resposta in enquete_respostas.items():
        writer.writerow([pessoa, resposta])