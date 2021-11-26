import pandas as pd
f = open('leitura_CSV/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
# print(rows)
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)

#print(full_data)


planilha = pd.read_csv('leitura_CSV/salarios.csv')
print(planilha.head())