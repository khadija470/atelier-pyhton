import csv


def sauvegarder_csv(datasets):
    with open("data/datasets.csv", "w", newline="", encoding="utf-8") as fichier:
        colonnes_csv = ["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"]
        writer = csv.DictWriter(fichier, fieldnames=colonnes_csv)
        writer.writeheader()
        for d in datasets:
            writer.writerow(d)
    print(f"{len(datasets)} dataset(s) sauvegardé(s) dans data/datasets.csv")


def recharger_csv(datasets):
    try:
        with open("data/datasets.csv", "r", newline="", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier)
            datasets.clear()
            for ligne in reader:
                ligne["lignes"] = int(ligne["lignes"])
                ligne["colonnes"] = int(ligne["colonnes"])
                ligne["taille"] = float(ligne["taille"])
                ligne["public"] = ligne["public"] == "True"
                datasets.append(ligne)
        if len(datasets) == 0:
            print("Le fichier data/datasets.csv est vide.")
        else:
            print(f"{len(datasets)} dataset(s) rechargé(s) depuis data/datasets.csv")
    except FileNotFoundError:
        print("Le fichier data/datasets.csv n'existe pas encore. Faites d'abord une sauvegarde.")