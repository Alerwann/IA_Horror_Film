
from .data_loader import DataLoader
from .analyzer import HorrorAnalyser

class HorrorRecommender:
    def __init__(self):
        """Initialisation des données"""
        self.analyzer = HorrorAnalyser