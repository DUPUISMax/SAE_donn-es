import requests, time, json
from math import sqrt

################################################""" CALCULS MATHEMATIQUES """ ####################################################

# moyenne des valeurs liste
def moy(list):
    return sum(list) / len(list)

###########################################################################################################################

# variance des valeurs liste
def var(list):
    somme = 0
    for element in list:
        somme += (element - moy(list))**2
    return somme / len(list)

###########################################################################################################################

# Ecart type des valeurs liste
def ecartType(list):
    return sqrt(var(list))

###########################################################################################################################

# Covariance des valeurs de deux listes 
def covariance(X,Y):
    differenceX = 0
    differenceY = 0
    if len(X)>=len(Y):
        somme = 0
        for i in range(len(Y)):
            somme += (moy(X) - X[i]) * (moy(Y) - Y[i])
        return somme / len(Y)
    
    elif len(Y)>len(X):
        somme = 0
        for i in range(len(X)):
            somme += (moy(X) - X[i]) * (moy(Y) - Y[i])
        return somme / len(X)

###########################################################################################################################

# Corrélation des valeurs de deux listes
def correlation(X,Y):
    return (covariance(X,Y) / (ecartType(X) * ecartType(Y)))

###########################################################################################################################

# Matrice de corrélation en fonction d'un nombre variable de liste
def matriceCorrelation(*arg):
    matrice = []
    for i in range(len(arg)):
        ligne = []
        for j in range(len(arg)):
            valeur = correlation(arg[i],arg[j])
            ligne.append(valeur)
        matrice.append(ligne)
    return matrice

###########################################################################################################################

def affichageMatriceCorrelation(matrice):
    
    print("matrice de corrélation :")
    largeur = max(max(len(f"{val:.2f}") for val in ligne) for ligne in matrice)
    for ligne in matrice:
        print(" | ".join(f"{val:.2f}".center(largeur) for val in ligne))
        
#######################################################################################################################

# Récupération de données de tout les données en fonction du temps avec compteur de temps intégré
def requestTemps(data, Te, attente):
    # Initialisation des variables
    L = []
    start = int(time.time())
    actualTime = int(time.time())
    compteur = 0
    
    # Compteur de temps
    while actualTime < start + Te:
        compteur += attente
        print(f"{compteur} secondes")
    
        # Récupération des données
        L.append(data)
        time.sleep(attente)
        actualTime = time.time()

    return L

################################################ """ VOITURE """ ######################################################

def ecrireSimpleVoitureDico(data):
    donnees = {}
    
    # Ecriture simplifiée des données sous forme de dictionnaire
    for i in range(len(data)):
        dico={
        "placeDispo": data[i]["availableSpotNumber"]["value"],
        "placesTotals": data[i]["totalSpotNumber"]["value"],
        "tempsMdif": data[i]['availableSpotNumber']["metadata"]["timestamp"]["value"],
        "emmplacement": data[i]['location']["value"]["coordinates"],
        "statut": data[i]["status"]["value"],
        }
        
        # Ajout des données dans un dictionnaire avec comme clé le nom du parking
        donnees[data[i]["name"]["value"]] = dico
    return donnees

################################################ """ VELO """ ####################################################

def ecritureSimpleVeloDico(data):
    donnees = {}
    
    # Ecriture simplifiée des données sous forme de dictionnaire
    for i in range(len(data)): 
        dico = {
        "veloDispo": data[i]["availableBikeNumber"]["value"],
        "placeLibre": data[i]["freeSlotNumber"]["value"],
        "placesTotals": data[i]["totalSlotNumber"]["value"],
        "tempsModif": data[i]['availableBikeNumber']["metadata"]["timestamp"]["value"],
        "emmplacement": data[i]['location']["value"]["coordinates"],
        "statut": data[i]["status"]["value"],
        }
        
        # Ajout des données dans un dictionnaire avec comme clé le nom du parking
        donnees[data[i]["address"]["value"]["streetAddress"]] = dico
    return donnees