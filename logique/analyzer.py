import os
import sys
from .data_loader import DataLoader
from .utils import calculate_proportion_in_percent

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

    # === CALCUL METHODE - SINGLE PARAMETER  ===

    def proportion_one_real(self,realisateur):

        nb_for_realisateur = len(self.data_loader.get_movie_by_realisateur(realisateur))
        
        total_realisateur = self.get_total_realisateur()
            
        proportion = calculate_proportion_in_percent(nb_for_realisateur, total_realisateur)
        return proportion

   

    def proportion_one_sous_genre(self, sous_genre):
        nb_for_sousgenre = len(self.data_loader.get_movie_by_sous_genre(sous_genre))
        
        total_sous_genre = self.get_total_sous_genre()
            
        proportion = calculate_proportion_in_percent(nb_for_sousgenre, total_sous_genre)
        
        return proportion

    # === CALCUL METHODE - INTERVAL PARAMETER ===

    def proportion_annee_range(self, annee_min,annee_max):
        nb_for_years = len(self.data_loader.get_movie_by_years_range(annee_min,annee_max))

        total_annee = self.get_total_annee()
      
        proportion = calculate_proportion_in_percent(nb_for_years, total_annee)
        return proportion



    def proportion_note_range(self,note_min, note_max):
            nb_for_note = len(self.data_loader.get_movie_by_note_range(note_min, note_max))
            
            total_note = self.get_total_note()
                
            proportion = calculate_proportion_in_percent(nb_for_note, total_note)
            return proportion




