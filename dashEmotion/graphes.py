#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:32:56 2020

@author: sacia
"""

import numpy as np # algèbre linéaire
import pandas as pd # procès de données, CSV file I/O (e.g. pd.read_csv)

import plotly.graph_objs as go

import plotly.offline as pyo

import joblib

#from plotly.offline import iplot
import plotly.express as px

#from callbacks import display_value_varWord

# librairie matplotlib
#import matplotlib.pyplot as plt

# Chargement des données qui seront utilisées.


datak = pd.read_csv('data/Emotion_final.csv')

# Préparation des données
# preparation des targets
corpus = np.array(datak["Text"])
targets = np.array(datak["Emotion"])

#la liste des émotions
listEmotion = datak["Emotion"].unique()


# encodage des données
# remplacer ['sadness' 'anger' 'love' 'surprise' 'fear' 'happy'] par 1, 2,3, 4, 5

datak["Emotion"] = datak["Emotion"].astype('category').cat.codes 

# la liste des émotions encodées

listEmotionCat = datak["Emotion"].unique()

correspondance  = { k : v for k , v in zip(listEmotionCat, listEmotion)}

def prediction (X, mod):
    pred = mod.predict(X)
    return correspondance[pred[0]]

# load the model from disk
filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)




# le pourcentage des différents sentiments :
# definition d'une fonction qui calcule le pourcentage d'un sentiment par rapport à la taille du data set:

def percentage (l,sentiment) :
    i = 0
    sum = 0
    for i in range (len(l)):
        if l[i] == sentiment:
            sum += 1
    return round(sum)

# listE englobe la somme de chaque émotion ds le dataset

listE = []
sumE = 0
for i in range (len(listEmotion)):
    sumE = percentage(datak["Emotion"],listEmotionCat[i])
    listE.append(sumE)

# les différentes figures

fig = px.histogram(x=targets, nbins=4).update_xaxes(categoryorder = 'total descending')

fig.update_layout( title="DataSet 1 ",
    xaxis_title="Emotion",
    yaxis_title="Count")


fig2 = px.pie(values=listE, names=listEmotion, title='Pourcentage des sentiments dans le dataset 1')
#fig2.update_layout( title="PieChart des sentiments ")
fig2.update_traces(textposition='inside', textinfo='percent+label')

#fig5 = px.histogram(datak,x="Emotion", color="Emotion", marginal="rug", hover_name="Text", histfunc="sum")

# 2eme jeu de donnée
dataw = pd.read_csv('data/text_emotion.csv')

#liste des emotions 2eme dataset
listEmotion1 = dataw["sentiment"].unique()

# Préparationration des données
targets2 = dataw["sentiment"].astype('category').cat.codes 


listE1 = []

targets2 = dataw["sentiment"]
sumE = 0
for i in range (len(listEmotion1)):
    sumE = percentage( targets2,listEmotion1[i])
    
    listE1.append(sumE)


fig3 = px.pie(values=listE1 , names=listEmotion1, title='Pourcentage des sentiments dans le dataset 2')

fig4 = px.histogram(x=dataw["sentiment"], nbins=13).update_xaxes(categoryorder = 'total descending', title="le dataset 2")

'''
# chargement des résultats 

df1 = pd.read_csv('result1.csv')
df2 = pd.read_csv('result2.csv')
df3 = pd.read_csv('result3.csv')
dfwordE = pd.read_csv('dfwordEmotion.csv')

fig7 = px.line(df2, x="Classifier", y="f1Score")

# comapraison de la performance des 5 modeles
# avec et sans pipeline pour les 3 data set
df12 = pd.read_csv('result11.csv')
df21 = pd.read_csv('result21.csv')
df31 = pd.read_csv('result31.csv')

# dataset1 comparaison du score des 5 classifiers avec et sans pipeline
figPipe = go.Figure()
figPipe.add_trace(go.Scatter(x=df1["Classifier"], y=df1["f1Score"],
                    mode='lines',
                    name='f1score sans piple_line'))
figPipe.add_trace(go.Scatter(x=df12["Classifier"], y=df12["f1ScorePipe"],
                    mode='lines+markers',
                    name='f1score Avec piple_Line'))

# comparaison du temps des 5 classifiers avec et sans pipeline

figTime = go.Figure()
figTime.add_trace(go.Scatter(x=df1["Classifier"], y=df1["Time"],
                    mode='lines',
                    name='Time sans piple_line'))

figTime.add_trace(go.Scatter(x=df12["Classifier"], y=df12["TimePipe"],
                    mode='lines+markers',
                    name='Time Avec piple_Line'))

# dataset2 comaparaison des performances des cinq classifiers selon le f1score

figPipe2 = go.Figure()
figPipe2.add_trace(go.Scatter(x=df2["Classifier"], y=df2["f1Score"],
                    mode='lines',
                    name='Sans piple_line'))
figPipe2.add_trace(go.Scatter(x=df21["Classifier"], y=df21["f1ScorePipe"],
                    mode='lines+markers',
                    name='Avec piple_Line'))
# dataset2 comaparaison des performances des cinq classifiers selon le f1score
figTime2 = go.Figure()
figTime2.add_trace(go.Scatter(x=df2["Classifier"], y=df2["Time"],
                    mode='lines',
                    name='Sans piple_line'))

figTime2.add_trace(go.Scatter(x=df21["Classifier"], y=df21["TimePipe"],
                    mode='lines+markers',
                    name='Avec piple_Line'))

# dataset3 comparaison du score des 5 classifiers avec et sans pipeline

figPipe3 = go.Figure()
figPipe3.add_trace(go.Scatter(x=df3["Classifier"], y=df3["f1Score"],
                    mode='lines',
                    name='Sans piple_line'))
figPipe3.add_trace(go.Scatter(x=df31["Classifier"], y=df31["f1ScorePipe"],
                    mode='lines+markers',
                    name='Avec piple_Line'))

# dataset3 comaparaison des performances des cinq classifiers selon le f1score
figTime3 = go.Figure()
figTime3.add_trace(go.Scatter(x=df3["Classifier"], y=df3["Time"],
                    mode='lines',
                    name='Sans piple_line'))

figTime3.add_trace(go.Scatter(x=df31["Classifier"], y=df31["TimePipe"],
                    mode='lines+markers',
                    name='Avec piple_Line'))


# fscore1 Create traces comparaison des classifiers sur les 3 dataset
fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=df1["Classifier"], y=df1["f1Score"],
                    mode='lines',
                    name='Dataset1'))
fig5.add_trace(go.Scatter(x=df2["Classifier"], y=df2["f1Score"],
                    mode='lines+markers',
                    name='Dataset2'))
fig5.add_trace(go.Scatter(x=df3["Classifier"], y=df3["f1Score"],
                    mode='lines+markers',
                    name='Dataset3'))

# Time Create traces comparaison des classifiers sur les 3 dataset
fig51 = go.Figure()
fig51.add_trace(go.Scatter(x=df1["Classifier"], y=df1["Time"],
                    mode='lines',
                    name='Dataset1'))
fig51.add_trace(go.Scatter(x=df2["Classifier"], y=df2["Time"],
                    mode='lines+markers',
                    name='Dataset2'))
fig51.add_trace(go.Scatter(x=df3["Classifier"], y=df3["Time"],
                    mode='lines+markers',
                    name='Dataset3'))

# Les N top  mots les plus utilisées par catégories

def figwordE(n):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dfwordE['love'][:n], y=[i for i in range(n)],
                    name='Love'))
    fig.add_trace(go.Scatter(x=dfwordE['surprise'][:n], y=[i for i in range(n)],
                    name='surprise'))
    fig.add_trace(go.Scatter(x=dfwordE['anger'][:n], y=[i for i in range(n)],
                    name='anger'))
    fig.add_trace(go.Scatter(x=dfwordE['happy'][:n], y=[i for i in range(n)],
                    name='happy'))
    fig.add_trace(go.Scatter(x=dfwordE['sadness'][:n], y=[i for i in range(n)],
                    name='sadness'))
    fig.add_trace(go.Scatter(x=dfwordE['fear'][:n], y=[i for i in range(n)],
                    name='fear'))
    return fig 

# les top 10 mots les plus utilisés par émotions
'''