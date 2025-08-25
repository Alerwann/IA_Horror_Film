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
    QGroupBox,
    QComboBox,
    
)
from PySide6.QtCore import Qt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.recommender import HorrorRecommender
from config.gui_settings import  RECO_DATA_PROD, HORROR_APP_STYLES
from config.settings import   GENRE_MAPPING


class HorrorApp(QMainWindow):
    def __init__(self):
        """ Initialisation des données"""
        super().__init__()
        self.recommender = HorrorRecommender()
        self._reco_data_dev = RECO_DATA_PROD
        self.setup_ui()

    def setup_ui(self):
        """ Création de la fenetre principal et ajout des widgets"""
        self.setWindowTitle("🎬 Recommandation de film d'horreur")
        self.setGeometry(200, 200, 900, 800)

        # Styles pour l'application
        self. setStyleSheet(HORROR_APP_STYLES)

        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout(central_widget)

        profile_section = self.create_profile_section()
        layout.addWidget(profile_section)
        profile_section.setFixedHeight(160)

        self.reco_section = self.create_recommendation_section()
        layout.addWidget(self.reco_section)

        choice_section = self.create_choice_section()
        layout.addWidget(choice_section)
        choice_section.setFixedHeight(200)
    # === Gestion de la section profil ======

    def create_profile_section(self ):
        """ A l'aide des donnéee du profil affiche le sous-genre et la période préférée"""
        profile_data = self.get_profile_data()
        # QGroupBox = boîte avec titre et bordure
        profile_group = QGroupBox("👨‍💻 Ton Profil 👩‍💻")

        # Layout pour organiser le contenu DANS le groupe
        profile_layout = QVBoxLayout(profile_group)

        # Ajouter les labels avec tes données
        genre_label = QLabel(
            f"🎭 Genre préféré: {profile_data['genre']} " )
        periode_label = QLabel(f"📅 Période: {profile_data['periode']}")

        # Ajouter au layout
        profile_layout.addWidget(genre_label)
        profile_layout.addWidget(periode_label)

        return profile_group

    def get_profile_data(self):
        """ Récupeère le profil de l'utilisateur retourne le genre et la période préférée"""

        profile = self.recommender.creat_user_profil_(
            rating_wish=None, periode_wish=None, sous_genre_wish=None
        )
        print(profile)

        genre_info = self.recommender.analyze_best_sous_genre()[0]
        periode_info = self.recommender.analyze_best_periode()[0]

        return {
            "genre": f"{genre_info[0]} ({genre_info[1]:.1f}%)",
            "periode": f"{periode_info[0]} ({periode_info[1]:.1f}%)"
            
        }

    def create_recommendation_section(
        self, rating_wish=None, periode_wish=None, sous_genre_wish=None
    ):
        """ Affiche les 5 meilleurs recommandations selon le profil choisi"""

        reco_data = self.get_reco_data(rating_wish=None, periode_wish=None, sous_genre_wish=None)

        reco_group = QGroupBox("🍿 Tes 5 recommendations 🍿")

        reco_layout = QVBoxLayout(reco_group)
        for film in reco_data[:5]:
            titre_label = QLabel(
                f"🎬 {film['title']} sorti en {film['release_date'][5:7]} - {film['release_date'][:4]}.💯 Il a une note de {film["vote_average"]} pour  {film["vote_count"]} votants"
            )

            reco_layout.addWidget(titre_label)

        return reco_group

    def get_reco_data(self, rating_wish=None, periode_wish=None, sous_genre_wish=None):
        """
        Récupère les recommandations de films selon les critères spécifiés.

        Args:
            rating_wish (float, optional): Note minimum souhaitée
            periode_wish (str, optional): Période historique souhaitée
            sous_genre_wish (str, optional): Sous-genre souhaité

        Returns:
            list: Liste des films recommandés
        """

        self._reco_data_dev = self.recommender.get_recommendations(rating_wish,periode_wish,sous_genre_wish)

        return self._reco_data_dev

    def create_choice_section(self):
        """
        Affichiche 3 menu déroulant (notes possibles, genre, période) et un bouton de validation
        Une fois validé un nouveau profil est créé.
        """
        choice_group = QGroupBox("🧐 Tu veux d'autres choix? 🧐")
        choice_layout = QVBoxLayout(choice_group, )
        combo_layout = QHBoxLayout()

        self.period_deroulant_box = QComboBox()
        QComboBox.setFixedSize(self.period_deroulant_box, 200,60)
        self.period_deroulant_box.addItems(
            [
                "Période",
                "classique",
                "golden_age",
                "moderne",
                "contemporain",
            ]
        )

        self.note_deroulant_box= QComboBox()
        QComboBox.setFixedSize(self.note_deroulant_box, 200, 60)
        self.note_deroulant_box.addItem('Note')
        for note in range(11):
            self.note_deroulant_box.addItem(f'{note}')

        self.genre_deroulant_box = QComboBox()
        QComboBox.setFixedSize(self.genre_deroulant_box, 200, 60)

        self.genre_deroulant_box.addItem("Genre de film")
        for genre in GENRE_MAPPING:
            self.genre_deroulant_box.addItem(f"{genre}")

        combo_layout.addWidget(self.note_deroulant_box)
        combo_layout.addWidget(self.period_deroulant_box)
        combo_layout.addWidget(self.genre_deroulant_box)

        choice_layout.addLayout(combo_layout)
        search_button = QPushButton("🔍 Rechercher avec mes critères")
        search_button.clicked.connect(self.on_search_clicked)
        search_button.setFixedSize(250,70)

        choice_layout.addWidget(search_button)
        choice_layout.setAlignment(search_button, Qt.AlignmentFlag.AlignHCenter)

        return choice_group

    def on_search_clicked(self):
        """
        Crée le profil en fonction des choix des menu déroulant
        Note: si le menu est sur la valeur par défaut renvoie None
        """
        select_note= self.note_deroulant_box.currentText()
        select_period = self.period_deroulant_box.currentText()
        select_genre = self.genre_deroulant_box.currentText()

        if select_note == "Note":
            select_note = None
        if select_genre == "Genre de film":
            select_genre = None
        if select_period == 'Période':
            select_period = None
        self.update_recommendation_section( select_note, select_period, select_genre  )

    def update_recommendation_section( self, rating_wish=None, periode_wish=None, sous_genre_wish=None ):
        """Met à jour SEULEMENT la section recommendations"""

        # Supprimer tous les widgets enfants de la section
        layout = self.reco_section.layout()
        if layout is not None:                
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            # Récupérer nouvelles données avec critères personnalisés
            new_reco_data = self.get_reco_data(rating_wish, periode_wish, sous_genre_wish)

            # Recréer le contenu
            for film in new_reco_data[:5]:
                titre_label = QLabel(
                        f"🎬 {film['title']} sorti en {film['release_date'][5:7]} - {film['release_date'][:4]}."
                    )
                detail_label = QLabel(
                        f"💯 Il a une note de {film['vote_average']} pour {film['vote_count']} votants"
                    )

                layout.addWidget(titre_label)
                layout.addWidget(detail_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HorrorApp()
    window.show()
    app.exec()
