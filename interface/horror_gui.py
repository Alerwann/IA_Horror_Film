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
    QComboBox,
)
from PySide6.QtCore import Qt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.recommender import HorrorRecommender
from config.dev_gui_settings import RECO_DATA_DEV, RECO_DATA_PROD
from config.settings import  HORROR_ERAS, GENRE_MAPPING


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

        reco_section = self.create_recommendation_section()
        layout.addWidget(reco_section)

        choice_section = self.create_choice_section()
        layout.addWidget(choice_section)

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

        profile = self.recommender.creat_user_profil_default()
        print(profile)

        genre_info = self.recommender.analyze_best_sous_genre()[0]
        periode_info = self.recommender.analyze_best_periode()[0]
        real_info = self.recommender.analyze_best_realisateur()[0]

        return {
            "genre": f"{genre_info[0]} ({genre_info[1]:.1f}%)",
            "periode": f"{periode_info[0]} ({periode_info[1]:.1f}%)",
            "realisateur": f"{real_info[0]} ({real_info[1]:.1f}%)",
        }

    def create_recommendation_section(self):

        reco_data = self.get_reco_data()

        reco_group = QGroupBox("🎞️ Tes recommendations")

        reco_layout = QVBoxLayout(reco_group)
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

    def create_choice_section(self):
        choice_group = QGroupBox("Tu veux d'autres choix?")

        # period_label =  QLabel("Periode :")
        self.period_deroulant_box = QComboBox()
        self.note_deroulant_box= QComboBox()
        self.genre_deroulant_box = QComboBox()

        self.period_deroulant_box.addItems(
            [
                "Période",
                "classique",
                "golden age (1980-1999)",
                "moderne (2000 - 2015)",
                "contemporain (depuis 2016)",
            ]
        )

        self.note_deroulant_box.addItem('Note')
        for note in range(11):
            self.note_deroulant_box.addItem(f'{note}')

        self.genre_deroulant_box.addItem("Genre de film")
        for genre in GENRE_MAPPING:
            self.genre_deroulant_box.addItem(f"{genre}")

        search_button = QPushButton("🔍 Rechercher avec mes critères")
        search_button.clicked.connect(self.on_search_clicked)
        
        choice_layout = QVBoxLayout(choice_group)
       
        choice_layout.addWidget(self.note_deroulant_box)
        choice_layout.addWidget(self.period_deroulant_box)
        choice_layout.addWidget(self.genre_deroulant_box)
        choice_layout.addWidget(search_button)

        return choice_group



    def on_search_clicked(self):

        select_note= self.note_deroulant_box.currentText()
        select_period = self.period_deroulant_box.currentText()
        select_genre = self.genre_deroulant_box.currentText()

        sortie = self.recommender.get_recommendations("particulier",select_note,select_period,select_genre)
        print(sortie[:2])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HorrorApp()
    window.show()
    app.exec()
