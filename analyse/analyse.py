from module import * 
import matplotlib.pyplot as plt
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
#for parking_name, places in parkings.items():
#    print(courbe(data2,places, parking_name)):
for parking_name, places in parkings.items():
    for parking_name_tot, placestot  in parkingstot.items():
        if parking_name == parking_name_tot:   
            plt.plot(data2,pourcentage(places, placestot[0]), label=parking_name,)
plt.xlabel('Temps')
plt.ylabel('Places disponibles')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=2)

fig = plt.gcf()  # Récupérer la figure actuelle
fig.subplots_adjust(right=0.7)  # Ajuster la taille du graphique pour laisser de la place à la légende
plt.title('Nombre de places disponibles par parking')

plt.show()

