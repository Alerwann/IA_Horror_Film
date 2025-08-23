import os
import sys
import pytest


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.horror_movie import HorrorMovie
from logique.data_loader import DataLoader
from logique.analyzer import HorrorAnalyser


def test_proportion_one_real():
    analyzer = HorrorAnalyser()

    # Réalisateur connu
    prop = analyzer.proportion_one_real("rob reiner")
    assert 0 <= prop <= 100
    assert prop > 0  # On sait qu'il a au moins 1 film

    # Réalisateur inexistant
    prop_zero = analyzer.proportion_one_real("inexistant")
    assert prop_zero == 0

def test_proportion_note_range():
    analyzer = HorrorAnalyser()
    
    # Toutes les notes (devrait faire 100%)
    prop_all = analyzer.proportion_annee_range(1890,2100)
    assert prop_all == 100
    
    # Plage vide
    prop_empty = analyzer.proportion_annee_range(0, 100)
    assert prop_empty == 0
