from dataset import df
import pandas as pd
import locale
import streamlit as st
import time
from babel.dates import format_date

#locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def format_number(value, prefix=''):
    for unit in ['','Mil']:
        if value < 1000:
            return f"{prefix}{value:.2f} {unit}"
        value  /= 1000
    return f"{prefix}{value:.2f} Milhoes"

#data farme receita por estado
df_rec_estado = df.groupby(['Local da compra'])['Preço'].sum().reset_index()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, on='Local da compra').sort_values('Preço', ascending=False)

#data farme receita por mes
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year

#df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name() # original 
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.strftime('%B').str.capitalize() # ajustado para portugues Copilot


#recita por categoria 
def_rec_cat=df.groupby(['Categoria do Produto'])[['Preço']].sum().sort_values('Preço', ascending=False)

#receita por vendedor
df_vendedor = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
#
#funcao para converter arquivo CSV 
@st.cache_data
def convert_csv(df):
    #converte o dataframe em CSV
    return df.to_csv().encode('utf-8')

def mensagem_sucesso():
    sucesso = st.success('Baixado com sucesso!', icon="✅")
    time.sleep(3)
    sucesso.empty()
    st.balloons()

