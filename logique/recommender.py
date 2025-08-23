import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.analyzer import HorrorAnalyser
from config.settings import NOTE_ERAS, HORROR_ERAS


class HorrorRecommender:
    def __init__(self):
        """Initialisation des données"""
        self.analyzer = HorrorAnalyser()

        self._best_realisateur = []
        self._best_sous_genre = []
        self._best_periode = []
        self._best_note = []

    def analyze_best_sous_genre(self):
        """retourne une liste des sous genre preféré"""
        best_stat =0
        for sous_genre in self.analyzer.data_loader.get_all_sous_genre():
            proportion = self.analyzer.proportion_one_sous_genre(sous_genre)
            if proportion > best_stat:
                self._best_sous_genre=[{sous_genre,proportion}]

            if proportion == best_stat:
                self._best_sous_genre.append({sous_genre, proportion})
        return self._best_sous_genre

    def analyze_best_realisateur(self):
        """retourne liste des meilleur realisateur"""
        best_stat = 0

        for realisateur in self.analyzer.data_loader.get_all_realisateurs():
            proportion = self.analyzer.proportion_one_real(realisateur)
            if proportion > best_stat:
                self._best_realisateur=[{realisateur,proportion}]

            if proportion == best_stat:
                self._best_realisateur.append({realisateur, proportion})
        return self._best_realisateur

    def analyze_best_periode(self):
        """Retourne la liste des meilleur périodes"""
        best_stat=0

        for era_name,(start,end)in HORROR_ERAS.items():
            proportion = self.analyzer.proportion_annee_range(start,end)
            if proportion >best_stat:
                self._best_periode=[{era_name,proportion}]

            if proportion == best_stat:
                self._best_periode.append({era_name,proportion})
        return self._best_periode

    def analyse_best_note(self):
        """Retourne la liste des meilleur périodes"""
        best_stat = 0

        for era_name,(start,end) in NOTE_ERAS.items():
            proportion  = self.analyzer.proportion_note_range(start,end)
            if proportion > best_stat:
                self._best_note=[era_name,proportion]

            if proportion == best_stat:
                self._best_note.append({era_name,proportion})
        return self._best_note


            
if __name__ == "__main__":
    recommender = HorrorRecommender()
    print(recommender.analyze_best_sous_genre(), 'sous-genre')
    print(recommender.analyze_best_realisateur(),'realisateur')
    print (recommender.analyze_best_periode(),'periode')
    print(recommender.analyse_best_note(),'note')
