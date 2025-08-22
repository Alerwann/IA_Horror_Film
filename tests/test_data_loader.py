import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.horror_movie import HorrorMovie
from logique.data_loader import DataLoader

# ==== Tests de chargement du fichier ====
def test_load_movies_success():
    loader = DataLoader()
    films = loader.load_movies()

    assert len(films) > 0 
    assert loader.is_loaded == True
    assert all(isinstance(film, HorrorMovie) for film in films)
    


def test_load_specific_movie():
    loader = DataLoader()
    
    films = loader.load_movies()
  

    misery = next((f for f in films if f.titre == 'misery'), None)
    assert misery is not None
    assert misery.annee == 1990
    assert misery.note_sur_10 == 10


def test_reload_movies():
    loader = DataLoader()
    films1 = loader.load_movies()
    films2 = loader.load_movies()  # Recharger

    assert len(films1) == len(films2)


## === Des fonctions get pour valeur particulières ===


def test_get_by_titre():
    """ Test de recherche par le titre """
    loader = DataLoader()
    
    titre_film = loader.get_movie_by_titre( "Misery")  
    titre_false_film = loader.get_movie_by_titre('Erreur')

    assert len(titre_film) > 0  
    assert titre_film[0].titre == "misery" 
    assert len(titre_false_film) == 0


def test_get_by_real():
    """ Test de recherche par le nom du realisateur """
    loader = DataLoader()

    real_film = loader.get_movie_by_realisateur('rob reiner')
    false_real_film = loader.get_movie_by_realisateur('Erreur')

    assert len(real_film)>0
    assert len(false_real_film) ==0
    assert real_film[0].titre == 'misery'

def test_get_by_sous_genre():
    """ Test de recherche par le genre """
    loader = DataLoader()

    sousgenre_film = loader.get_movie_by_sous_genre('psychologique')

    assert len(sousgenre_film)>0
    assert sousgenre_film[1].titre == 'cassandra'


## === Test unitaires pour les recherches par interval ===

def test_by_note():
    "Test les recherches par intervalle de note"
    loader = DataLoader()
    for film in loader.get_movie_by_note_range(5, 10):
        assert 5 <= film.note_sur_10 <= 10
    assert loader.get_movie_by_note_range(7,10) == loader.get_movie_by_note_range(10,7)
    assert loader.get_movie_by_note_range('9',10)== loader.get_movie_by_note_range(9,10)
    assert loader.get_movie_by_note_range(9, 10) == loader.get_movie_by_note_range(9, '10')

    assert len(loader.get_movie_by_note_range(11,20)) == 0
    


### === Test de Get movie get_movie_range
# Get_movie et get_movies sont utilisées sous toutes ses formes dans chacune des fonctions testées
