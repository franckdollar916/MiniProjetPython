
---

# Dashboard des Accidents de la Route

Ce projet contient un dashboard  pour visualiser et analyser les données d'accidents de la route, développé en utilisant Dash, Plotly, et Folium.

## User Guide

### Prérequis
- **Python** 3.7 ou supérieur
- Les bibliothèques Python suivantes :
  - `dash`
  - `pandas`
  - `plotly`
  - `folium`

### Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/franckdollar916/MiniProjetPython.git
   cd dashboard-accidents
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

### Déploiement et Exécution

1. Lancez le fichier principal `main.py` pour démarrer le serveur :
   ```bash
   python main.py
   ```
2. Accédez au dashboard via votre navigateur à l'adresse [http://127.0.0.1:8050](http://127.0.0.1:8050).

## Data

### Description des Données
Les données utilisées proviennent de la plateforme Data.gouv qui contient des informations sur les données annuelles caractéristiques des accidents corporels de la circulation routière (Année de 2022). Les colonnes incluent :
- **Mois** : Mois de l'année où l'accident s'est produit.
- **HeureMinute** : Heure de l'accident, sous format HH:MM.
- **Lumiere** : Conditions de luminosité au moment de l'accident.
- **ConditionsAtmospheriques** : Conditions météorologiques au moment de l'accident.
- **lat** et **long** : Coordonnées géographiques de l'accident.
- **TypeCollision** : Type de collision.
- **Intersection** : Type d'intersection où l'accident a eu lieu (si applicable).

Les données doivent être nettoyées et formatées pour correspondre à ces colonnes afin d'assurer le bon fonctionnement du dashboard.

## Developer Guide

### Architecture du Code
- `main.py` : Fichier principal pour exécuter le dashboard. Ce fichier appelle la fonction `create_dashboard` du module `dashboard1.py`.
- `src/pages/dashboard1.py` : Contient le code du dashboard, avec des graphiques pour l'analyse temporelle, les conditions environnementales, la localisation géographique des accidents, et les types de collisions.
- `data/cleaned/cleaned_dataset.csv` : Chemin vers les données nettoyées utilisées dans le dashboard.

### Ajouter une Nouvelle Page
1. Créez un nouveau fichier dans `src/pages/`, par exemple `dashboard2.py`.
2. Utilisez Dash pour définir un nouveau layout et ajouter des graphiques ou visualisations spécifiques.
3. Modifiez `main.py` pour importer et appeler votre nouvelle page ou intégrez-la en utilisant un composant de navigation de Dash.

### Ajouter un Nouveau Graphique
1. Dans `dashboard1.py`, ajoutez votre graphique dans la fonction `update_charts` ou une nouvelle fonction de callback si nécessaire.
2. Créez votre figure avec Plotly ou Matplotlib.
3. Utilisez `dcc.Graph` pour les graphiques Plotly ou `html.Img` pour les graphiques Matplotlib, en les ajoutant au layout du dashboard.

## Rapport d'Analyse

### Analyse Temporelle
- Le graphique montre une distribution des accidents par mois. Nous observons une légère augmentation pendant les mois d'été (mai à août) et une baisse en hiver. Cette tendance pourrait indiquer que la saisonnalité affecte la fréquence des accidents, possiblement en raison des conditions météorologiques, de l'afflux touristique, ou d'autres facteurs saisonniers.

### Analyse Horaire
- Les accidents se produisent principalement aux heures de pointe (8h-9h et 17h-18h), ce qui correspond aux périodes de forte affluence routière en lien avec les trajets domicile-travail.

### Conditions Environnementales
- En termes de luminosité, les accidents se produisent souvent en journée, mais il y a aussi une proportion notable d'accidents dans des conditions de faible luminosité (nuit ou crépuscule).
- Les conditions météorologiques influent également sur les accidents, avec davantage d'accidents signalés sous la pluie ou par mauvais temps.

### Localisation Géographique
- La carte interactive montre les zones à risque avec un grand nombre d'accidents dans les grandes villes et les zones denses.

### Types de Collisions
- Les types de collisions les plus courants sont les collisions arrière et latérales. Cela peut être lié à la densité de trafic, aux intersections et aux limitations de vitesse.

Ces conclusions peuvent être utilisées pour recommander des interventions de sécurité routière, telles que l'amélioration de l'éclairage dans les zones accidentogènes, la signalisation renforcée aux intersections, et des campagnes de prévention pendant les périodes d'affluence.

--- 
