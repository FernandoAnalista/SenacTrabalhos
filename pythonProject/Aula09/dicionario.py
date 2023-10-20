listadepessoas = ["Pessoa1", "Pessoa2", "Pessoa3", "Pessoa4", "Pessoa5"]

enquete_respostas = {pessoa: False for pessoa in listadepessoas}

df.to_csv(
for pessoa in listadepessoas:
    if enquete_respostas[pessoa]:
        print(f"{pessoa} já respondeu à enquete. Obrigado!")
    else:
        print(f"{pessoa}, convidamos você a responder à nossa enquete sobre sua linguagem de programação favorita.")

