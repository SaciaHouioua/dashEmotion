#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:28:54 2021

@author: sacia
"""

import plotly.graph_objects as go
import pandas as pd
import dash_table

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np

from apps import home , page1, page2, page3



import graphes

tab1_content = dash_table.DataTable(id='container-button-timestamp',
            #data=df.to_dict('records'),
            data=graphes.datak.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in graphes.datak.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
                'padding-left':'5px'
                }
            )


tab2_content = dash_table.DataTable(id='container-button-timestamp',
            data=graphes.dataw.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in graphes.dataw.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left',
             },
            css=[ {'selector': '.row', 'rule': 'margin: 0'}]
            )



layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Data table'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising the data table from the two file'), className="mb-4")
        ]),
        dbc.Row([dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Data Kaggle",label_style={"color":"#810303"}),
        dbc.Tab(tab2_content, label="Data World", label_style={"color":"#11337E"}),
    ]
  ),
      ]),
        
        
        ############### Visualisation #########################"
        
        dbc.Row([
            dbc.Col(html.H1(children='Visualisation'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H4(children='The count of emotion'), className="mb-1")
        ]), 
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-1',figure=graphes.fig),),
                dbc.Col(dcc.Graph(id='graph-2',figure=graphes.fig4), className="mb-2"),
            ]),
        dbc.Row([
                dbc.Col(html.H6(children='The shape of first dataset :  (21459, 2) with 6 emotions classes.         The shape of the second dataset : (40000, 4 ) with 13 emotions classes'), className="mb-4")
            ]),
        dbc.Row([
                dbc.Col(html.H4(children='The proportion'), className="mb-1")
            ]),
       
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-5',figure=graphes.fig2),),
                dbc.Col(dcc.Graph(id='graph-6',figure=graphes.fig3), className="mb-4"),
            ]),
        
        ],
        className="mb-5"), 
    ])