import os
import sys
import csv
from pathlib import Path
from typing import List, Optional


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.settings import CSV_PATH, COLONNES
from logique.horror_movie import HorrorMovie


class DataLoader:
    def __init__(self):
        """Initialisation des variables necessaires pour la classe"""
        self.csv_path = CSV_PATH
        self.movies = []
        self.is_loaded = False

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

        if not Path(CSV_PATH).exists():
            raise FileNotFoundError(f"Le fichier CSV est introuvable : {CSV_PATH}")

        with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
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

    def get_movie(self, search_type, search):
        """
        Parcours la liste de movies pour trouver l'ensemble des films selon les paramètres demandé

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
                print(film.titre)
        return search_movies

    def get_movie_by_note(self, note):
        """
        Fonction qui permet de retourner l'ensembles des films ayant une note précise
        Fait appel à get_movie() pour obtenir les résultats

        Args:
            note (int or str) : Les films sont notés de 0 à 10

        Return:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note :
            - retourne un tableau vide si aucun film
            - si l'argument n'est pas un entier, retourne 'la note doit être un nombre valide"
        """
        try:
            notes = int(note)
        except (ValueError, TypeError):
            raise ValueError("La note doit être un nombre valide")
        return self.get_movie("note_sur_10", notes)

    def get_movie_by_realisateur(self, real):
        """
        Parcours l'ensemble des films chargé pour retourné ceux qui ont été réalisé par un réalisateur donné
        Fait appel à get_movie() pour obtenir les résultats

        Args:
            real(str) : Le nom du realisateur donné est modifié pour supprimer les espaces de début et fin

        Retur:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note : retourne un tableau vide si aucun film avec ce réalisateur
        """
        realisateurs = real.strip().lower()
        return self.get_movie("realisateur", realisateurs)

    def get_movie_by_sous_genre(self, sous_genre):
        """
        Parcours l'ensemble des films chargé pour retourné ceux qui ont un sous-genre donné
        Fait appel à get_movie() pour obtenir les résultats

        Args:
            sous_genre(str) : Le sous-genre est modifié pour supprimer les espaces de début et fin

        Retur:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note : retourne un tableau vide si aucun film trouvé
        """
        sousgenre = sous_genre.strip().lower()
        return self.get_movie("sous_genre", sousgenre)

    def get_movie_by_titre(self, titre):
        """
        Parcours l'ensemble des films chargé pour retourné ceux qui ont un titre donné
        Fait appel à get_movie() pour obtenir les résultats

        Args:
            titre(str) : Le sous-genre est modifié pour supprimer les espaces de début et fin

        Retur:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note :
            - retourne un tableau vide si aucun film trouvé
            - peut permettre de vérifier si doublons d'insertion
        """
        titres = titre.strip().lower()
        return self.get_movie("titre", titres)

    def get_movie_by_years(self, annee):
        """
        Parcours l'ensemble des films chargé pour retourné ceux qui sont sortie une année précise
        Fait appel à get_movie() pour obtenir les résultats

        Args:
            annee(str or int) : Une vérification de convertion en int est réalisé pour valider la donnée

        Retur:
            [obj, ... obj] -> tableau d'objet HorrorMovie

        Note : retourne un tableau vide si aucun film trouvé
        """
        try:
            annees = int(annee)
        except (ValueError, TypeError):
            raise ValueError("L'année doit être un nombre valide")
        return self.get_movie("annee", annees)


if __name__ == "__main__":
    loader = DataLoader()
    loader.load_movies()

    print(f"Chargé {len(loader.movies)} films")
    # loader.get_movie_by_note('7')
    # loader.get_movie_by_years(2018)
    loader.get_movie_by_titre("la main")
