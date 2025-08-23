class HorrorMovie:
    def __init__(self, titre, annee, realisateur, sous_genre, note_sur_10):
        """
        Initialisation de la classe film avec vérification des champs

        Args:
            titre(str), realisateur(str), sous_genre(str):
                Si 1 de ces champs est vide ou remplis uniquement avec des espaces renvoie None
                sinon renvoie la donnée
            annee(int), note_sur_10(int) :
                si il ne peut être converti en int renvoie None
                Testé avec try/except
        """
        self.titre = titre.strip().lower() if titre and titre.strip().lower() else None

        try:
            self.annee = int(annee)
        except (ValueError, TypeError):
            self.annee = None

        self.realisateur = (
            realisateur.strip().lower() if realisateur and realisateur.strip().lower() else None
        )

        self.sous_genre = (
            sous_genre.strip().lower() if sous_genre and sous_genre.strip().lower() else None
        )

        try:
            self.note_sur_10 = int(note_sur_10)
        except (ValueError, TypeError):
            self.note_sur_10 = None
