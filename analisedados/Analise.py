import pandas as pd


def ImportandoPlanilhas():
    df_principal = pd.read_excel("C:\\Users\\victor.graciano\\Desktop\\Imersão Python - Tabela de ações.xlsx", sheet_name="Principal")

    df_total_acoes = pd.read_excel("C:\\Users\\victor.graciano\\Desktop\\Imersão Python - Tabela de ações.xlsx", sheet_name="Total_de_acoes")

    df_ticker = pd.read_excel("C:\\Users\\victor.graciano\\Desktop\\Imersão Python - Tabela de ações.xlsx", sheet_name="Ticker")
    
    
def TirandoInuteis():
    df_principal = df_principal[['Ativo','Data','Último (R$)','Var. Dia (%)']].copy()
    df_principal
    
    df_principal = df_principal.rename(columns={'Último (R$)':'Valor Final'})
    df_principal = df_principal.rename(columns={'Var. Dia (%)':'var_dia_pct'})
    df_principal
    
def AdicionandoColunas():
    df_principal['var_pct'] = df_principal['var_dia_pct'] /100
    df_principal['valor_inicial'] = df_principal['Valor Final'] / (df_principal['var_pct'] + 1)
    df_principal
    
def Merge():
    df_principal = df_principal.merge(df_total_acoes, left_on='Ativo', right_on="Código", how='left')
    df_principal.drop(columns=['Código'])
    
    df_principal['variacao_rs'] = ((df_principal['Valor Final']) - df_principal['valor_inicial']) * df_principal['Qtde. Teórica']
    pd.options.display.float_format = '{:.2f}'.format
    df_principal['Qtde. Teórica'] = df_principal['Qtde. Teórica'].astype(int)
    df_principal

def Condicao():
    df_principal['Resultado'] = df_principal['variacao_rs'].apply(lambda x: 'Subiu' if x > 0 else ('Desceu' if x < 0 else 'Estavel'))
    df_principal