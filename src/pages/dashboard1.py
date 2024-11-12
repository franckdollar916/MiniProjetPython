# src/pages/dashboard1.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.express as px
from io import BytesIO
import base64
import folium
from folium.plugins import MarkerCluster

# Fonction pour convertir une figure matplotlib en image encodée pour Dash
def matplotlib_to_dash(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    img = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close(fig)  # Fermeture de la figure après l'avoir enregistrée
    return "data:image/png;base64,{}".format(img)

def create_dashboard(data_path):
    # Charger les données nettoyées
    data = pd.read_csv(data_path)

    # Initialiser l'application Dash
    app = dash.Dash(__name__)

    # Layout du dashboard
    app.layout = html.Div([
        html.H1("Dashboard des Accidents"),

        # Étude temporelle
        html.H2("1. Étude temporelle"),
        dcc.Graph(id="accidents_by_month"),
        dcc.Graph(id="accidents_by_hour"),

        # Conditions environnementales
        html.H2("2. Conditions environnementales"),
        html.Img(id="accidents_by_luminosity"),
        html.Img(id="accidents_by_weather"),

        # Sélecteur de mois pour la carte
        html.H2("Sélectionner un mois pour afficher les accidents"),
        dcc.Dropdown(
            id="month_selector",
            options=[{'label': str(i), 'value': i} for i in range(1, 13)],  # Options de mois de 1 à 12
            value=1,  # Mois initial sélectionné
            style={'width': '50%'}
        ),

        # Localisation des accidents
        html.H2("3. Localisation des accidents"),
        html.Iframe(id="accidents_map", srcDoc=None, width="100%", height="600"),

        # Types de collisions et de routes
        html.H2("4. Types de collisions et de routes"),
        html.Img(id="collision_types"),
        html.Img(id="collisions_by_intersection"),
    ])

    # Callback pour mettre à jour les graphiques et la carte
    @app.callback(
        [Output("accidents_by_month", "figure"),
         Output("accidents_by_hour", "figure"),
         Output("accidents_by_luminosity", "src"),
         Output("accidents_by_weather", "src"),
         Output("accidents_map", "srcDoc"),
         Output("collision_types", "src"),
         Output("collisions_by_intersection", "src")],
        [Input("month_selector", "value")]  # Utilisation du mois sélectionné comme entrée
    )
    def update_charts(selected_month):
        # Étude temporelle avec Plotly - Nombre d'accidents par mois
        fig_month = px.histogram(
            data, 
            x="Mois", 
            title="Nombre d'accidents par mois", 
            color="Mois",  
            color_discrete_sequence=px.colors.qualitative.Set1  
        )

        # Étude temporelle avec Plotly - Nombre d'accidents par heure
        data['Heure'] = data['HeureMinute'].str[:2].astype(int)
        fig_hour = px.histogram(
            data, 
            x="Heure", 
            title="Nombre d'accidents par heure", 
            category_orders={"Heure": list(range(0, 24))},
            color="Heure",  
            color_discrete_sequence=px.colors.qualitative.Plotly  
        )

        # Conditions environnementales avec Matplotlib
        # Accidents par luminosité
        fig_luminosity = plt.figure(figsize=(8, 4))
        data['Lumiere'].value_counts().plot(kind="bar", color="skyblue", ax=fig_luminosity.gca())
        plt.title("Accidents par conditions de luminosité")
        plt.xlabel("Luminosité")
        plt.ylabel("Nombre d'accidents")
        luminosity_img = matplotlib_to_dash(fig_luminosity)

        # Accidents par conditions météorologiques
        fig_weather = plt.figure(figsize=(8, 4))
        data['ConditionsAtmospheriques'].value_counts().plot(kind="bar", color="salmon", ax=fig_weather.gca())
        plt.title("Accidents par conditions météorologiques")
        plt.xlabel("Conditions météorologiques")
        plt.ylabel("Nombre d'accidents")
        weather_img = matplotlib_to_dash(fig_weather)

        # Localisation des accidents avec Folium
        filtered_data = data[data['Mois'] == selected_month]
        accident_map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
        marker_cluster = MarkerCluster().add_to(accident_map)
        for _, row in filtered_data.iterrows():
            folium.Marker(
                location=[row['lat'], row['long']],
                popup=f"Accident ID: {row['AccidentID']}",
                icon=folium.Icon(color="red")
            ).add_to(marker_cluster)
        map_html = accident_map._repr_html_()

        # Types de collisions
        fig_collision = plt.figure(figsize=(8, 4))
        data['TypeCollision'].value_counts().plot(kind="bar", color="lightgreen", ax=fig_collision.gca())
        plt.title("Types de collisions")
        plt.xlabel("Type de collision")
        plt.ylabel("Nombre d'accidents")
        collision_img = matplotlib_to_dash(fig_collision)

        # Types d'intersections
        fig_intersection = plt.figure(figsize=(8, 4))
        data['Intersection'].value_counts().plot(kind="bar", color="purple", ax=fig_intersection.gca())
        plt.title("Accidents par type d'intersection")
        plt.xlabel("Type d'intersection")
        plt.ylabel("Nombre d'accidents")
        intersection_img = matplotlib_to_dash(fig_intersection)

        return fig_month, fig_hour, luminosity_img, weather_img, map_html, collision_img, intersection_img

    # Exécuter le serveur Dash
    app.run_server(debug=True)

    return app


