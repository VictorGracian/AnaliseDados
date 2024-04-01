import pandas as pd
import plotly.express as px

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
    
def funcoes():
    maior = df_principal['variacao_rs'].max()
    menor =  df_principal['variacao_rs'].min()
    media =  df_principal['variacao_rs'].mean()
    
    media_subiu = df_principal[df_principal['Resultado'] == 'Subiu']['variacao_rs'].mean()
    media_desceu = df_principal[df_principal['Resultado'] == 'Desceu']['variacao_rs'].mean()
    
    print(f'A variação maior é {maior:,.2f}')
    print(f'A variação menor é {menor:,.2f}')
    print(f'A media de variação é {media:,.2f}')
    print(f'A media de quem subiu é {media_desceu:,.2f}')
    
def Analises():
    df_analise_segmento =  df_principal.groupby('Resultado')['variacao_rs'].sum().reset_index()
    df_analise_segmento

def Grafico():
    fig = px.bar(df_analise_segmento, x='Resultado', y='variacao_rs', text='variacao_rs', title='Variação reais por Resultado')