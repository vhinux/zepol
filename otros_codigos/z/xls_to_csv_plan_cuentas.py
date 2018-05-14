import pandas as pd

df = pd.read_excel('Plan_Cuentas.xls')
df.to_csv('plan_cuentas.csv', encoding='utf-8')
