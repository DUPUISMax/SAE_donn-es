from module import *  # Assurez-vous que les fonctions comme `pourcentage` et `courbe` sont correctement définies
import matplotlib.pyplot as plt
import json

# Liste des fichiers JSON
voiture_files = ['données/Voiture/21.01.8h30.json', 'données/Voiture/21.01.14h.json']
temps_files = ['données/Temps/21.01.8h30.json', 'données/Temps/21.01.14h.json']
placetotal_file = 'données/Voiture/placeTotal/placeTotalVoiture.json'

# Initialiser des dictionnaires pour stocker les données
parkings = {}
parkingstot = {}

# Charger les données des fichiers `voiture_files`
for file_path in voiture_files:
    with open(file_path, 'r') as file:
        data = json.load(file)
        for entry in data:
            for parking_name, parking_info in entry.items():
                if parking_name not in parkings:
                    parkings[parking_name] = []
                parkings[parking_name].append(parking_info['place'])

# Charger les données des fichiers `temps_files`
temps_data = []
for file_path in temps_files:
    with open(file_path, 'r') as file:
        temps_data.extend(json.load(file))  # Fusionner les temps de plusieurs fichiers

# Charger les données des places totales
with open(placetotal_file, 'r') as file:
    data3 = json.load(file)
    for entry in data3:
        for parking_name, parking_info in entry.items():
            if parking_name not in parkingstot:
                parkingstot[parking_name] = []
            parkingstot[parking_name].append(parking_info['placetotal'])

# Tracer les données
plt.figure(figsize=(12, 6))

for parking_name, places in parkings.items():
    for parking_name_tot, placestot in parkingstot.items():
        if parking_name == parking_name_tot:
            plt.plot(
                temps_data,
                pourcentage(places, placestot[0]),
                label=parking_name,
            )

plt.xlabel('Temps')
plt.ylabel('Places disponibles Parking Voiture')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

fig = plt.gcf()  # Récupérer la figure actuelle
fig.subplots_adjust(right=0.7)  # Ajuster la taille du graphique pour laisser de la place à la légende
plt.title('Nombre de places disponibles par parking')
plt.show()
