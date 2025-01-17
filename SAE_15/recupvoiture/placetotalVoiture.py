import requests, json
response=requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")
data = response.json() 
liste, dico, dico2 = [], {}, {}

for i in range (len(data)):
    dico = {
    "placetotal":data[i]["totalSpotNumber"]["value"],
    "emplacement":data[i]["location"]["value"]["coordinates"]
    }
    dico2[data[i]["name"]["value"]]=dico
liste.append(dico2)

with open("SAE_15/données/Voiture/placeTotal/placeTotalVoiture.json", 'w') as file:
    json.dump(liste, file, indent=4)
