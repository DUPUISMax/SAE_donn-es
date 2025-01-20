from module import * 
<<<<<<< Updated upstream
import matplotlib.pyplot as plt
=======
from matplotlib import pyplot as plt
>>>>>>> Stashed changes
import json

# Charger les données du fichier JSON
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
for entry in data3: 
    for parking_name, parking_info in entry.items():
        if parking_name not in parkingstot:
            parkingstot[parking_name] = []
        parkingstot[parking_name].append(parking_info['placetotal'])
#print(parkings)
# Afficher les places pour chaque parking
<<<<<<< Updated upstream
#for parking_name, places in parkings.items():
#    print(courbe(data2,places, parking_name)):
for parking_name, places in parkings.items():
    plt.plot(data2, places, label=parking_name,)
plt.xlabel('Temps')
plt.ylabel('Places disponibles')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

fig = plt.gcf()  # Récupérer la figure actuelle
fig.subplots_adjust(right=0.7)  # Ajuster la taille du graphique pour laisser de la place à la légende
plt.title('Nombre de places disponibles par parking')

plt.show()

                   
=======
# for parking_name, places in parkings.items():
#     print(courbe(data2,places, parking_name))
>>>>>>> Stashed changes

# Charger les données du fichier JSON
with open('données/Voiture/test2.json', 'r') as file:
    data = json.load(file)

# Définir les temps en heures (par exemple)
temps = ["1h", "2h", "3h", "4h", "5h"]

# Créer un graphique
plt.figure(figsize=(12, 8))  # Taille du graphique

# Tracer les courbes pour chaque parking
for parking, places in data.items():
    # Les données pour chaque parking sont des listes de places, donc on les trace
    plt.plot(temps, places, marker='o', linestyle='-', label=parking)

# Ajouter des labels et un titre
plt.xlabel('Temps')
plt.ylabel('Places Disponibles')
plt.title('Disponibilité des Places par Parking en Fonction du Temps')

# Ajouter une légende
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))  # Légende à l'extérieur du graphique

# Afficher le graphique
plt.grid(True)
plt.tight_layout()  # Pour éviter que la légende se chevauche avec le graphique
plt.show()
