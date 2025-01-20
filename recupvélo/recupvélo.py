import requests, time, json

temps=float(input("entrez le nombre de minutes de prise de données : "))
te=float(input("entrez l'intervalle de prise de données : "))

fichiers = "données/Vélo/général/" + input("entrez le nom du fichier pour telechargé : ") +".json"
fichiers2 = "données/Vélo/temps/"+ input("entrez le nom du fichier pour le temps : ") +".json"

liste, liste2, dico2 = [], [], {}

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
       dico2[data[i]["address"]["value"]["streetAddress"]]=dico
    liste.append(dico2)
    
    print("ok")
    time.sleep(te*60)
     
with open(fichiers, 'w') as file:
    json.dump(liste, file, ensure_ascii=False, indent=4)

with open(fichiers2, 'w') as file2:
    json.dump(liste2, file2, ensure_ascii=False, indent=4)
