import matplotlib.pyplot as plt
import json
from module import *

with open('données/Vélo/22.01.8h00.json', 'r') as file:
    data_velo = json.load(file)

with open('données/Voiture/22.01.8h00.json', 'r') as file:
    data_voiture = json.load(file)

tableauvoiture = chargevoiture(data_voiture)
tableauvelo = chargeveloplace(data_velo)

MEFcroisee(tableaucor(tableauvoiture), tableaucor(tableauvelo))