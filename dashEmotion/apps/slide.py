#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:03:36 2021

@author: sacia
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from apps import home, page1, page2, page3, slide


# - Layout -

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Classification de textes '), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Une tâche NPL (Natural Language Processing) '), className="mb-4")
        ]),
        
         dbc.Row([
            dbc.Col(html.H6(children='Mettre une étiquette sur un texte'), className="mb-4")
        ]),
         
        dbc.Row([
            dbc.Col(html.H6(children='Applications : Analyse de sentiments, Détection de spams , Détection de langue, Classification de documents ... '), className="mb-4")
        ]),
      
        
        dbc.Row([
            dbc.Col(html.H6(children='Un modèle de Machine Learning (ML):  Entraînement  +  Inférence'), className="mb-2")
        ]),
        
       dbc.Row([
            dbc.Col(html.H6(children='Algorithmes de ML : le SVM, la Regression Logistique, le Random Forest'), className="mb-2")
        ]),
        
    ])
    ])