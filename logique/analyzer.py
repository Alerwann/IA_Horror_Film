import os
import sys
from .data_loader import DataLoader

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class HorrorAnalyser:
    # ==== INITIALISATION DES DONNEES ====
    def __init__(self):
        """Initialisation des variable"""
        self.data_loader=DataLoader()
        self._total_movie = None
        self._total_annee = None
        self._total_realisateur = None
        self._total_sous_genre = None
        self._total_note = None

    def get_total_movies(self):
        if self._total_movies is None:
            self._total_movies = len(self.data_loader.load_movies())
        return self._total_movies

    def get_total_information_about(self,theme):
        informations = len(self.data_loader.get_all_informations(theme) )
        return informations

    def get_total_note(self):
        if self._total_note is None :
           self._total_note = self.get_total_information_about('note_sur_10')
        return self._total_note

    def get_total_realisateur(self):
        if self._total_realisateur is None:
            self._total_realisateur = self.get_total_information_about('realisateur')
        return self._total_realisateur

    def get_total_sous_genre(self):
        if self._total_sous_genre is None :
            self._total_sous_genre = self.get_total_information_about('sous_genre')
        return self._total_sous_genre

    def get_total_annee(self):
        if self._total_annee is None : 
            self._total_annee = self.get_total_information_about('annee')
        return self._total_annee



        
















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
