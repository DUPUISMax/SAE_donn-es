import requests, json
response=requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
data = response.json() 
liste, dico, dico2 = [], {}, {}

for i in range (len(data)):
    dico = {
    "placetotal":data[i]["totalSlotNumber"]["value"],
    "emplacement":data[i]["location"]["value"]["coordinates"]
    }
    dico2[data[i]["address"]["value"]["streetAddress"]]=dico
liste.append(dico2)

with open("données/Vélo/placeTotal/placeTotalVélo.json", 'w') as file:
    json.dump(liste, file, ensure_ascii=False, indent=4)