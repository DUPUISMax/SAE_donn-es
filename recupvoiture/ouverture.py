import requests
import json
import time
temps=float(input("entrez le nombre de minutes de prise de données : "))
te=float(input("entrez l'intervalle de prise de données : "))
fichiers=input("entrez le nom du fichier pour telechargé : ")
fichiers2=input("entrez le nom du fichier pour le temps : ")
fichiers2+=".json"
fichiers+=".json"
liste=[]
liste2=[]
dico={}
debut = int(time.time())
while int(time.time())-debut< 60*temps:
    liste2.append(round((time.time()-debut)//60,0))
    
    response=requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")
    data = response.json()
    for i in range (len(data)):
       dico2={
       "nom":data[i]["name"]["value"],
       "ouverture":data[i]["status"]["value"],
       "place":data[i]["availableSpotNumber"]["value"],
       "date":data[i]["availableSpotNumber"]["metadata"]["timestamp"]["value"]
       }
       liste.append(dico2)

    print("ok")
    time.sleep(te*60)
with open(fichiers, 'w') as file:
    json.dump(liste, file, indent=4)
with open(fichiers2, 'w') as file2:
    json.dump(liste2, file2, indent=4)