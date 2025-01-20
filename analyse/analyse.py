from module import * 

import json

# Charger les données du fichier JSON
with open('données/Voiture/17.01.20h.json', 'r') as file:
    data = json.load(file)
with open('données/Temps/17.01.20h.json', 'r') as file:
    data2 = json.load(file)
# Initialiser un dictionnaire pour stocker les places par parking
parkings = {}
print(data2[])
# Récupérer les places de chaque parking
for entry in data:
    for parking_name, parking_info in entry.items():
        if parking_name not in parkings:
            parkings[parking_name] = []
        parkings[parking_name].append(parking_info['place'])

# Afficher les places pour chaque parking
for parking_name, places in parkings.items():
    courbe(data2,places, parking_name)






        
    
    