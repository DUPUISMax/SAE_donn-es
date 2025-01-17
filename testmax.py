import time

def obtenir_heure_actuelle_formattee():
  """Retourne une chaîne de caractères représentant l'heure actuelle au format HH:MM:SS."""
  return time.strftime("%H:%M", time.localtime())

# Exemple d'utilisation
heure_formattee = obtenir_heure_actuelle_formattee()
print("L'heure actuelle est :", heure_formattee)