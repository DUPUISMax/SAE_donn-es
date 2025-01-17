import requests, json
responsevelo=requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
datavelo = responsevelo.json() 
listevelo, dicovelo2 = [], {}

for i in range (len(datavelo)):
    dicovelo = {
    "placetotal":datavelo[i]["totalSlotNumber"]["value"],
    "emplacement":datavelo[i]["location"]["value"]["coordinates"]
    }
    dicovelo2[datavelo[i]["address"]["value"]["streetAddress"]]=dicovelo
listevelo.append(dicovelo2)

with open("données/Vélo/placeTotal/placeTotalVélo.json", 'w') as file:
    json.dump(listevelo, file, ensure_ascii=False, indent=4)


responsevoiture=requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")
datavoiture = responsevoiture.json() 
listevoiture, dicovoiture2 = [], {}

for i in range (len(datavoiture)):
    dicovoiture = {
    "placetotal":datavoiture[i]["totalSpotNumber"]["value"],
    "emplacement":datavoiture[i]["location"]["value"]["coordinates"]
    }
    dicovoiture2[datavoiture[i]["name"]["value"]]=dicovoiture
listevoiture.append(dicovoiture2)

with open("données/Voiture/placeTotal/placeTotalVoiture.json", 'w') as file:
    json.dump(listevoiture, file, indent=4)
