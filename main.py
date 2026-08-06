from menu import afficher_menu
from gestion import (
    ajouter_dataset,
    afficher_datasets,
    rechercher_dataset,
    trier_dataset,
    modifier_dataset,
    supprimer_dataset,
    sauvegarder,
    recharger,
)
from statistiques import statistiques

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
        sauvegarder(datasets)
    elif choix == "9":
        recharger(datasets)
    elif choix == "10":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, réessayez.")

    input("\nAppuyez sur Entrée pour continuer...")