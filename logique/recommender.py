import sys
import os
from .data_loader import DataLoader
from .analyzer import HorrorAnalyser

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class HorrorRecommender:
    def __init__(self):
        """Initialisation des données"""
        self.analyzer = HorrorAnalyser
        self._best_realisateur = None
        self._best_sous_genre = None
        self._best_periode = None
        self._best_note = None
