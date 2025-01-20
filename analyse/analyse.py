from module import * 
import matplotlib.pyplot as plt
import json

# Charger les données du fichier JSON
with open('données/Voiture/17.01.20h.json', 'r') as file:
with open('données/Voiture/test2.json', 'r') as file:
    data = json.load(file)
with open('données/Temps/test2.json', 'r') as file:
    data2 = json.load(file)
# Initialiser un dictionnaire pour stocker les places par parking
parkings = {}

# Récupérer les places de chaque parking
for entry in data:
    for parking_name, parking_info in entry.items():
        if parking_name not in parkings:
            parkings[parking_name] = []
        parkings[parking_name].append(parking_info['place'])
<<<<<<< HEAD
for entry in data3: 
    for parking_name, parking_info in entry.items():
        if parking_name not in parkingstot:
            parkingstot[parking_name] = []
        parkingstot[parking_name].append(parking_info['placetotal'])
#print(parkings)
=======

>>>>>>> parent of 33295b1 (enfin)
# Afficher les places pour chaque parking
#for parking_name, places in parkings.items():
#    print(courbe(data2,places, parking_name)):
for parking_name, places in parkings.items():
<<<<<<< HEAD
    plt.plot(data2, places, label=parking_name)
plt.show()

                
                
=======
    print(courbe(data2,places, parking_name))
>>>>>>> parent of 33295b1 (enfin)






        
    
    