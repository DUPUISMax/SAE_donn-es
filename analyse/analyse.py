from module import * 

L1=[]
tps=[]
data=lecture("données/Voiture/général/test.json") # mettre le nom du fichier à ouvrir

for Antigone in data: # mettre le nom du parking à analyser
    L1.append(Antigone["Antigone"]["place"]) # analyse d'une donnée
temps=lecture("données/Voiture/temps/temps.json") # mettre le nom du fichier à ouvrir

for i in range(len(temps)):
    tps.append(temps[i])
if len(L1)!=len(temps): # vérification de la cohérence des données
    print("erreur")

print(L1)
print(temps)

totalplace=lecture("données/Voiture/placeTotal/placeTotalVoiture.json") # mettre le chemin du fichier à ouvrir (placeTotal)
totalparking=0

for Antigone in totalplace:
    totalparking+=Antigone["Antigone"]["placetotal"]

print(courbe(temps,L1,"place libre"))
print(pourcentage(L1,totalparking))
print(courbe(temps,pourcentage(L1,totalparking),"pourcentage de place libre"))