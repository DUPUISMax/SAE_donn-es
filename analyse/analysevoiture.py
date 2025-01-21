import matplotlib.pyplot as plt
import mplcursors, json
from module import * 

with open('données/Voiture/test2.json', 'r') as file:
    data = json.load(file)

with open('données/Temps/test2.json', 'r') as file:
    data2 = json.load(file)

with open('données/Voiture/placeTotal/placeTotalVoiture.json', 'r') as file:
    data3 = json.load(file)

# Initialiser un dictionnaire pour stocker les places par parking
parkings = {}
parkingstot = {}

# Récupérer les places de chaque parking
for entry in data:
    for parking_name, parking_info in entry.items():
        if parking_name not in parkings:
            parkings[parking_name] = []
        parkings[parking_name].append(parking_info['place'])

# Récupérer les places totales de chaque parking
for entry in data3:
    for parking_name, parking_info in entry.items():
        if parking_name not in parkingstot:
            parkingstot[parking_name] = []
        parkingstot[parking_name].append(parking_info['placetotal'])

# Création de l'image
fig, axs = plt.subplots(3, 4, figsize=(12, 12))  # 3 lignes, 4 colonne

# Premier graphique
axs[0,0].set_title('Nombre de places disponibles par parking en pourcentage')

for i, (parking_name, places) in enumerate(list(parkings.items())[:6]) :
    for parking_name_tot, placestot in parkingstot.items():
        if parking_name == parking_name_tot:
            axs[0,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)

axs[0,0].set_xlabel('Temps')
axs[0,0].set_ylabel('Places disponibles')
axs[0,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Deuxième graphique
axs[0,3].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(parkings.items())[7:13]) :
    for parking_name_tot, placestot in parkingstot.items():
        if parking_name == parking_name_tot:
            axs[0,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs[0,3].set_xlabel('Temps')
axs[0,3].set_ylabel('Places disponibles')
axs[0,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Troisième graphique
axs[2,0].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(parkings.items())[13:19]) :
    for parking_name_tot, placestot in parkingstot.items():
        if parking_name == parking_name_tot:
            axs[2,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs[2,0].set_xlabel('Temps')
axs[2,0].set_ylabel('Places disponibles')
axs[2,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Quatrième graphique
axs[2,3].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(parkings.items())[19:25]) :
    for parking_name_tot, placestot in parkingstot.items():
        if parking_name == parking_name_tot:
            axs[2,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs[2,3].set_xlabel('Temps')
axs[2,3].set_ylabel('Places disponibles')
axs[2,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Laisser ligne et colonne vide vide
fig.delaxes(axs[0, 1])
fig.delaxes(axs[0, 2])
fig.delaxes(axs[1, 1])
fig.delaxes(axs[1, 2])
fig.delaxes(axs[1, 0])
fig.delaxes(axs[2, 1])
fig.delaxes(axs[2, 2])
fig.delaxes(axs[1, 3])

# Ajuster la taille du graphique pour laisser de la place à la légende
fig.subplots_adjust(right=0.7)

# Afficher le graphique
plt.show()