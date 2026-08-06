<div align="center">

# 📊 Application datasetManager

**Gestion d'un catalogue de jeux de données — application console en Python**

![Python](https://img.shields.io/badge/Python-3.14.7-3776AB?logo=python&logoColor=white)
![Statut](https://img.shields.io/badge/Statut-Terminé-brightgreen)
![Formation](https://img.shields.io/badge/TP-Formation%20IA-2C3E50)

</div>

---

## 📋 Description

Avant de traiter des données avec des outils comme **Pandas**, il est utile de disposer d'un catalogue des jeux de données (*datasets*) disponibles et de leurs caractéristiques.

**datasetManager** est une application console qui permet d'enregistrer, consulter, rechercher et analyser un ensemble de datasets, puis de sauvegarder ces informations sur le disque aux formats **CSV** et **JSON**.

---

## ✨ Fonctionnalités

- ➕ **Ajouter** un dataset (nom, domaine, lignes, colonnes, taille, format, public/privé)
- 📄 **Afficher** la liste des datasets enregistrés
- 🔍 **Rechercher** un dataset par son nom
- ↕️ **Trier** les datasets par nom
- ✏️ **Modifier** un dataset existant
- 🗑️ **Supprimer** un dataset
- 📈 **Statistiques** : totaux, moyennes, répartition par domaine et par format
- 💾 **Sauvegarder / recharger** au format **CSV** et **JSON**
- 🛡️ **Gestion des erreurs** : saisie invalide, fichier manquant ou vide

---

## 📁 Structure du projet

```
datasetManager/
├── main.py              # point d'entrée : menu principal
├── interface/           # affichage
│   ├── __init__.py
│   ├── menu.py          # affichage du menu
│   └── affichage.py     # affichage des datasets
├── datasets/            # logique métier
│   ├── __init__.py
│   ├── gestion.py       # ajout, recherche, tri, modification, suppression
│   └── statistiques.py  # calcul des statistiques
├── stockage/            # persistance des données
│   ├── __init__.py
│   ├── csv_manager.py   # sauvegarde / rechargement CSV
│   └── json_manager.py  # sauvegarde / rechargement JSON
└── data/                # fichiers de données
    ├── datasets.csv
    └── datasets.json
```

> Le projet est organisé en **packages** (chaque dossier contient un `__init__.py`), chacun avec une responsabilité claire : l'interface, la gestion des datasets et le stockage.

---

## ⚙️ Prérequis

- **Python 3** — [télécharger ici](https://www.python.org/downloads/)

Aucune bibliothèque externe : le programme n'utilise que les modules standards `csv` et `json`.

---

## 🚀 Lancement

Depuis le dossier racine `datasetManager` :

```bash
python main.py
```

> ⚠️ Le programme doit être lancé **depuis la racine**, pour que les chemins vers le dossier `data/` soient corrects.

---

## 🕹️ Utilisation

Au lancement, un menu interactif propose les actions suivantes :

| Choix | Action                | Choix | Action                 |
|:-----:|-----------------------|:-----:|------------------------|
| 1     | Ajouter un dataset    | 7     | Statistiques           |
| 2     | Afficher les datasets | 8     | Sauvegarder (CSV)      |
| 3     | Rechercher un dataset | 9     | Recharger (CSV)        |
| 4     | Trier les datasets    | 10    | Sauvegarder (JSON)     |
| 5     | Modifier un dataset   | 11    | Recharger (JSON)       |
| 6     | Supprimer un dataset  | 12    | Quitter                |

Le menu reste actif tant que l'utilisateur ne choisit pas **Quitter**.

---

## 💾 Formats de données

| Format | Fichier              | Particularité                                                        |
|--------|----------------------|---------------------------------------------------------------------|
| CSV    | `data/datasets.csv`  | Tabulaire, simple, ouvrable dans un tableur                          |
| JSON   | `data/datasets.json` | Structuré et lisible ; conserve les types (nombres, booléens)       |

---

## 👤 Auteur

**Khadija Ngom** — Formation Intelligence Artificielle
