#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:01:54 2021

@author: sacia
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from dash.dependencies import Input, Output, State

import dash

from app import app, server

import graphes

from apps import home, page1, page2, page3, slide

import joblib

# load the model from disk
filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)

# - Layout -

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Predict APP'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='For this APP, we use the first dataset to training our prediction model because it is much more efficient'), className="mb-4")
        ]),
        
       # dbc.Row([
            #dbc.Col(html.Img(src="/assets/wheel.jpeg", height="150px", style={"verticalAlign": "middle"}))
        #]),
        
        dbc.Row([
            dbc.Col(html.H6(children='To try our APP, you can input your text'), className="mb-2  text-center ")
        ]),
        dbc.Row([
            dbc.Col(dcc.Input(id="input1", type="text", placeholder="Type your text", debounce=True), className="mb-4 text-center")
        ]),
        dbc.Row([
            dbc.Col(html.H2(id="output"), className="mb-4 text-center")
        ]),
        
    ])
    ])


@app.callback(
    Output("output", "children"),
    Input("input1", "value"),)
def update_output(input1):  
    
    text = [input1]
    if input1 is None:
        return "Wheel of Emotions"
    else:
        y_pred = graphes.prediction(text,loaded_model )
        return u'Emotion : {}'.format(y_pred)
