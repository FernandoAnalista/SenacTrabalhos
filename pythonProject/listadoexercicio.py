# Crie duas listas de tamanho igual com valores numéricos
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Crie uma nova lista vazia para armazenar a fusão das duas primeiras
nova_lista = []

# Utilize um laço de repetição para percorrer todos os índices das listas originais
for i in range(len(lista1)):
    # Para cada índice, adicione o elemento da primeira lista na nova lista
    nova_lista.append(lista1[i])
    # Em seguida, adicione o elemento correspondente da segunda lista na nova lista
    nova_lista.append(lista2[i])

# Se as listas originais possuem tamanhos diferentes, adicione os elementos restantes da lista maior no final da nova lista
if len(lista1) < len(lista2):
    nova_lista.extend(lista2[len(lista1):])
elif len(lista1) > len(lista2):
    nova_lista.extend(lista1[len(lista2):])

# Imprima a nova lista na tela
print(nova_lista)