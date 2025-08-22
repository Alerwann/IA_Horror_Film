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

    misery = next((f for f in films if f.titre == "misery"), None)
    assert misery is not None
    assert misery.annee == 1990
    assert misery.note_sur_10 == 10


def test_reload_movies():
    loader = DataLoader()
    films1 = loader.load_movies()
    films2 = loader.load_movies()  # Recharger

    assert len(films1) == len(films2)


## === Des fonctions get particulières ===


def test_get_by_titre():

    loader = DataLoader()
    
    titre_film = loader.get_movie_by_titre( "misery")  
    titre_false_film = loader.get_movie_by_titre('Erreur')

    assert len(titre_film) > 0  
    assert titre_film[0].titre == "misery" 
    assert len(titre_false_film) == 0


def test_get_by_annee():
    loader = DataLoader()

    str_year_film = loader.get_movie_by_years( "1990")
    int_year_film = loader.get_movie_by_years( 1990)
    

    assert len(str_year_film) >0
    assert len(str_year_film) == len (int_year_film)
    assert str_year_film[0].titre == "misery"
    


def test_get_by_real():
    loader = DataLoader()

    real_film = loader.get_movie_by_realisateur('rob reiner')
    false_real_film = loader.get_movie_by_realisateur('Erreur')

    assert len(real_film)>0
    assert len(false_real_film) ==0
    assert real_film[0].titre == 'misery'

def test_get_by_sous_genre():
    loader = DataLoader()

    sousgenre_film = loader.get_movie_by_sous_genre('psychologique')

    assert len(sousgenre_film)>0
    assert sousgenre_film[1].titre == 'cassandra'

def test_by_not():
    loader = DataLoader()

    note_film = loader.get_movie_by_note(7)
    

    assert len(note_film) >0
    assert note_film[0].titre == 'annabelle'
   
### === Test de Get movie
# Get movie est utilisé sous toutes ses formes dans chacune des fonctions testées
