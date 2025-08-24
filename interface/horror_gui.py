# horror_gui.py
import sys
import os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QGroupBox,
)
from PySide6.QtCore import Qt
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.recommender import HorrorRecommender
from config.dev_gui_settings import RECO_DATA_DEV, RECO_DATA_PROD


class HorrorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recommender = HorrorRecommender()
        self._reco_data_dev = RECO_DATA_DEV
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("🎬 Recommandation de film d'horreur")
        self.setGeometry(200, 200, 800, 600)

        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout(central_widget)

        profile_section = self.create_profile_section()
        layout.addWidget(profile_section)

        reco_section =self.create_recommendation_section()
        layout.addWidget(reco_section)

    # === Gestion de la section profil ======

    def create_profile_section(self):
        profile_data = self.get_profile_data()
        # QGroupBox = boîte avec titre et bordure
        profile_group = QGroupBox("📊 Ton Profil")

        # Layout pour organiser le contenu DANS le groupe
        profile_layout = QVBoxLayout(profile_group)

        # Ajouter les labels avec tes données
        genre_label = QLabel(f"🎭 Genre préféré: {profile_data['genre']}")
        periode_label = QLabel(f"📅 Période: {profile_data['periode']}")
        real_label = QLabel(f"🎬 Réalisateur favori: {profile_data['realisateur']}")

        # Ajouter au layout
        profile_layout.addWidget(genre_label)
        profile_layout.addWidget(periode_label) 
        profile_layout.addWidget(real_label)

        return profile_group

    def get_profile_data(self):
        # Utiliser ton recommender existant !

        profile = self.recommender.creat_user_profil()
        print(profile)

        genre_info = self.recommender.analyze_best_sous_genre()[0]
        periode_info = self.recommender.analyze_best_periode()[0] 
        real_info = self.recommender.analyze_best_realisateur()[0]

        return {
            "genre": f"{genre_info[0]} ({genre_info[1]:.1f}%)",
            "periode": f"{periode_info[0]} ({periode_info[1]:.1f}%)", 
            "realisateur": f"{real_info[0]} ({real_info[1]:.1f}%)"
        }

    def create_recommendation_section(self):

        reco_data = self.get_reco_data()

        reco_group= QGroupBox("🎞️ Tes recommendations")

        reco_layout= QVBoxLayout(reco_group)
        for film in reco_data[:5]:
            titre_label = QLabel(
                f"🎬 {film['title']} sorti en {film['release_date'][5:7]} - {film['release_date'][:4]}."
            )
            detail_label = QLabel(
                f"💯 Il a une note de {film["vote_average"]} pour  {film["vote_count"]} votants"
            )

            reco_layout.addWidget(titre_label)
            reco_layout.addWidget(detail_label)

        return reco_group

    def get_reco_data(self):
        if self._reco_data_dev is None:
            print("🌐 Appel API...")
            self._reco_data_dev = self.recommender.get_recommendations()
            
        else:
            print("💾 Utilisation cache...")    

        return self._reco_data_dev


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HorrorApp()
    window.show()
    app.exec()
