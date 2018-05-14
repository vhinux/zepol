import pandas as pd

df = pd.read_excel('lista_materiaprima.xls')
df.to_csv('output.csv', encoding='utf-8')
