# clean_data.py
import os
import pandas as pd

def clean_data(raw_file_path, cleaned_file_path):
    """Nettoie les données brutes, supprime les enregistrements avec des valeurs manquantes, 
    et les enregistre dans un format exploitable pour le tableau de bord."""
    
    try:
        # Chargement des données brutes
        df = pd.read_csv(raw_file_path, delimiter=';', decimal=',')
        
        # Suppression des lignes avec des valeurs manquantes dans toutes les colonnes
        df.dropna(inplace=True)
        
        # Conversion et nettoyage des colonnes
        df['jour'] = df['jour'].astype(int)
        df['mois'] = df['mois'].astype(int)
        df['an'] = df['an'].astype(int)
        df['hrmn'] = pd.to_datetime(df['hrmn'], format='%H:%M', errors='coerce').dt.time
        df['lat'] = pd.to_numeric(df['lat'].astype(str).str.replace(',', '.'), errors='coerce')
        df['long'] = pd.to_numeric(df['long'].astype(str).str.replace(',', '.'), errors='coerce')
        
        # Renommage des colonnes pour plus de clarté
        df.rename(columns={
            'Accident_Id': 'AccidentID',
            'jour': 'Jour',
            'mois': 'Mois',
            'an': 'An',
            'hrmn': 'HeureMinute',
            'lum': 'Lumiere',
            'dep': 'Departement',
            'com': 'Commune',
            'agg': 'ZoneAgglomeration',
            'int': 'Intersection',
            'atm': 'ConditionsAtmospheriques',
            'col': 'TypeCollision',
            'adr': 'Adresse'
        }, inplace=True)
        
        # Enregistrement des données nettoyées
        df.to_csv(cleaned_file_path, index=False)
        print(f"Les données nettoyées ont été enregistrées dans : {cleaned_file_path}")
    
    except Exception as e:
        print("Erreur lors du nettoyage des données :", e)

def load_and_clean_data(cleaned_file_path):
    """Charge les données nettoyées depuis le fichier CSV."""
    try:
        df = pd.read_csv(cleaned_file_path)
        df['HeureMinute'] = pd.to_datetime(df['HeureMinute'], format='%H:%M:%S', errors='coerce')
        return df
    except Exception as e:
        print("Erreur lors du chargement des données nettoyées :", e)
        return None

# Chemin vers les fichiers bruts et nettoyés
if __name__ == "__main__":
    raw_file_path = "data/raw/dataset.csv"
    cleaned_file_path = "data/cleaned/cleaned_dataset.csv"
    clean_data(raw_file_path, cleaned_file_path)

