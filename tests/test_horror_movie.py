import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.horror_movie import HorrorMovie

def test_creation_film_normal():

    titre = 'Misery'
    annee = 1990
    realisateur = "Rob Reiner"
    sous_genre = "Psychologique"
    note = 10

    film = HorrorMovie (titre, annee, realisateur, sous_genre, note)

    assert film.titre == "misery"
    assert film.annee == 1990
    assert film.realisateur == "rob reiner"
    assert film.sous_genre == "psychologique"
    assert film.note_sur_10 == 10

def test_creation_film_data_empty():
    film= HorrorMovie("","","","","")

    assert film.titre is None      
    assert film.annee is None       
    assert film.realisateur is None 
    assert film.sous_genre is None  
    assert film.note_sur_10 is None 

def test_creation_film_data_str_to_int():
    film = HorrorMovie('Misery','1990', 'Rob Reiner', 'Psychologique', '10')

    assert film.titre == "misery"
    assert film.annee == 1990
    assert film.realisateur == "rob reiner"
    assert film.sous_genre == "psychologique"
    assert film.note_sur_10 ==10

def test_creation_film_data_not_int():
    film = HorrorMovie("Misery", "fgds", "Rob Reiner", "Psychologique", "fvds")

    assert film.titre == "misery"
    assert film.annee is None
    assert film.realisateur == "rob reiner"
    assert film.sous_genre == "psychologique"
    assert film.note_sur_10 is None


def test_creation_film_espaces():
    
    film = HorrorMovie("  shining  ", "1980", "  stanley kubrick  ", "  psychologique  ", "10")

    
    assert film.titre == "shining"  # Espaces supprimés
    assert film.realisateur == "stanley kubrick"  # Espaces supprimés
    assert film.sous_genre == "psychologique"  # Espaces supprimés
