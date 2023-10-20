import csv
import datetime
import time

with open('pesquisa.csv', 'w', newline='') as arquivo:

    writer = csv.writer(arquivo)

    writer.writerow(['idade   ', 'genero   ', 'primeira pergunta   ', 'segunda pergunta   ', 'terceira pergunta   ', 'quarta pergunta   ', 'data   ', 'hora   '])

    while True:

        idade = input('Qual é a sua idade? (Digite 00 para sair) ')

        if idade == '00':
            print('Obrigado por participar da pesquisa!')
            break

        genero = input('Qual é o seu gênero? (M/F/NB) ').upper()

        if genero not in ['M', 'F', 'NB']:
            print('Gênero inválido. Digite M, F ou NB.')
            continue

        respostas = []

        perguntas = ['Você tem acesso à internet?',
                     'Você usa a internet para ter acesso às informações ou como meio de pesquisa?',
                     'Você confia nas informações fornecidas?',
                     'Você usa a internet para lazer?']

        for pergunta in perguntas:
            resposta = input(pergunta + ' (S/N/NS) ').upper()
            if resposta not in ['S', 'N', 'NS']:
                print('Resposta inválida. Digite S, N ou NS.')
                break
            else:
                respostas.append(resposta)

        if len(respostas) == 4:

            data = datetime.date.today().strftime('%d/%m/%Y')
            hora = datetime.datetime.now().strftime('%H:%M:%S')

            writer.writerow([idade, genero] + respostas + [data, hora])
            print('Resposta registrada com sucesso!')
