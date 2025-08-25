import os
import sys
import csv
from pathlib import Path
from typing import List, Optional
from pathlib import Path


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.settings import COLONNES
from logique.horror_movie import HorrorMovie
from logique.utils import verif_var_int, verif_order_int, str_strip_lower


class DataLoader:

    # === INITIALISATION ===

    def __init__(self):
        """Initialisation des variables necessaires pour la classe"""
        
        self.movies = []
        self.is_loaded = False

        if getattr(sys, "frozen", False):
            # Mode PyInstaller
            self.csv_path = Path(sys._MEIPASS) / "data" / "My_horror_film.csv" # type: ignore
        else:
            # Mode développement
            self.csv_path= Path(__file__).parent.parent / "data" / "My_horror_film.csv"

    

    def load_movies(self):
        """
        Importe le liste des films et leurs caractéristiques au format csv

        Utilise CSV pour le traitement du fichier et convertir chaque ligne en dict

        Returns:
            [obj,...,obj] -> retourne un tableau de objet.
            Chaque objet est un HorrorMovie

        Raises:
            FileNotFoundError: Si le fichier CSV n'existe pas
        """
        movies = []

        if not Path(self.csv_path).exists():
            raise FileNotFoundError(f"Le fichier CSV est introuvable : {self.csv_path}")

        with open(self.csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                movies.append(
                    HorrorMovie(
                        row["Titre"],
                        row["Année"],
                        row["Réalisateur"],
                        row["Sous_genre"],
                        row["Note sur 10"],
                    )
                )

        self.movies = movies
        self.is_loaded = True

        return self.movies

    # === CORS METHODE ===

    def get_movie_range(self, search_type, var_min, var_max):
        """
        Parcours la liste de movies qu'il aura chargé pour trouver l'ensemble des films selon un interval de paramètres demandé

        Args:
            - search_type(str) : Nom de l'attribut qui est sujet de la recherche
            - var_min(int): Valeur minimal de l'interval
            - var_max(int): Valeur maximal de l'interval

        Return:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note :
                - retourne un tableau vide si aucun film

        """
        if not self.is_loaded:
            self.load_movies()

        search_movies = []

        for film in self.movies:
            film_value = getattr(film, search_type)
            if film_value is not None and var_min <= film_value <= var_max:
                search_movies.append(film)
        return search_movies

    def get_all_informations(self, search):
        """
        Retoune une liste de toutes les valeurs uniques d'un attribut

        Ags:
            search(str) : Nom de l'attribut à extraire (peut être : titre, annee, sous_genre, note_sur_10, realisateur)

        Returns:
            all_infos[str] : Liste sans doublon des valeurs
        """
        all_infos = []
        if not self.is_loaded:
            self.load_movies()

        for film in self.movies:
            search_value = getattr(film, search)
            if search_value not in all_infos:
                all_infos.append(search_value)
        return all_infos

    def get_movie(self, search_type, search):
        """
        Parcours la liste de movies qu'il aura chargé pour trouver l'ensemble des films selon les paramètres demandé

        Args:
            - search_type(str) : Nom de l'attribut qui est sujet de la recherche
            - search(str ou int): Valeur de l'attribut qui est recherché

        Return:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note :
                - retourne un tableau vide si aucun film
        """
        if not self.is_loaded:
            self.load_movies()

        search_movies = []

        for film in self.movies:
            if getattr(film, search_type) == search:
                search_movies.append(film)

        return search_movies

    # ==== SEARCH METHODS - GLOBAL PARAMETER ===

    def get_all_realisateurs(self):
        """ Fonction permettant de retourner une liste de nom des realisateurs"""
        all_real = self.get_all_informations('realisateur')
        return all_real

    def get_all_years(self):
        """Fonction permettant de retourner une liste unique des années"""
        all_years= self.get_all_informations('annee')
        return all_years

    def get_all_note(self):
        """Fonction permettant de retourner une liste unique des notes"""
        all_notes = self.get_all_informations('note_sur_10')
        return all_notes

    def get_all_sous_genre(self):
        """Fonction permettant de retourner une liste des sous-genre"""
        all_ssgenre = self.get_all_informations('sous_genre')
        return all_ssgenre

    # === SEARCH METHODS - SINGLE PARAMETER ===

    def get_movie_by_realisateur(self, real):
        """
        Parcours l'ensemble des films chargé pour retourné ceux qui ont été réalisé par un réalisateur donné
        Fait appel à get_movie() pour obtenir les résultats
        Fait appel a str_strip_lower pour que la donnée soit vérifiée, les espaces de début et fin supprimés, mis en minuscule


        Args:
            real(str) : Le nom du realisateur donné est modifié pour supprimer les espaces de début et fin

        Retur:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note : retourne un tableau vide si aucun film avec ce réalisateur
        """
        realisateurs = str_strip_lower(real)
        return self.get_movie("realisateur", realisateurs)

    def get_movie_by_sous_genre(self, sous_genre):
        """
        Parcours l'ensemble des films chargé pour retourné ceux qui ont un sous-genre donné
        Fait appel à get_movie() pour obtenir les résultats
        Fait appel a str_strip_lower pour que la donnée soit vérifiée, les espaces de début et fin supprimés, mis en minuscule

        Args:
            sous_genre(str) : Le sous-genre est modifié pour supprimer les espaces de début et fin

        Retur:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note : retourne un tableau vide si aucun film trouvé
        """
        sousgenre = str_strip_lower(sous_genre)
        return self.get_movie("sous_genre", sousgenre)

    def get_movie_by_titre(self, titre):
        """
        Parcours l'ensemble des films chargé pour retourné ceux qui ont un titre donné
        Fait appel à get_movie() pour obtenir les résultats
        Fait appel a str_strip_lower pour que la donnée soit vérifiée, les espaces de début et fin supprimés, mis en minuscule

        Args:
            titre(str) : Le sous-genre est modifié pour supprimer les espaces de début et fin

        Retur:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note :
            - retourne un tableau vide si aucun film trouvé
            - peut permettre de vérifier si doublons d'insertion
        """
        titres = str_strip_lower(titre)
        return self.get_movie("titre", titres)

    # === SEARCH METHODS - MULTI PARAMETER ===

    def get_movie_by_years_range(self, annee_min, annee_max):
        """
            Parcours l'ensemble des films chargé pour retourné ceux qui sont sortie sur une période ou une année précise
            Fait appel à get_movie() pour obtenir les résultats
            Fait appel à verif_var_int() pour vérifié que la donnée peut être traduit en int

            Args:
                annee_min(int or str), annee_max(int,str): annee donnée par utilisateur pour la plage de recherche.
                si besoin d'une valeur précise : faire la recherche avec la même valeur pour les 2 args

            Retur:
                [obj, ... obj] -> list d'objet HorrorMovie

            Note : retourne une liste vide si aucun film trouvé
            """
        annee_min = verif_var_int(annee_min)
        annee_max = verif_var_int(annee_max)

        films = []

        annee_min, annee_max = verif_order_int(annee_min, annee_max)

        films = self.get_movie_range("annee", annee_min, annee_max)

        return films

    def get_movie_by_note_range(self, note_min, note_max):
        """
            Fonction qui permet de retourner l'ensembles des films aynt un interval de note ou une note précise
            Fait appel à get_movie() pour obtenir les résultats
            Fait appel à verif_var_int() pour vérifié que la donnée peut être traduit en int

            Args:
                note_min(int or str), note_max(int,str): note donnée par utilisateur pour la plage de recherche.
                si besoin d'une valeur précise : faire la recherche avec la même valeur pour les 2 args

            Return:
                [obj, ... obj] -> tableau d'objet HorrorMovie

            Note :
                - retourne un tableau vide si aucun film
                - si l'argument n'est pas un entier, retourne 'la note doit être un nombre valide"
        """
        note_min = verif_var_int(note_min)
        note_max = verif_var_int(note_max)
        note_min, note_max = verif_order_int(note_min, note_max)
        films = self.get_movie_range("note_sur_10", note_min, note_max)

        return films


if __name__ == "__main__":
    loader = DataLoader()

    movie_year = loader.get_movie_by_years_range(2005, 200)
    print(f"{len(movie_year)}")
