# Imports depuis le sous-dossier `utils` pour le téléchargement et le nettoyage des données
from src.utils.get_data import download_raw_data
from src.utils.clean_data import clean_data

# Import depuis le sous-dossier `pages` pour le dashboard
from src.pages.dashboard1 import create_dashboard

# Chemins de fichiers
url = "https://www.data.gouv.fr/fr/datasets/r/5fc299c0-4598-4c29-b74c-6a67b0cc27e7"
raw_data_path = "data/raw/dataset.csv"
cleaned_data_path = "data/cleaned/cleaned_dataset.csv"

# Télécharger les données
download_raw_data(url, raw_data_path)

# Nettoyer les données
clean_data(raw_data_path, cleaned_data_path)

# Lancer le dashboard (vérifiez que `create_dashboard` est bien une fonction dans `dashboard1.py`)
create_dashboard(cleaned_data_path)
