import matplotlib.pyplot as plt
import json
from module import * 

fichierVoiture = "22.01.8h00.json"

with open('données/Voiture/'+fichierVoiture, 'r') as file:
    data = json.load(file)

with open('données/Voiture/placeTotal/placeTotalVoiture.json', 'r') as file:
    data3 = json.load(file)

repetition = len(data)
duree = tempsConversion("22.01.8h00", repetition)
print(duree)
# Création de l'image
fig, axs = plt.subplots(3, 4, figsize=(14, 7))  # 3 lignes, 4 colonne

# Premier graphique
axs[0,0].set_title('Nombre de places disponibles par parking en pourcentage')

for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[:6]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[0,0].plot(duree, pourcentage(places, placestot[0]), label=parking_name)

axs[0,0].set_xlabel('Temps')
axs[0,0].set_ylabel('Places disponibles')
axs[0,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Deuxième graphique

axs[0,3].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[7:13]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[0,3].plot(duree, pourcentage(places, placestot[0]), label=parking_name)

axs[0,3].set_xlabel('Temps')
axs[0,3].set_ylabel('Places disponibles')
axs[0,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Troisième graphique
axs[2,0].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[13:19]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[2,0].plot(duree, pourcentage(places, placestot[0]), label=parking_name)

axs[2,0].set_xlabel('Temps')
axs[2,0].set_ylabel('Places disponibles')
axs[2,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Quatrième graphique
axs[2,3].set_title('Nombre de places disponibles par parking en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevoiture(data).items())[19:25]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs[2,3].plot(duree, pourcentage(places, placestot[0]), label=parking_name)
axs[2,3].set_xlabel('Temps')
axs[2,3].set_ylabel('Places disponibles')
axs[2,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)


# appel d'une fonction permettant l'affichage de la durée de la simulation de manière plus lisible
affichageDuree(0,0,24,duree,axs)
affichageDuree(0,3,24,duree,axs)
affichageDuree(2,0,24,duree,axs)
affichageDuree(2,3,24,duree,axs)

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

