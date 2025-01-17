from module import * 
import json
data=lecture("données/Voiture/test.json") # mettre le nom du fichier à ouvrir
temps=lecture("données/Temps/temps.json")
L1=[]  
for Antigone in data: # mettre le nom du parking à analyser
    L1.append(Antigone["Antigone"]["place"]) # analyse d'une donnée
print(L1)

# for i in range(len(temps)):
#     tps.append(temps[i])
# if len(L1)!=len(temps): # vérification de la cohérence des données
#     print("erreur")

# print(L1)
# print(temps)

# totalplace=lecture("données/Voiture/placeTotal/placeTotalVoiture.json") # mettre le chemin du fichier à ouvrir (placeTotal)
# totalparking=0

# for Antigone in totalplace:
#     totalparking+=Antigone["Antigone"]["placetotal"]

# print(courbe(temps,L1,"place libre"))
# print(pourcentage(L1,totalparking))
# print(courbe(temps,pourcentage(L1,totalparking),"pourcentage de place libre"))
tot=(len(temps))
L1=[]
    print(cle)
    for parking in cle.items():
        print(parking)
        L1.append(cle['place'])
print(L1)
        
    
    