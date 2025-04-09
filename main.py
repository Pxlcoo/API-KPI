import requests

# Adresse de l'API
url = "http://10.101.1.116:8000/kpis"

try:
    # Effectuer la requête GET
    response = requests.get(url)

    # Vérifier le statut de la réponse
    if response.status_code == 200:
        # Si la requête est un succès, traiter les données JSON
        data = response.json()  # Convertir la réponse en dictionnaire Python
        print("Données récupérées depuis l'API :")
        print(data)
    else:
        print(f"Erreur : Statut {response.status_code} - Impossible de récupérer les données.")
except requests.exceptions.RequestException as e:
    print(f"Une erreur est survenue lors de la requête : {e}")
