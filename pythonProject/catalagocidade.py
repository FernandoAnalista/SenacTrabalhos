catalogo_cidades = [
    {
        "nome": "Rio de Janeiro",
        "estado": "Rio de Janeiro",
        "populacao": 6747815,
        "tem_praia": True,
        "regiao": "Sudeste",

    },
    {
        "nome": "São Paulo",
        "estado": "São Paulo",
        "populacao": 12252023,
        "tem_praia": False,
        "regiao": "Sudeste",

    },
    {
        "nome": "Recife",
        "estado": "Pernambuco",
        "populacao": 1645727,
        "tem_praia": True,
        "regiao": "Nordeste",

    },
    {
        "nome": "Natal",
        "estado": "Rio Grande do Norte",
        "populacao": 884122,
        "tem_praia": True,
        "regiao": "Nordeste",

    },
]
for cidade in catalogo_cidades:
    print(f"Nome da cidade: {cidade['nome']}")
    print(f"Estado: {cidade['estado']}")
    print(f"População: {cidade['populacao']} habitantes")
    if cidade['tem_praia']:
        print("Possui praia.")
    else:
        print("Não possui praia.")
    print(f"Região: {cidade['regiao']}")
    print()
