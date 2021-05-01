#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install jupyter_dash


# In[2]:


import pandas as pd
import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from jupyter_dash import JupyterDash
import plotly.express as px


# In[3]:


df = pd.read_csv('clean_v3.csv')
#df.head()


# In[4]:


df.drop('SalePrice.1', inplace  = True, axis = 1)
#df.head()


# In[81]:


# Create a dash application
app = JupyterDash(__name__)
JupyterDash.infer_jupyter_proxy_config()
#JupyterDash.infer_jupyter_proxy_config()

app.layout = html.Div(children = [
    # Title
    html.H1('Ames Housing Dashboard',
            style = {'textAlign': 'center','color' : '#503D36','font-size': '40px'}),
    
    
    html.Div(['Input Year: ', dcc.Input(id = 'input-year', value = 2010, type ='number', style = {'height':'35px', 'font-size': 25})], style={'font-size': 30}),
    
    html.Br(),
    
    html.Div([html.Div(dcc.Graph(id = 'YearBuilt')), html.Div(dcc.Graph(id = 'OverallQual'))], style = {'display': 'flex'}),
    html.Br(),
    html.Div([html.Div(dcc.Graph(id = 'FullBath')), html.Div(dcc.Graph(id = 'Fireplaces'))], style = {'display': 'flex'}),
    html.Br(),
    html.Div(dcc.Graph(id = 'TotRmsAbvGrd'), style={'width':'65%'})
])

@app.callback(
    [Output(component_id = 'YearBuilt', component_property = 'figure'),
     Output(component_id = 'OverallQual', component_property = 'figure'),
     Output(component_id = 'FullBath', component_property = 'figure'),
     Output(component_id = 'Fireplaces', component_property = 'figure'),
     Output(component_id = 'TotRmsAbvGrd', component_property = 'figure'),
    ],
    Input(component_id = 'input-year', component_property = 'value')
)

def get_graph(test):
    df_yb = df.groupby('YearBuilt').mean().reset_index()
    YearBuilt = px.line(df_yb, x = 'YearBuilt', y = 'SalePrice')
    
    #df_oq = df.groupby('YearBuilt').mean().reset_index()
    OverallQual = px.line(df_yb, x = 'YearBuilt', y = 'OverallQual')
    
    df_fb = df.groupby('FullBath').mean().reset_index()
    FullBath = px.bar(df_fb, x = 'FullBath', y = 'SalePrice')
    
    df_fp = df.groupby('Fireplaces').mean().reset_index()
    Fireplaces = px.bar(df_fp, x = 'Fireplaces', y = 'SalePrice')
    
    df_trag = df.groupby('TotRmsAbvGrd').mean().reset_index()
    TotRmsAbvGrd = px.bar(df_trag, x = 'TotRmsAbvGrd', y = 'SalePrice')
    
    return[YearBuilt, OverallQual, FullBath, Fireplaces, TotRmsAbvGrd]

if __name__ == '__main__':
    app.run_server(mode="external", host="localhost", port=7645, debug=True)


# In[ ]:




