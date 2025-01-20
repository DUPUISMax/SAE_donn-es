import requests, time, json

temps=float(input("entrez le nombre de minutes de prise de données : "))
te=float(input("entrez l'intervalle de prise de données : "))
fichiersvoiture = "données/Voiture/"+ input("entrez le nom du fichier pour telechargé les données voiture : ")+".json"
fichiersvelo = "données/Vélo/" + input("entrez le nom du fichier pour telechargé les données vélo : ") +".json"
fichierstps = "données/temps/"+input("entrez le nom du fichier pour le temps : ")+".json"


listevelo, dicovelo2 = [], {}
listevoiture, dicovoiture2 = [], {}
listetps = []
debut = int(time.time())
while int(time.time())-debut< 60*temps:    
    listetps.append(round((time.time()-debut)//60,0))
    headers = {'Cache-Control': 'no-cache'}
    responsevoiture = requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")
    if responsevoiture.status_code != 200: # 200 signifie "OK"
        print("Erreur lors de la requête voiture")
    datavoiture = responsevoiture.json()
    dicovoiture2={}
    for i in range (len(datavoiture)):
       dicovoiture = {
       "ouverture":datavoiture[i]["status"]["value"],
       "place":datavoiture[i]["availableSpotNumber"]["value"],
       "date":datavoiture[i]["availableSpotNumber"]["metadata"]["timestamp"]["value"]
       }
       dicovoiture2[datavoiture[i]["name"]["value"]] = dicovoiture
    listevoiture.append(dicovoiture2)
    
    responsevelo=requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
    
    datavelo = responsevelo.json()
    dicovelo2={}    
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
     
with open(fichiersvelo, 'w') as filevelo:
    json.dump(listevelo, filevelo, ensure_ascii=False, indent=4)

with open(fichierstps, 'w') as filevelo2:
    json.dump(listetps, filevelo2, ensure_ascii=False, indent=4)

with open(fichiersvoiture, 'w') as file:
    json.dump(listevoiture, file, indent=4)
    
