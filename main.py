from interface.menu import afficher_menu
from interface.affichage import afficher_datasets
from datasets.gestion import (
    ajouter_dataset,
    rechercher_dataset,
    trier_dataset,
    modifier_dataset,
    supprimer_dataset,
)
from datasets.statistiques import statistiques
from stockage.csv_manager import sauvegarder_csv, recharger_csv
from stockage.json_manager import sauvegarder_json, recharger_json

domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")
datasets = []

while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_dataset(datasets, domaines_autorises)
    elif choix == "2":
        afficher_datasets(datasets)
    elif choix == "3":
        rechercher_dataset(datasets)
    elif choix == "4":
        trier_dataset(datasets)
    elif choix == "5":
        modifier_dataset(datasets)
    elif choix == "6":
        supprimer_dataset(datasets)
    elif choix == "7":
        statistiques(datasets, domaines_autorises)
    elif choix == "8":
        sauvegarder_csv(datasets)
    elif choix == "9":
        recharger_csv(datasets)
    elif choix == "10":
        sauvegarder_json(datasets)
    elif choix == "11":
        recharger_json(datasets)
    elif choix == "12":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, réessayez.")

    input("\nAppuyez sur Entrée pour continuer...")