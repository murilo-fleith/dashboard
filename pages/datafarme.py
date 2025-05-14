import streamlit as st
from dataset import df
from utils import format_number, df_rec_estado, convert_csv,mensagem_sucesso

# Configuração do título da página
st.set_page_config(
    page_title="Dashboard de  Vendas", #altera o título da aba do navegador
    page_icon=":shopping_trolley:",     #altera o icone da aba do navegador
    layout="wide",            #layout da pagina
    initial_sidebar_state="collapsed", #inicializa a barra lateral fechada
)

st.title('Dataset de vendas  :shopping_trolley:') 

#filtros expender
st.sidebar.title('Filtros')
with st.expander('Selecione as colunas'):  
    colunas = st.multiselect(
        'Colunas ',
        list(df.columns),
        list(df.columns),   
)
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
)
with st.sidebar.expander('Preço'):
    preco = st.slider(
        'Selecione o Preço',
        #min_value=0,
        max_value=int(df['Preço'].max()),
        value=(0, int(df['Preço'].max()))
)
with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input(
        'Selecione a Data da Compra',
        (df['Data da Compra'].min(),  # o primeiro parentes( e por a data estar como tupla
         df['Data da Compra'].max()) # aqui fecha a tupla 
)
with st.sidebar.expander('Vendedor'):
    vendedor = st.multiselect(
        'Vendedor',
        df['Vendedor'].unique(),
        df['Vendedor'].unique()
)
with st.sidebar.expander('Local da compra'):
    local_compra = st.multiselect(
        'Local da compra',
        df['Local da compra'].unique(),
        df['Local da compra'].unique()
)
with st.sidebar.expander('Tipo de pagamento'):
    tipo_pagamento = st.multiselect(
        'Tipo de pagamento',
        df['Tipo de pagamento'].unique(),
        df['Tipo de pagamento'].unique()
)
#aplicar os filtros 
query = '''
    `Categoria do Produto` in @categorias and\
    @preco[0] <= `Preço` <= @preco[1] and\
    @data_compra[0] <= `Data da Compra` <= @data_compra[1] and\
    `Vendedor` in @vendedor and\
    `Local da compra` in @local_compra and\
    `Tipo de pagamento` in @tipo_pagamento
'''
#quando nao for coluna numerica passar entre `Crase`

filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]
st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas') #falores com filtros aplicados
st.markdown('Escreva um nome para o arquivo CSV')
coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input('', label_visibility='collapsed') 
    nome_arquivo += '.csv'
with coluna2:
    st.download_button(
        'Baixar CSV',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso)
st.metric('Receita Total',format_number(filtro_dados['Preço'].sum(),'R$'))
st.dataframe(filtro_dados)





