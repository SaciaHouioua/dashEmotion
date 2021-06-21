#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:31:30 2021

@author: sacia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:06:37 2020
@author: randon
"""

#import plotly.express as px
#import plotly.graph_objs as go



#####


import numpy as np
#import base64
#import io
from io import BytesIO
import re
from dash import no_update


import pandas as pd




#####



import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app, server

import dash
import numpy as np

from app import app, server

from apps import home , page1, page2, page3, slide



layout = html.Div([
    dbc.Container([
        
        dbc.Row([
            dbc.Col(html.H1("The Wheel of Emotions", className="text-center")
                    , className="mb-4 mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(dbc.Card(children=[
                                       # html.H5(children='Data', className="text-center"),
                                       dbc.Button("Visualize" , href="/page1",
                                                                   color="primary",
                                                        className="mt-3"),
                                       html.Img(src="/assets/data.jpeg", height="150px")]),),
           
            dbc.Col(dbc.Card(children=[
                                       # html.H5(children='MachineLearning',className="text-center"),
                                       dbc.Button("Analyze" , href="/page2",
                                                                   color="primary",
                                                        className="mt-3"),
                                       html.Img(src="./assets/ml.png", height="150px")]),),
            dbc.Col(dbc.Card(children=[
                                       # html.H5(children='Emotion', className="text-center"),
                                        dbc.Button("Emotion" , href="/page3",
                                                                   color="primary",
                                                        className="mt-3"),
                                       html.Img(src="/assets/predict.png", height="150px")])
                        ,className="mb-4"),
            ]),
        
        
      
        
        ])])






       
        
        
        
    





        
        
   

