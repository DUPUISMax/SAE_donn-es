import matplotlib.pyplot as plt
import json
from module import * 

fichierVoiture = "21.01.14h.json"

with open('données/Voiture/'+fichierVoiture, 'r') as file:
    data = json.load(file)

with open('données/Voiture/placeTotal/placeTotalVoiture.json', 'r') as file:
    data3 = json.load(file)

repetition = len(data)
data2 = tempsConversion("21.01.14h00", repetition)
print(data2)
# Création de l'image
fig, axs = plt.subplots(3, 4, figsize=(14, 7))  # 3 lignes, 4 colonne

# Premier graphique
axs[0,0].set_title('Nombre de places disponibles par parking en pourcentage')

for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[:6]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[0,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)

# Sélectionner les ticks à afficher (chaque 5ème élément)
interval = 6  # Afficher tous les 5 éléments
ticks_to_display = data2[:len(data2):interval]  # Sélectionner tous les 5 éléments de data2
plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=45, ha="right")

# Appliquer les ticks à l'axe des x
axs[0, 0].set_xticks(ticks_to_display)

axs[0,0].set_xlabel('Temps')
axs[0,0].set_ylabel('Places disponibles')
axs[0,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Deuxième graphique

axs[0,3].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[7:13]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[0,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
            
# Sélectionner les ticks à afficher (chaque 6ème élément)
interval = 6  # Afficher tous les 6 éléments
ticks_to_display = data2[:len(data2):interval]  # Sélectionner tous les 5 éléments de data2
plt.setp(axs[0, 3].xaxis.get_majorticklabels(), rotation=45, ha="right")

# Appliquer les ticks à l'axe des x
axs[0, 3].set_xticks(ticks_to_display)

axs[0,3].set_xlabel('Temps')
axs[0,3].set_ylabel('Places disponibles')
axs[0,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Troisième graphique
axs[2,0].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[13:19]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[2,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)

axs[2,0].set_xlabel('Temps')
axs[2,0].set_ylabel('Places disponibles')
axs[2,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Sélectionner les ticks à afficher (chaque 6ème élément)
interval = 6  # Afficher tous les 6 éléments
ticks_to_display = data2[:len(data2):interval]  # Sélectionner tous les 5 éléments de data2
plt.setp(axs[2,0].xaxis.get_majorticklabels(), rotation=45, ha="right")

# Appliquer les ticks à l'axe des x
axs[2,0].set_xticks(ticks_to_display)

# Quatrième graphique
axs[2,3].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[19:25]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[2,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs[2,3].set_xlabel('Temps')
axs[2,3].set_ylabel('Places disponibles')
axs[2,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Sélectionner les ticks à afficher (chaque 6ème élément)
interval = 6  # Afficher tous les 6 éléments
ticks_to_display = data2[:len(data2):interval]  # Sélectionner tous les 5 éléments de data2
plt.setp(axs[2,3].xaxis.get_majorticklabels(), rotation=45, ha="right")

# Appliquer les ticks à l'axe des x
axs[2,3].set_xticks(ticks_to_display)

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

# curseur sur la heatmap
MEF(data)

