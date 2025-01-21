import matplotlib.pyplot as plt
import json
from module import * 

with open('données/Vélo/21.01.14h.json', 'r') as file:
    data = json.load(file)

with open('données/Temps/21.01.14h.json', 'r') as file:
    data2 = json.load(file)

with open('données/Vélo/placeTotal/placeTotalVélo.json', 'r') as file:
    data3 = json.load(file)

# Création de l'image 1
fig1, axs1 = plt.subplots(3, 4, figsize=(14, 7))  # 3 lignes, 4 colonne

# Premier graphique
axs1[0,0].set_title('Nombre de places disponibles pour vélo en pourcentage')

for i, (parking_name, places) in enumerate(list(chargeveloplace(data).items())[:15]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs1[0,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)

axs1[0,0].set_xlabel('Temps')
axs1[0,0].set_ylabel('Places disponibles')
axs1[0,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Deuxième graphique
axs1[0,3].set_title('Nombre de places disponibles pour vélo en pourcentage')
for i, (parking_name, places) in enumerate(list(chargeveloplace(data).items())[16:30]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs1[0,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs1[0,3].set_xlabel('Temps')
axs1[0,3].set_ylabel('Places disponibles')
axs1[0,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Troisième graphique
axs1[2,0].set_title('Nombre de places disponibles pour vélo en pourcentage')
for i, (parking_name, places) in enumerate(list(chargeveloplace(data).items())[31:45]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs1[2,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs1[2,0].set_xlabel('Temps')
axs1[2,0].set_ylabel('Places disponibles')
axs1[2,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Quatrième graphique
axs1[2,3].set_title('Nombre de places disponibles pour vélo en pourcentage')
for i, (parking_name, places) in enumerate(list(chargeveloplace(data).items())[46:60]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs1[2,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs1[2,3].set_xlabel('Temps')
axs1[2,3].set_ylabel('Places disponibles')
axs1[2,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Laisser ligne et colonne vide vide
fig1.delaxes(axs1[0, 1])
fig1.delaxes(axs1[0, 2])
fig1.delaxes(axs1[1, 1])
fig1.delaxes(axs1[1, 2])
fig1.delaxes(axs1[1, 0])
fig1.delaxes(axs1[2, 1])
fig1.delaxes(axs1[2, 2])
fig1.delaxes(axs1[1, 3])

# Ajuster la taille du graphique pour laisser de la place à la légende
fig1.subplots_adjust(right=0.7)

# Afficher le graphique
plt.show()

MEF(tableaucor(chargeveloplace(data)))
# Création de l'image 2
fig2, axs2 = plt.subplots(3, 4, figsize=(14, 7))  # 3 lignes, 4 colonne

# Premier graphique
axs2[0,0].set_title('Nombre de vélos disponibles en pourcentage')

for i, (parking_name, places) in enumerate(list(chargevelodispo(data).items())[:15]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs2[0,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)

axs2[0,0].set_xlabel('Temps')
axs2[0,0].set_ylabel('Places disponibles')
axs2[0,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Deuxième graphique
axs2[0,3].set_title('Nombre de vélos disponibles en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevelodispo(data).items())[16:30]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs2[0,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs2[0,3].set_xlabel('Temps')
axs2[0,3].set_ylabel('Places disponibles')
axs2[0,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Troisième graphique
axs2[2,0].set_title('Nombre de vélos disponibles en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevelodispo(data).items())[31:45]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs2[2,0].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs2[2,0].set_xlabel('Temps')
axs2[2,0].set_ylabel('Places disponibles')
axs2[2,0].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Quatrième graphique
axs2[2,3].set_title('Nombre de vélos disponibles en pourcentage')
for i, (parking_name, places) in enumerate(list(chargevelodispo(data).items())[46:60]) :
    for parking_name_tot, placestot in chargetotal(data3).items():
        if parking_name == parking_name_tot:
            axs2[2,3].plot(data2, pourcentage(places, placestot[0]), label=parking_name)
axs2[2,3].set_xlabel('Temps')
axs2[2,3].set_ylabel('Places disponibles')
axs2[2,3].legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

# Laisser ligne et colonne vide vide
fig2.delaxes(axs2[0, 1])
fig2.delaxes(axs2[0, 2])
fig2.delaxes(axs2[1, 1])
fig2.delaxes(axs2[1, 2])
fig2.delaxes(axs2[1, 0])
fig2.delaxes(axs2[2, 1])
fig2.delaxes(axs2[2, 2])
fig2.delaxes(axs2[1, 3])

# Ajuster la taille du graphique pour laisser de la place à la légende
fig2.subplots_adjust(right=0.7)

# Afficher le graphique
plt.show()

MEF(tableaucor(chargevelodispo(data)))
