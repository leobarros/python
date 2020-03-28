import csv

with open('desafio-ibge.csv', encoding='ISO8859-1') as coleta:
    for dados in csv.reader(coleta):
        print('Nome Destino: %s, Nome Origem: %s' % (dados[8], dados[3]))
