import sys
from pathlib import Path

# === CHEMIN DES FICHIERS ET DOSSIERS ===


# === SEUIL DES NOTES ===
NOTE_ERAS={
    "nul" :(0,2),
    "mauvais":(3,4),
    "moyen": (5,6),
    "bon" : (7,8),
    "excellent" : (9,10)
    }

# === PERIODE DU CINEMA ===
HORROR_ERAS = {
    "classique": (1960, 1979),
    "golden_age": (1980, 1999),
    "moderne": (2000, 2015),
    "contemporain": (2016, 2030),
}
# ===GENRE MAPPING===

GENRE_MAPPING = {
    "psychologique": '27, 9648,53',  # Horror + Thriller + Mystery
    "surnaturel": '27, 14',  # Horror + Fantasy
    "horror pur": '27',  # Pure Horror
    "fantaisie": '27, 53,878',  # Horror + Fantasy+ sciencefiction
}


# # === COLONNES ATTENDUES ===

COLONNES = {"Titre", "Année", "Réalisateur", "Sous_genre", "Note sur 10"}

