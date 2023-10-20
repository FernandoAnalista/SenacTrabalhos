#usando tuplas como chaves de dicionários
#dicionário de telefones: chaves com nome e sobrenome
telefones = {
    ('Ana', 'Santos'): '555-5550',
    ('Maria', 'Nascimento'): '555-5551',
    ('Paula', 'Melo'): '555-5552',
}

#iteerando sobre o dicionário
for nome,sobrenome in telefones:
    print(nome,sobrenome)