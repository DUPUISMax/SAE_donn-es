import requests, time, json
import sys

# TODO:  ##### COMMENTEZ TOUJOURS TOUT !!!!!!!!! #####
#  du code sans commentaire c'est relou as fuck

# TODO: foutez moi ses constantes dans un fichier de conf que vous importez ici

temps = float(input("entrez le nombre de minutes de prise de données : "))
te = float(input("entrez l'intervalle de prise de données : "))
fichiersvoiture = "données/Voiture/" + input(
    "entrez le nom du fichier pour telechargé les données voiture : ") + ".json"
fichiersvelo = "données/Vélo/" + input(
    "entrez le nom du fichier pour telechargé les données vélo : ") + ".json"
fichierstps = "données/Temps/" + input(
    "entrez le nom du fichier pour le temps : ") + ".json"

debut = int(time.time())

def hydrate_json_file(file_path, datas):
    """
    Fonction pour hydrater un fichier JSON
    :param file_path: Chemin fichier cible
    :param datas: Données
    """
    try:
        # Charge les données existantes
        with open(file_path, 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []  # Si le fichier est vide ou mal formaté, commencer par une liste vide
            # Ajoute les nouvelles données
            data.extend(datas)
            # Réinitialise le fichier et hydrate les données
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.truncate()
    except FileNotFoundError:
        # Si le fichier n'existe pas, créer une nouvelle liste
        with open(file_path, 'w') as file:
            json.dump(datas, file, ensure_ascii=False, indent=4)


def timer(minutes):
    """
    Fonction pour le minuteur, contrôle l'attente avant relance d'une prise de donnée
    :param minutes: intervalle en minutes
    """
    total_seconds = int(minutes) * 60  # Minutes en secondes et etre sur que c'est un int
    time_frames = ['◯', '◝', '◞', '◟', '◜']
    start_time = time.time()
    while total_seconds > 0:
        min_left = total_seconds // 60
        sec_left = total_seconds % 60
        timer = f"{int(min_left)}:{int(sec_left):02}"
        sys.stdout.write(f"\rProchaine passe dans : {time_frames[int(time.time() - start_time) % len(time_frames)]} {timer}")  # Met à jour le timer
        sys.stdout.flush()
        time.sleep(1)  # Attendre 1 seconde avant refresh
        total_seconds -= 1


while int(time.time()) - debut < 60 * temps:
    # On purge list/dict à chaque passe vu qu'on réhydrate les fichiers JSON
    listevelo, dicovelo2 = [], {}
    listevoiture, dicovoiture2 = [], {}
    listetps = []

    listetps.append(round((time.time() - debut) // 60, 0))
    headers = {'Cache-Control': 'no-cache'}
    responsevoiture = requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000")
    if responsevoiture.status_code != 200:  # 200 signifie "OK"
        print("Erreur lors de la requête voiture")

        # TODO: ¯\_(ツ)_/¯
        #  euhhhhhhh ou est la procédure en cas d'échec de l'API ? car la ça crash purement et simplement
        #  il faut re intérroger l'API avec une intervalle jusqu'à ce quelle réponde OK (try / except)

    datavoiture = responsevoiture.json()

    # TODO : enumerate (python)
    #  fruits = ['pomme', 'banane', 'orange']
    #  for index, fruit in enumerate(fruits):
    #      print(index, fruit)
    #  sortie : 0 pomme, 1 banane, 2 orange

    dicovoiture2 = {}
    for index, voiture in enumerate(datavoiture):
        dicovoiture = {
            "ouverture": voiture["status"]["value"],
            "place": voiture["availableSpotNumber"]["value"],
            "date": voiture["availableSpotNumber"]["metadata"]["timestamp"]["value"]
        }
        dicovoiture2[voiture["name"]["value"]] = dicovoiture
    listevoiture.append(dicovoiture2)

    responsevelo = requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
    # TODO : IDEM ICI !!! cas d'échec de l'API ? osef ¯\_(ツ)_/¯

    datavelo = responsevelo.json()
    dicovelo2 = {}

    # TODO : voir enumerate (python)
    for index, velo in enumerate(datavelo):
        dicovelo = {
            "ouverture": velo["status"]["value"],
            "velodispo": velo["availableBikeNumber"]["value"],
            "placelibre": velo["freeSlotNumber"]["value"],
            "date": velo["availableBikeNumber"]["metadata"]["timestamp"]["value"]
        }
        dicovelo2[velo["address"]["value"]["streetAddress"]] = dicovelo
    listevelo.append(dicovelo2)

    # Appel la fonction pour hydrater chaque fichier
    hydrate_json_file(fichiersvelo, listevelo)
    hydrate_json_file(fichierstps, listetps)
    hydrate_json_file(fichiersvoiture, listevoiture)

    # Appel la fonction minuteur / prochaine passe
    timer(te)

# TODO: à quel moment vous vous etes dit que laisser les datas en cache mémoire pendant toute la prise de donnée était une putain de bonne idée ???!!!
#  ça sert à rien de remplir une liste à chaque passe, il suffit de réhydraté le fichier JSON à chaque passe et purger les listes/dicos sinon vous allez coucher les perfs et potentiellement le serveur
#  PS : en prog il y a une convention de nommage qui dit que tout code doit être écrit en anglais (c'est pas vrais, mais faites le putain !)
#  en python on met des '_' dans les noms de variable ex: 'responsevelo' devrait être 'response_velo' ou encore mieux 'res_bike' c'est franchement plus élégant et facile à lire