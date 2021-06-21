#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 01:13:10 2021

@author: sacia
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from apps import home, page1, page2, page3, slide


import graphes
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
                dbc.Col(html.H6(children='We used the following 6 models : LogisticRegression , KNeighborsClassifier , DecisionTreeClassifier, LinearSVC, svm.SVC, SGDClassifier. In order to determine the best performing model in terms of score and speed of execution.'), className="mb-4")
            ]),
        
       #dbc.Row([
             #   dbc.Col(html.H4(children='With out pipeline'), className="mb-4")
           # ]),
       
       dbc.Row([
                dbc.Col(html.H5(children='Dataset1'),),
                dbc.Col(html.H5(children='Dataset2'), className="mb-4"),
            ]),   
        
      
                        
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-5',figure=graphes.fig5),),
                # a remplacer par le meme sur data set 2
                dbc.Col(dcc.Graph(id='graph-6',figure=graphes.fig6), className="mb-4"),
            ]),
       
         dbc.Row([
                dbc.Col(html.H6(children=' The best performing model in terms of score and execution speed is the SGDClassifier. The KNeighborsClassifier gets the lowest score with the fastest execution time with "n_neighbors=3". If the time allows it, we come back to this step to test several "n_neighbors=N". On the other hand the SVM.SVC represents the longest processing time.'),),
                dbc.Col(html.H6(children='On dataset 2, the best performing model stell the SGD model. The comparison curve looks similar to that of data set 1 '), className="mb-4"),
            ]),
                
         
         dbc.Row([
                dbc.Col(html.H5(children='Score Dataset1'),),
                dbc.Col(html.H5(children='Score Dataset2'), className="mb-4"),
            ]),
         
         dbc.Row([
                dbc.Col(dcc.Graph(id='graph-7',figure=graphes.fig7),),
                # a remplacer par le meme sur data set 2
                dbc.Col(dcc.Graph(id='graph-8',figure=graphes.fig8), className="mb-4"),
            ]),
        
        dbc.Row([
                dbc.Col(html.H5(children='Time Dataset1'),),
                dbc.Col(html.H5(children='Time Dataset2'), className="mb-4"),
            ]),
         dbc.Row([
                dbc.Col(dcc.Graph(id='graph-9',figure=graphes.fig9),),
                # a remplacer par le meme sur data set 2
                dbc.Col(dcc.Graph(id='graph-10',figure=graphes.fig10), className="mb-4"),
            ]),
    
         dbc.Row([
                dbc.Col(html.H5(children='Classification_report Dataset1'),),
                dbc.Col(html.H5(children='Classification_report Dataset2'), className="mb-4"),
            ]),
         
         dbc.Row([
                dbc.Col(html.H6(children='We used the SGD Classifier on a pipline with stop_words and tfidf.'), className="mb-4")
            ]),
         
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-11',figure=graphes.fig11),),
                # a remplacer par le meme sur data set 2
                dbc.Col(dcc.Graph(id='graph-12',figure=graphes.fig12), className="mb-4"),
            ]),
        
               
        ],
        className="mb-5"), 
    ])