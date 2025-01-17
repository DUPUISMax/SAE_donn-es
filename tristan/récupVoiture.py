import requests, json
from librairie import *


########################################################################################################


# récupération de la réponse à la requête GET
data = requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")


########################################################################################################


# Initialisation des variables de temps
tempsRecup = float(input("Combien de temps voulez-vous récupérer les données ? (en secondes) : "))
attente = float(input("Toutes les combien de secondes voulez-vous récupérer les données ? : "))


########################################################################################################


# Transformation de la réponse en données JSON
data = data.json()


# Récupération des données de tout les parkings en fonction du temps
data = requestTemps(data, tempsRecup, attente)
print("RECUPERATION FINIE")


# Mise en forme des données dans une liste
liste = []
listeOriginal = []
for i in range(len(data)):
    liste.append(ecrireSimpleVoitureDico(data[i]))
    listeOriginal.append(data[i])

    
# Ecriture des données transformées dans un fichier JSON
with open("données/Voiture/dataVoiture.json", "w", encoding="utf-8") as f:
    json.dump(liste, f, ensure_ascii=False, indent=4)
    
# Ecriture des données originales dans un fichier JSON
with open("données/Voiture/dataVoitureOriginal.json", "w", encoding="utf-8") as f:
    json.dump(listeOriginal, f, ensure_ascii=False, indent=4)
    
print("FIN DE L'ECRITURE")

########################################################################################################


# Ouverture du fichier JSON
with open("données/Voiture/dataVoiture.json", "r") as f:
    data = json.load(f)