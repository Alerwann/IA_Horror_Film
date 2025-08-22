import os
import sys
from .data_loader import DataLoader

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class HorrorAnalyser:
    def __init__(self):
        """Initialisation des variable"""
    # note il faudrait que je trouve un moyen pour parcourir le tableau pour trouver que en parcourrant horrorfilm je puisse identifier tous les real, sous genre pour faire un classement

    def stat_by_real(self, realisateur):
        """ 
        calcule le nombre de film d'un realisateur dans la liste
        """

    def stat_by_date(self, date=[int,int]):
        """
        calcule le nombre de film a une date donnée
        
        note: pour ameliorer faire une recherche par periode dans data loader
        """

    def stat_by_note(self, note=[int, int]):
        """
        calcule le nombre de film qui ont une note donnée
        
        note : ajouter une recherche par interval dans note pour collé avec les seuils de note du settings
        """

    def stat_by_genre(self, sous_genre):
        """
        Calcul le nombre de film qui ont un certain sous-genre
        """

    def calcul_stat(self, nb_film_spé):
        """ calcul du rapport de film spécifique sur la totalité"""

    def response_stat(self):
        """Renvoie un compte rendu des réponse soit global soit précis"""