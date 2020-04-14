greek_alphabet = {
    u'\u0391': 'Alpha',
    u'\u0392': 'Beta',
    u'\u0393': 'Gamma',
    u'\u0394': 'Delta',
    u'\u0395': 'Epsilon',
    u'\u0396': 'Zeta',
    u'\u0397': 'Eta',
    u'\u0398': 'Theta',
    u'\u0399': 'Iota',
    u'\u039A': 'Kappa',
    u'\u039B': 'Lamda',
    u'\u039C': 'Mu',
    u'\u039D': 'Nu',
    u'\u039E': 'Xi',
    u'\u039F': 'Omicron',
    u'\u03A0': 'Pi',
    u'\u03A1': 'Rho',
    u'\u03A3': 'Sigma',
    u'\u03A4': 'Tau',
    u'\u03A5': 'Upsilon',
    u'\u03A6': 'Phi',
    u'\u03A7': 'Chi',
    u'\u03A8': 'Psi',
    u'\u03A9': 'Omega',
    u'\u03B1': 'alpha',
    u'\u03B2': 'beta',
    u'\u03B3': 'gamma',
    u'\u03B4': 'delta',
    u'\u03B5': 'epsilon',
    u'\u03B6': 'zeta',
    u'\u03B7': 'eta',
    u'\u03B8': 'theta',
    u'\u03B9': 'iota',
    u'\u03BA': 'kappa',
    u'\u03BB': 'lamda',
    u'\u03BC': 'mu',
    u'\u03BD': 'nu',
    u'\u03BE': 'xi',
    u'\u03BF': 'omicron',
    u'\u03C0': 'pi',
    u'\u03C1': 'rho',
    u'\u03C3': 'sigma',
    u'\u03C4': 'tau',
    u'\u03C5': 'upsilon',
    u'\u03C6': 'phi',
    u'\u03C7': 'chi',
    u'\u03C8': 'psi',
    u'\u03C9': 'omega',
}

import glob, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
from ast import literal_eval
import datetime
from datetime import date
import pandas as pd
import numpy as np
from plotly import __version__
import plotly.graph_objs as go


###dash server prepi
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
###


eoi='Fe'
list_of_files = glob.glob('./data/*'+str(eoi)+'*') # * means all if need specific format then *.csv
filename =list_of_files[0]

subg_anl=pd.read_csv(filename)
subg_anl['e_zset']=subg_anl['e_zset'].apply(literal_eval)
subg_anl['mu_zset']=subg_anl['mu_zset'].apply(literal_eval)
groupct=subg_anl['0'].value_counts()

colors=['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', '#ffffff', '#000000']

################################################
#################################################
import plotly.express as px
import plotly.graph_objects as go

fig = go.Figure()
'''
leg_switch=[]
for pp in subg_anl.index:
  if subg_anl['0'][pp] in leg_switch:
    boolswitch=False
    leg_switch.append(subg_anl['0'][pp])
  else:
    boolswitch=True
    leg_switch.append(subg_anl['0'][pp])


  fig.add_trace(go.Scatter(x=subg_anl['e_zset'][pp], y=subg_anl['mu_zset'][pp],
                           showlegend=boolswitch,
                           mode='lines',
                           hoverinfo='none',
                           marker_color=colors[subg_anl['0'][pp]],
                           name=str(list(greek_alphabet.keys())[subg_anl['0'][pp]+6])+' group with count = '+ str(groupct.iloc[subg_anl['0'][pp]])))
'''
###########################################

############################################
app.layout =html.Div([
    dcc.Textarea(
    placeholder='Enter a value...',
    value='This is collection of normalized XAS data take at the selected edge, each color corresponding to a group as determined by DBSCAN',
    style={'width': '90%'}
    ),  
    dcc.Dropdown(
        id='el-dropdown',
        options=[
            {'label': 'Iron (Fe)', 'value': 'Fe'},
            {'label': 'Zinc (Zn)', 'value': 'Zn'}
        ],
        value='Fe'
    ),
    dcc.Graph(
        id='scatgraph',
        style={'height': '100vh','width': '180vh'},
        figure=fig)
    ])

@app.callback(
    Output(component_id='scatgraph',component_property='figure'),
    [Input(component_id='el-dropdown', component_property='value')]
)

def update_graph(dropdown_eoi):
    list_of_files = glob.glob('./data/*'+str(dropdown_eoi)+'*') # * means all if need specific format then *.csv
    filename =list_of_files[0]
    subg_anl=pd.read_csv(filename)
    subg_anl['e_zset']=subg_anl['e_zset'].apply(literal_eval)
    subg_anl['mu_zset']=subg_anl['mu_zset'].apply(literal_eval)
    groupct=subg_anl['0'].value_counts()

    fig = go.Figure()
    leg_switch=[]
    for pp in subg_anl.index:
        if subg_anl['0'][pp] in leg_switch:
            boolswitch=False
            leg_switch.append(subg_anl['0'][pp])
        else:
            boolswitch=True
            leg_switch.append(subg_anl['0'][pp])


        fig.add_trace(go.Scatter(x=subg_anl['e_zset'][pp], y=subg_anl['mu_zset'][pp],
                           showlegend=boolswitch,
                           mode='lines',
                           hoverinfo='none',
                           marker_color=colors[subg_anl['0'][pp]],
                           name=str(list(greek_alphabet.keys())[subg_anl['0'][pp]+6])+' group with count = '+ str(groupct.iloc[subg_anl['0'][pp]])))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True,port=8080)




