import pandas as pd

df_principal = pd.read_excel("C:\\Users\\victor.graciano\\Desktop\\Imersão Python - Tabela de ações.xlsx", sheet_name="Principal")
df_principal.head(50)

df_total_acoes = pd.read_excel("C:\\Users\\victor.graciano\\Desktop\\Imersão Python - Tabela de ações.xlsx", sheet_name="Total_de_acoes")
df_total_acoes.head(50)

df_ticker = pd.read_excel("C:\\Users\\victor.graciano\\Desktop\\Imersão Python - Tabela de ações.xlsx", sheet_name="Ticker")
df_ticker.head(50)