import requests, time, json

temps=float(input("entrez le nombre de minutes de prise de données : "))
te=float(input("entrez l'intervalle de prise de données : "))

fichiersvelo = "données/Vélo/général/" + input("entrez le nom du fichier pour telechargé : ") +".json"
fichiersvelo2 = "données/Vélo/temps/"+ input("entrez le nom du fichier pour le temps : ") +".json"

listevelo, listevelo2, dicovelo2 = [], [], {}

debut = int(time.time())
while int(time.time())-debut< 60*temps:
    responsevelo=requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
    listevelo2.append(round((time.time()-debut)//60,0))
    
    datavelo = responsevelo.json()
    for i in range (len(datavelo)):
       dicovelo={
       "ouverture":datavelo[i]["status"]["value"],
       "velodispo":datavelo[i]["availableBikeNumber"]["value"],
       "placelibre":datavelo[i]["freeSlotNumber"]["value"],
       "date":datavelo[i]["availableBikeNumber"]["metadata"]["timestamp"]["value"]
       }
       dicovelo2[datavelo[i]["address"]["value"]["streetAddress"]]=dicovelo
    listevelo.append(dicovelo2)
    
    print("ok")
    time.sleep(te*60)
     
with open(fichiersvelo, 'w') as file:
    json.dump(listevelo, file, ensure_ascii=False, indent=4)

with open(fichiersvelo2, 'w') as file2:
    json.dump(listevelo2, file2, ensure_ascii=False, indent=4)