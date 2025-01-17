import requests, json, time, os

temps = float(input("entrez le nombre de minutes de prise de données : "))
te = float(input("entrez l'intervalle de prise de données : "))

fichiers = "données/Voiture/général/"+ input("entrez le nom du fichier pour telechargé : ")+".json"
fichiers2 = "données/Voiture/temps/"+input("entrez le nom du fichier pour le temps : ")+".json"

liste, liste2, dico, dico2 = [], [], {},{}

debut = int(time.time())
while int(time.time()) - debut < 60*temps:
    liste2.append(round((time.time() - debut) // 60,0))
    response = requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")
    
    data = response.json()
    for i in range (len(data)):
       dico = {
       "ouverture":data[i]["status"]["value"],
       "place":data[i]["availableSpotNumber"]["value"],
       "date":data[i]["availableSpotNumber"]["metadata"]["timestamp"]["value"]
       }
       dico2[data[i]["name"]["value"]] = dico
    liste.append(dico2)

    print("ok")
    time.sleep(te*60)

with open(fichiers, 'w') as file:
    json.dump(liste, file, indent=4)
    
with open(fichiers2, 'w') as file2:
    json.dump(liste2, file2, indent=4)
