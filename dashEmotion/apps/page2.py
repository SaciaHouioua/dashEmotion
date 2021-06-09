#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 01:13:10 2021

@author: sacia
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from apps import home, page1, page2, page3


layout = html.Div([
    dbc.Container([
      
        ############### Visualisation #########################"
        
        dbc.Row([
            dbc.Col(html.H1(children='Classification models analysis'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H4(children='Comparison of classification models'), className="mb-1")
        ]), 
       
        dbc.Row([
                dbc.Col(html.H6(children='On the two dataset, we used the following 6 models : LogisticRegression , KNeighborsClassifier , DecisionTreeClassifier, LinearSVC, svm.SVC, SGDClassifier. In order to determine the best performing model in terms of score and speed of execution'), className="mb-4")
            ]),
        
       
               
        ],
        className="mb-5"), 
    ])