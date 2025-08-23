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
        if self._best_sous_genre == []:
            for sous_genre in self.analyzer.data_loader.get_all_sous_genre():
                proportion = self.analyzer.proportion_one_sous_genre(sous_genre)
                if proportion > best_stat:
                    self._best_sous_genre=[(sous_genre,proportion)]
                    best_stat = proportion

                if proportion == best_stat:
                    self._best_sous_genre.append((sous_genre, proportion))
        return self._best_sous_genre

    def analyze_best_realisateur(self):
        """retourne liste des meilleur realisateur"""
        best_stat = 0
        if self._best_realisateur == []:

            for realisateur in self.analyzer.data_loader.get_all_realisateurs():
                proportion = self.analyzer.proportion_one_real(realisateur)
                if proportion > best_stat:
                    self._best_realisateur = [(realisateur, proportion)]
                    best_stat = proportion

                if proportion == best_stat:
                    self._best_realisateur.append((realisateur, proportion))
        return set(self._best_realisateur)

    def analyze_best_periode(self):
        """Retourne la liste des meilleur périodes"""
        best_stat=0
        best_periode= []
        if self._best_periode == []:
            for era_name,(start,end)in HORROR_ERAS.items():
                proportion = self.analyzer.proportion_annee_range(start,end)
                if proportion > best_stat:
                    best_periode=[(era_name,proportion)]
                    print( best_periode)

                if proportion == best_stat:
                    best_periode.append((era_name,proportion))
        self._best_periode = self.get_the_best_periode(best_periode)
        print(self._best_periode, "dans l'annalyse")
           

        return self._best_periode

    def get_the_best_periode(self,best_periode):   
        print(best_periode)             
        if len(best_periode) == 0:
            self._best_periode = best_periode
        if len(best_periode)>0:
            best_rating = 0
            length_films=0
            self._best_periode = best_periode[0]
            # for i in [0,len(best_periode)-1]:

            #     start, end = HORROR_ERAS[best_periode[i][0]]

            #     films = self.analyzer.data_loader.get_movie_by_note_range(start,end)
            #     length_films= len(films)
            #     rating_= self.calculate_rating(films, length_films)
            #     if rating_ >= best_rating:
            #         best_rating=rating_
            #         self._best_periode = best_periode[i]
            # return length_films
        return self._best_periode
    
    def calculate_rating(self,films= None, length_films=1):
        if films == None:
            return 0
        total = sum(film.note_sur_10 for film in films if film.note_sur_10)
        return total / length_films


if __name__ == "__main__":
    recommender = HorrorRecommender()
    print(recommender.analyze_best_sous_genre(), 'sous-genre')
    print(recommender.analyze_best_realisateur(),'realisateur')
    print (recommender.analyze_best_periode(),'periode')
