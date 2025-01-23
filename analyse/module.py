from math import *
import json, mplcursors
import matplotlib.pyplot as plot
import numpy as np

#fonction pour faire la moyenne d'un tableau
def moyenne(t):
    moyenne=0
    for i in range(len(t)):
        moyenne+=t[i]
    return moyenne/len(t)

#fonction pour faire la variance d'un tableau en réutilisant la fonction moyenne
def variance(t):
    moy = moyenne(t)
    var = 0
    for i in range (len(t)):
        var+=(t[i]-moy)**2
    return var/len(t)

#fonction pour faire l'écart type d'un tableau en réutilisant la fonction variance
def ecarttype (t):
    return sqrt(variance(t))

#fonction pour faire la covariance entre deux tableauxen réutilisant la fonction moyenne
def covariance(t1,t2):
    cov=0
    moy1=moyenne(t1)
    moy2=moyenne(t2)
    for i in range (len(t1)):
        cov+=(t1[i]-moy1)*(t2[i]-moy2)
    return cov/len(t1)

#fonction pour faire la corrélation entre deux tableaux en réutilisant les fonctions covariance et variance
def correlation(t1,t2):
    varian=variance(t1)*variance(t2)
    ecart=sqrt(varian)
    corre=abs(covariance(t1,t2)/ecart)
    return corre


#fonction pour faire une courbe de suivi d'une donnée
def courbe(x,y,nom):
    plot.plot(x,y)
    plot.xlabel('Temps')
    plot.ylabel(nom)  
    plot.show()

def pourcentage (t,tot):
    tab=[]
    for i in range (len(t)):
        tab.append(round((t[i]/tot*100),2))
    return tab

def lecture(fichier):
    with open(fichier) as file:
        data = json.load(file)
    return data

# Récupérer les places de chaque parking
def chargevoiture(data):
    parkings = {}
    for entry in data:
        for parking_name, parking_info in entry.items():
            if parking_name not in parkings:
                parkings[parking_name] = []
            parkings[parking_name].append(parking_info['place'])
    return parkings

# Récupérer les places totales de chaque parking
def chargetotal(data):
    parkingstot = {}
    for entry in data:
        for parking_name, parking_info in entry.items():
            if parking_name not in parkingstot:
                parkingstot[parking_name] = []
            parkingstot[parking_name].append(parking_info['placetotal'])
    return parkingstot

def chargeveloplace(data):
    place = {}
    for entry in data:
        for parking_name, parking_info in entry.items():
            if parking_name not in place:
                place[parking_name] = []
            place[parking_name].append(parking_info['placelibre'])
    return place

def chargevelodispo(data):
    velo = {}
    for entry in data:
        for parking_name, parking_info in entry.items():
            if parking_name not in velo:
                velo[parking_name] = []
            velo[parking_name].append(parking_info['velodispo'])
    return velo

# Fonction qui crée un tableau de tableau de places disponibles pour chaque parking
def tableaucor(dico):
    tab=[]
    for cle,valeur in dico.items():
        tab.append(valeur)
    return tab

#fonction pour faire la matrice de corrélation d'un tableau de tableaux en réutilisant la fonction correlation sans mise en forme (un tableau de tableaux)
def correlationmatrice (t):
    tableau=[]
    for j in range (len(t)):
        tab1=[]
        for k in range(len(t)):
            if variance(t[j])==0 or variance(t[k])==0:
                tab1.append(0)
            else: 
                tab1.append(round(correlation(t[j],t[k]),6))
        tableau.append(tab1)
    return tableau


def analysecroisee (t1, t2):
    tableau=[]
    for j in range (len(t1)):
        tab1=[]
        for k in range(len(t2)):
            if variance(t1[j])==0 or variance(t2[k])==0:
                tab1.append(0)
            else: 
                tab1.append(round(correlation(t1[j],t2[k]),6))
        tableau.append(tab1)
        tab1=[]
    return tableau

#fonction de mise en forme de la matrice de corrélation (je n'ai pas utilisé d'heatmap mais imshow)
def MEF (data):
    tableau=correlationmatrice(tableaucor(data))
    fig, ax = plot.subplots()
    cax = ax.imshow(tableau, cmap='Blues')
    fig.colorbar(cax)
    labels = []
    for entry in data:
        for parking_name, parking_info in entry.items():
            labels.append(parking_name)
    cursor = mplcursors.cursor(cax, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f"({labels[int(sel.target[1])]} vs {labels[int(sel.target[0])]}\nCorrélation: {tableau[int(sel.target[0])][int(sel.target[1])]}"))
    plot.show()

def MEFcroisee (t1,t2):
    tableau=analysecroisee(t1,t2)
    plot.imshow(tableau, cmap='Blues')
    plot.colorbar()
    plot.show()
    
def tempsConversion(chaine, repet):
    # Étape 1 : Extraire "8h30" et séparer les heures et minutes
    partie_heure = chaine.split('.')[2]  # Extraction de "8h30"
    heures, minutes = map(int, partie_heure.split('h'))  # Convertit en entiers

    # Étape 2 : Créer une liste vide pour stocker les temps
    temps = []

    # Étape 3 : Boucle pour ajouter des incréments de 5 minutes
    for _ in range(repet):  # Exemple pour générer 10 itérations
        # Ajouter le temps actuel dans la liste
        temps.append(f"{heures:02}h{minutes:02}")
        
        # Ajouter 10 minutes
        minutes += 10
        
        # Gérer les minutes > 60
        if minutes >= 60:
            minutes -= 60
            heures += 1


        # Gérer les heures > 24
        if heures >= 24:
            heures = 0

    # Afficher la liste résultante
    return temps

def affichageDuree(x,y,repetition, duree, axe):
    # Sélectionner les ticks à afficher (chaque 5ème élément)
    interval = repetition  # Afficher tous les repetition éléments
    ticks_to_display = duree[:len(duree):interval]  # Sélectionner tous les repetitions éléments de data2
    plot.setp(axe[x, y].xaxis.get_majorticklabels(), rotation=45, ha="right")

    # Appliquer les ticks à l'axe des x
    axe[x, y].set_xticks(ticks_to_display)