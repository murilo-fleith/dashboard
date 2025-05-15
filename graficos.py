import plotly.express as px
from utils import df_rec_estado,df_rec_mensal,def_rec_cat,df_vendedor

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope = 'south america',
    size = 'Preço',
    template= 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False , 'lon': False},
    title= 'Receita por Estado'
    )

grafico_rec_mensal = px.line(
    df_rec_mensal,  #df 
    x = 'Mes', 
    y = 'Preço',
    template = 'seaborn',
    markers = True,
    range_y= (0, df_rec_mensal['Preço'].max()),
    color= 'Ano',
    line_dash= 'Ano',
    title = 'Receita por Mes'
)
grafico_rec_mensal.update_layout(yaxis_title='Receita (R$)')

grafico_rec_estado = px.bar(
    df_rec_estado.head(7), #.head() para mostrar apenas os 5 primeiros estados
    x = 'Local da compra',
    y = 'Preço',
    text_auto=True,
    #template = 'seaborn',
    title = 'Receita por Estado',
    #color_discrete_sequence= ['#636EFA'],
    #text = df_rec_estado['Preço'].apply(lambda x: f'R$ {x:,.2f}'),
)
#
grafico_rec_cat = px.bar(
    def_rec_cat.head(7),
    text_auto=True,
    title = 'Receita por Categoria',
)

grafico_rec_vendedor = px.bar(
    df_vendedor[['sum']].sort_values('sum', ascending=False).head(7),
    x = 'sum',
    y = df_vendedor[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto=True,
    title = 'Receita por Vendedor',
)

grafico_vendas_vendedor = px.bar(
    df_vendedor[['count']].sort_values('count', ascending=False).head(7),
    x = 'count',
    y = df_vendedor[['count']].sort_values('count', ascending=False).head(7).index,
    text_auto=True,
    title = 'Quantidade de Vendas por Vendedor',
)