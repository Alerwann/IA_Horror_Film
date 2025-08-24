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
        best_sous_genre= []
        if self._best_sous_genre == []:
            for sous_genre in self.analyzer.data_loader.get_all_sous_genre():
                proportion = self.analyzer.proportion_one_sous_genre(sous_genre)
                
                if proportion > best_stat:
                    best_sous_genre=[(sous_genre,proportion)]
                    best_stat = proportion
                elif proportion == best_stat:
                    best_sous_genre.append((sous_genre, proportion))
                
        self._best_sous_genre = self.get_the_best_sous_genre(best_sous_genre)
        return self._best_sous_genre

    def analyze_best_realisateur(self):
        """retourne liste des meilleur realisateur"""
        best_stat = 0
        best_realisateur=[]
        if self._best_realisateur == []:

            for realisateur in self.analyzer.data_loader.get_all_realisateurs():
                proportion = self.analyzer.proportion_one_real(realisateur)
                if proportion > best_stat:
                    best_realisateur = [(realisateur, proportion)]
                    best_stat = proportion
                elif proportion == best_stat:
                    best_realisateur.append((realisateur, proportion))
            self._best_realisateur = self.get_the_best_realisateur(best_realisateur)
        return self._best_realisateur

    def analyze_best_periode(self):
        """Retourne la liste des meilleur périodes"""
        best_stat=0
        best_periode= []
        if self._best_periode == []:
            for era_name,(start,end)in HORROR_ERAS.items():
                proportion = self.analyzer.proportion_annee_range(start,end)

                if proportion > best_stat:
                    best_periode=[(era_name,proportion)]
                    best_stat = proportion

                elif proportion == best_stat:
                    best_periode.append((era_name,proportion))

        self._best_periode = self.get_the_best_periode(best_periode)

        return self._best_periode

    # === FUNCTION GET THE BEST ===
    # ces fonctions choisissent si il y une égaliter lequel prendre en fonction des moyennes des notes
    def get_the_best_periode(self,best_periode):   

        if len(best_periode) == 1:

            self._best_periode=best_periode
        if len(best_periode)>0:

            for i in range(len(best_periode)):
                best_moyenne_rating =0
                start, end = HORROR_ERAS[best_periode[i][0]]
                sum_rating = 0

                for film in self.analyzer.data_loader.get_movie_by_years_range(start,end):
                    sum_rating += film.note_sur_10
                moyen_rating=round(sum_rating/len(self.analyzer.data_loader.get_movie_by_years_range(start,end)),4)

                if moyen_rating >= best_moyenne_rating:
                    self._best_periode = best_periode

        return self._best_periode

    def get_the_best_realisateur(self, best_real):
        length_tab = len(best_real) 

        if length_tab==1:
            self._best_realisateur = best_real
        elif length_tab>1:
            best_moyenne_rating =0     
            for i in range(length_tab):
                sum_rating = 0

                for film in self.analyzer.data_loader.get_movie_by_realisateur(best_real[i][0]):
                    sum_rating+= film.note_sur_10

                moyenne_rating = round(sum_rating / len(self.analyzer.data_loader.get_movie_by_realisateur(best_real[i][0] )), 4)

                if moyenne_rating >= best_moyenne_rating:
                    self._best_realisateur .append(best_real[i])
                    best_moyenne_rating=moyenne_rating

        return self._best_realisateur

    def get_the_best_sous_genre(self, best_sousgenre):
        """"""
        length_list = len(best_sousgenre)
        if length_list == 1:
            self._best_sous_genre = best_sousgenre
        if length_list>1:
            best_moyenne_rating = 0
            for i in range(len(best_sousgenre)):
                sum_rating=0
                collection_film = self.analyzer.data_loader.get_movie_by_sous_genre(best_sousgenre[i][0])

                for film in collection_film:
                    sum_rating+=film.note_sur_10

                moyenne_rating = round(sum_rating/ len(collection_film),4)
                
                if moyenne_rating >= best_moyenne_rating:
                    self._best_sous_genre .append(best_sousgenre[i])
                    best_moyenne_rating = moyenne_rating
        return self._best_sous_genre

    # ==== CREATION DU PROFIL ===

    def creat_user_profil(self):
        """"""
        periode= self.analyze_best_periode()
        start,end = HORROR_ERAS[periode[0][0]]
        realisateur = self.analyze_best_realisateur()
        
        




    
if __name__ == "__main__":
    recommender = HorrorRecommender()
    print(recommender.analyze_best_sous_genre(), 'sous-genre')
    print(recommender.analyze_best_realisateur(),'realisateur')
    print (recommender.analyze_best_periode(),'periode')
