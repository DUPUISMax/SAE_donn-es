import requests
import json
import time
temps=float(input("entrez le nombre de minutes de prise de données : "))
te=float(input("entrez l'intervalle de prise de données : "))
fichiers=input("entrez le nom du fichier pour telechargé : ")
fichiers2=input("entrez le nom du fichier pour le temps : ")
fichiers+=".json"
fichiers2+=".json"
liste=[]
liste2=[]
debut = int(time.time())
while int(time.time())-debut< 60*temps:
    response=requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
    liste2.append(round((time.time()-debut)//60,0))
    data = response.json()
    for i in range (len(data)):
       dico={
       'numero':i,
       "adresse":data[i]["address"]["value"]["streetAddress"],
       "ouverture":data[i]["status"]["value"],
       "velodispo":data[i]["availableBikeNumber"]["value"],
       "placelibre":data[i]["freeSlotNumber"]["value"],
       "date":data[i]["availableBikeNumber"]["metadata"]["timestamp"]["value"]
       }
       liste.append(dico)
    
    print("ok")
    time.sleep(te*60) 
with open(fichiers, 'w') as file:
    json.dump(liste, file, indent=4)
with open(fichiers2, 'w') as file2:
    json.dump(liste2, file2, indent=4)