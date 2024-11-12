# get_data.py
import requests
import os

def download_raw_data(url, save_path):
    """Télécharge un fichier CSV brut depuis une URL et l'enregistre localement."""
    
    # Crée le répertoire si nécessaire
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    
    try:
        # Télécharge le fichier
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs de téléchargement
        
        # Sauvegarde du contenu brut dans le fichier
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Les données ont été téléchargées et enregistrées dans : {save_path}")
    
    except requests.exceptions.RequestException as e:
        print("Erreur lors du téléchargement des données :", e)

# URL des données et chemin de stockage
if __name__ == "__main__":
    csv_url = "https://www.data.gouv.fr/fr/datasets/r/5fc299c0-4598-4c29-b74c-6a67b0cc27e7"
    save_path = "data/raw/dataset.csv"
    download_raw_data(csv_url, save_path)
