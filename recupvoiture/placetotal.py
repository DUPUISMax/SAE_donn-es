import requests
import json
response=requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")
data = response.json() 
liste=[]
dico={}
for i in range (len(data)):
    dico={
    "nom":data[i]["name"]["value"],
    "placetotal":data[i]["totalSpotNumber"]["value"],
    "emplacement":data[i]["location"]["value"]["coordinates"]
    }
    liste.append(dico)
with open("placetotal.json", 'w') as file:
    json.dump(liste, file, indent=4)
