import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.horror_movie import HorrorMovie
from logique.data_loader import DataLoader

# ==== TEST INITIALISATION====
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

## === TEST SEARCH METHODS - GLOBAL PARAMETER ===


def test_get_all_realisateurs():
    loader = DataLoader()
    realisateurs = loader.get_all_realisateurs()

    assert len(realisateurs) > 0
    assert len(realisateurs) == len(set(realisateurs))  
    assert "rob reiner" in realisateurs  
    assert None not in realisateurs  


@pytest.mark.parametrize(
    "search,expected_value",
    [
        ("realisateur", "rob reiner"),
        ("annee", 1990),
        ("sous_genre", "psychologique"),
        ("note_sur_10", 10),
    ],
)
def test_get_all_function(search,expected_value):
    loader = DataLoader()
    informations = loader.get_all_informations(search)
    assert len(informations) > 0
    assert len(informations) == len(set(informations))
    assert expected_value in informations
    assert None not in informations


## === TESTS SERCH METHODS - SINGLE PARAMETER ===


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


## === TEST SEARCH METHODS - MULTI PARAMETERS ===

def test_by_note():
    "Test les recherches par intervalle de note"
    loader = DataLoader()

    for film in loader.get_movie_by_note_range(5, 10):
        assert 5 <= film.note_sur_10 <= 10
        
    assert loader.get_movie_by_note_range(7,10) == loader.get_movie_by_note_range(10,7)
    assert loader.get_movie_by_note_range('9',10)== loader.get_movie_by_note_range(9,10)
    assert loader.get_movie_by_note_range(9, 10) == loader.get_movie_by_note_range(9, '10')

    assert len(loader.get_movie_by_note_range(11,20)) == 0
    assert len(loader.get_movie_by_note_range(-45,-2)) == 0

def test_by_annee():
    "test de recherche sur une période donnée"
    loader = DataLoader()

    for film in loader.get_movie_by_years_range(1998,2005):
        assert 1998 <= film.annee <= 2005

    assert loader.get_movie_by_years_range(2005, 2010) == loader.get_movie_by_years_range(2010,2005)
    assert loader.get_movie_by_years_range("2009", 2010) == loader.get_movie_by_years_range(2009, 2010)
    assert loader.get_movie_by_years_range(2009, 2010) == loader.get_movie_by_years_range(2009, "2010" )

    assert len(loader.get_movie_by_years_range(3000,3001)) == 0
    assert len(loader.get_movie_by_years_range(50, 100)) == 0


### === Test de Get movie get_movie_range
# Get_movie et get_movies sont utilisées sous toutes ses formes dans chacune des fonctions testées
