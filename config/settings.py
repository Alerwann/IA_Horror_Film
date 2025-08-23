# === CHEMIN DES FICHIERS ET DOSSIERS ===
CSV_PATH = "data/My_horror_film.csv"

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

# === COLONNES ATTENDUES ===

COLONNES = {"Titre", "Année", "Réalisateur", "Sous_genre", "Note sur 10"}

# === POIDS D'IMPORTANCE ===

TRES_IMPORTANT = 4
IMPORTANT = 3
PAS_IMPORTANT = 2
NEGLIGEABLE = 0

POIDS_SOUS_GENRE = IMPORTANT
POIDS_NOTE = TRES_IMPORTANT
POIDS_DATE = NEGLIGEABLE
POIDS_REALISATEUR = PAS_IMPORTANT
