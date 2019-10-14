import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash_table
from dash.dependencies import Input, Output, State
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dftsa = pd.read_csv('tsa_claims_ujian.csv')



app.layout = html.Div(children = [
        html.H1('Ini Dashboard'),
        html.P('Created by: Christian'),
        dcc.Tabs(value='tabs',id='tabs-1',children = [

            dcc.Tab(label='DataFrame Table',value='DataFrame Table',children=[
                html.Div([
                html.Div([
                    html.H6('Claim Site'),
                    dcc.Dropdown(id='claim_site',
                        options = [{'label':i, 'value':i} for i in dftsa['Claim Site'].dropna().unique()]+[{'label':'All','value':'All'}],
                        value = 'All'
                    )
                ],className='col-3'),
                html.Div([
                    html.H6('Max Rows'),
                    dcc.Dropdown(id='table_maxrows',
                        options = [{'label':i, 'value':i} for i in range(5,50,5)],
                        value = 5
                    )
                ],className='col-3'),
                html.Div(html.Button('Search', id='Search_table'),
                className='col-3')
                ]),
                html.Div(id='tsatable',children =
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in dftsa.columns],
                        data=dftsa.to_dict('records'),
                        page_action = 'native',
                        page_current = 0,
                        page_size = 10,
                        style_table={'overflowX': 'scroll'}
                    )
                )
            ]),
            dcc.Tab(label='Bar-Chart',value='tabsatu',children = [

                html.Div(className='row',children=[
                    html.Div([
                        html.Div([html.H5('Y1')],className='col-3'),
                        html.Div([dcc.Dropdown(id='x1',
                            options = [{'label':i, 'value':i} for i in ['Close Amount','Claim Amount']],
                            value = 'Claim Amount'
                        )],className='col-3')
                    ],className='col-3'),

                    html.Div([
                        html.Div([html.H5('Y2')],className='col-3'),
                        html.Div([
                        dcc.Dropdown(id='x2',
                            options = [{'label':i, 'value':i} for i in ['Close Amount','Claim Amount']],
                            value = 'Close AMount'
                        )],className='col-3')
                    ],className='col-3'),
                    html.Div([
                        html.Div([html.H5('X')],className='col-3'),
                        html.Div([dcc.Dropdown(id='x',
                            options = [{'label':i, 'value':i} for i in ['Claim Type','CLaim Site','Disposition']],
                            value = 'Claim Amount'
                        )],className='col-3')
                    ])
                ]),
                
                html.Div([
                    dcc.Graph(
                    id = 'contoh-graph-bar',
                    figure={
                    'data':[
                        {'x': dftsa['Claim Type'],'y':dftsa['Claim Amount'],'type':'bar','name':'Claim Amount'},
                        {'x': dftsa['Claim Type'],'y':dftsa['Close Amount'],'type':'bar','name':'Close Amount'}
                    ],
                        'layout':{'title':'Graph Bar'}
                    }
                        )])
            ],className='col-3')
            # dcc.Tab(label='Pie-Chart',value='tabtwo',children = [
            #     html.Div(html.Button('Search', id='Search')),
            #     html.Div(
            #         children=[
            #             html.H5('X1'),
            #             dcc.Dropdown(id='x1_pie',
            #                 options = [{'label':i, 'value':i} for i in dftsa.select_dtypes('number').columns],
            #                 value = 'Attack'
            #             )
            #         ]
            #         ,className='col-3'
            #     ),

            #     html.Div([
            #         dcc.Graph(
            #         id = 'contoh-graph-pie',
            #         figure = 
            #         {
            #             'data': [
            #                 go.Pie(
            #                     labels=['Generation {}'.format(i) for i in list(dftsa['Generation'].unique())],
            #                     values = [dftsa.groupby('Generation').mean()['Attack'][i] for i in list(dftsa['Generation'].unique())],
            #                     sort = False)
            #             ],
            #                 'layout' : {'title':'Mean Pie Chart'}
            #         }
            #         )
            #     ])
            # ],className='col-3'),
            # dcc.Tab(label='Scatter-Chart',value='tabtiga',children=
            #     dcc.Graph(
            #         id = 'graph-scatter',
            #         figure = {
            #             'data': [
            #                 go.Scatter(
            #                     x = dftsa[dftsa['Generation']==i]['Attack'],
            #                     y = dftsa[dftsa['Generation']==i]['Speed'],
            #                     text = dftsa[dftsa['Generation']==i]['Name'],
            #                     mode = 'markers',
            #                     name = 'Generation {}'.format(i)
            #                 ) for i in dftsa['Generation'].unique()
            #             ],
            #             'layout' : 
            #                 go.Layout(
            #                     xaxis = {'title':'Attack Pokemon'},
            #                     yaxis = {'title': 'Speed Pokemon'},
            #                     hovermode = 'closest'
            #                 )
            #         }   
            #     ), 
            #     className = 'col-3')
    

            ],
            content_style = {
                'fontFamily':'Arial',
                'borderBottom':'100px solid #d6d6d6',
                'borderLeft':'100px solid #d6d6d6',
                'borderRight':'100px solid #d6d6d6',
                'padding':'44px'
                }            
            )
],style = {
    'maxwidth':'1200px',
    'margin':'0 auto'
}
)

# @app.callback(
#     Output(component_id='contoh-graph-bar', component_property='figure'),
#     [Input(component_id = 'x1', component_property='value'),
#     Input(component_id = 'x2',component_property='value')]
# )
# def create_graph(x1,x2):
#     figure = {
#         'data':[
#             {'x':dftsa['Generation'],'y':dftsa[x1],'type':'bar','name':x1},
#             {'x':dftsa['Generation'],'y':dftsa[x2],'type':'bar','name':x2}
#         ],
#         'layout':{'title':'Bar Chart'}
#     }
#     return figure 


# @app.callback(
#     Output(component_id='contoh-graph-pie', component_property='figure'),
#     [Input(component_id = 'Search', component_property='n_clicks')],
#     [State(component_id = 'x1_pie',component_property = 'value')]
# )
# def create_graph_pie(n_clicks,x1_pie):
#     figure = {
#         'data': [
#             go.Pie(labels=['Generation {}'.format(i) for i in list(dftsa['Generation'].unique())],
#             values = [dftsa.groupby('Generation').mean()[x1_pie][i] for i in list(dftsa['Generation'].unique())],
#             sort = False)
#         ],
#             'layout' : {'title':'Mean Pie Chart'}
#     }
#     return figure 

@app.callback(
    Output(component_id='tsatable', component_property='children'),
    [Input(component_id = 'Search_table', component_property='n_clicks')],
    [State(component_id = 'claim_site',component_property = 'value'),
    State(component_id = 'table_maxrows',component_property = 'value')]
)
def create_table(n_clicks,claim_site,table_maxrows):
    if claim_site=='All':

        table = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dftsa.columns],
            data=dftsa.to_dict('records'),
            page_action = 'native',
            page_current = 0,
            page_size = table_maxrows,
            style_table={'overflowX': 'scroll'}
        )
    else:
        table = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dftsa.columns],
            data=dftsa[dftsa['Claim Site']==claim_site].to_dict('records'),
            page_action = 'native',
            page_current = 0,
            page_size = table_maxrows,
            style_table={'overflowX': 'scroll'}
        )
    return table 





if __name__ == '__main__':
    app.run_server(debug=True)
