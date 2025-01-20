from module import * 
import json
data=lecture("données/Voiture/17.01.20h.json") # mettre le nom du fichier à ouvrir
temps=lecture("données/Temps/17.01.20h.json")
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
for cle in data:
    for key in cle.keys():
        print(key)
        print(cle.keys())
        if key == cle.keys():   
                L1.append(key[data]["place"])
print(L1)
        
    
    