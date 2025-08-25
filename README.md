# ==== INFORMATIONS SUR LE PROJET ====

# Nom du projet

        IA horror film 

# Description

Application qui permet d'avoir une liste de 5 films d'horreur.
La liste est basée un fichier CSV des goût de l'utilisateur et peut être modifier par un choix de note, sous-genre, période


### Version

V1.0.0

# 4 Auteur

Alerwann

## ==== UTILISATION ====
### Prérequis

- Python 3.8 ou plus récent
- pip (gestionnaire de paquets Python)
- fichier CSV remplis (lien pour fichier pdf type pour le tableur)
- Clé API TMBD(gratuite)

### Configuration API
1. **Créer un compte TMDB :**
   - Aller sur [https://www.themoviedb.org/](https://www.themoviedb.org/)
   - Créer un compte gratuit
   - Aller dans Paramètres > API
   - Demander une clé API (approbation immédiate)

2. **Creation CSV :**
        Solution 1:
                - Importer le tableau My_filmr_Horror
                - Remplir avec les films que vous avez vu (plus vous aurez d'information differentes plus l'étude sera complète)
                - Exporter au fomat CSV en le nommant My_horror_film.csv
                - Remplacer le fichier existant dans le dossier data par le votre
        Solution 2:
                - Dans le fichier data/My_horror_film.csv effacer les films en conservant les titres de colonnes (1ère ligne)
                - Remplir les informations dans l'ordre des colonnes en séparant par ";" les colonnes et "entrer" les lignes


### Installation
```bash
git clone https://github.com/Alerwann/IA_Horror_Film.git
cp .env.example .en 
git checkout feature/horror_gui
pip install -r requirements.txt pyinstaller
cp .env.example .env  # ← IMPORTANT !

Pour tester: python -m interfaces.horror_gui
Pour installer : pyinstaller HorrorRecommendApp.spec

```
- A l'ouverture de l'application s'affiche:
        - Le profil de l'utilisateur
        - La liste de 5 recommendations
        - L'espace de choix pour modifier la demande

- A la validation de la modification, la partie recommendation uniquement se met à jour

## 🐛 Dépannage

### Problèmes courants

#### "Aucune recommandation ne s'affiche"
- ✅ Vérifier que le fichier `.env` existe
- ✅ Vérifier que votre clé API est correcte  
- ✅ Tester votre clé sur [TMDB API](https://developers.themoviedb.org/3)

#### "Erreur 401 Unauthorized"
- ❌ Clé API invalide ou expirée
- 🔄 Régénérer une nouvelle clé sur votre compte TMDB

#### "L'interface se lance mais reste vide"
- ⚠️ Problème de connexion réseau
- 🌐 Vérifier votre connexion internet

# 4 ==== CONTRIBUTIONS ET LICENCES ====

# Contribution

Pas de contribution possibles

## Licences
MIT License - voir [LICENSE](LICENSE) pour les détails.


