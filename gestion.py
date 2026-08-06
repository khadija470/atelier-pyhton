import csv


def ajouter_dataset(datasets, domaines_autorises):
    nom = input("Nom du dataset : ")
    domaine = input("Domaine : ")
    if domaine not in domaines_autorises:
        print(f"Attention : « {domaine} » n'est pas un domaine autorisé.")
    try:
        lignes = int(input("Nombre de lignes : "))
        colonnes = int(input("Nombre de colonnes : "))
        taille = float(input("Taille en Mo : "))
        format_dataset = input("Format (csv ou json) : ")
        public = input("Public ? (true ou false) : ") == "true"
        dataset = {
            "nom": nom,
            "domaine": domaine,
            "lignes": lignes,
            "colonnes": colonnes,
            "taille": taille,
            "format": format_dataset,
            "public": public,
        }
        datasets.append(dataset)
        print(f"Dataset « {nom} » ajouté. Total : {len(datasets)}")
    except ValueError:
        print("Erreur : lignes, colonnes et taille doivent être des nombres. Dataset non ajouté.")


def afficher_datasets(datasets):
    if len(datasets) == 0:
        print("Aucun dataset enregistré.")
    else:
        for d in datasets:
            print(f"- {d['nom']} ({d['domaine']}, {d['lignes']} lignes, format {d['format']})")


def rechercher_dataset(datasets):
    recherche = input("Nom du dataset à rechercher : ")
    trouve = False
    for d in datasets:
        if d["nom"] == recherche:
            print(f"Trouvé : {d['nom']} ({d['domaine']}, {d['lignes']} lignes)")
            trouve = True
    if not trouve:
        print("Aucun dataset ne porte ce nom.")


def trier_dataset(datasets):
    datasets.sort(key=lambda d: d["nom"])
    print("Datasets triés par nom.")
    for d in datasets:
        print(f"- {d['nom']}")


def modifier_dataset(datasets):
    recherche = input("Nom du dataset à modifier : ")
    trouve = False
    for d in datasets:
        if d["nom"] == recherche:
            d["domaine"] = input("Nouveau domaine : ")
            try:
                d["lignes"] = int(input("Nouveau nombre de lignes : "))
                print(f"Dataset « {recherche} » modifié.")
            except ValueError:
                print("Erreur : le nombre de lignes doit être un nombre. Modification annulée.")
            trouve = True
    if not trouve:
        print("Aucun dataset ne porte ce nom.")


def supprimer_dataset(datasets):
    recherche = input("Nom du dataset à supprimer : ")
    trouve = False
    for d in datasets:
        if d["nom"] == recherche:
            datasets.remove(d)
            print(f"Dataset « {recherche} » supprimé.")
            trouve = True
            break
    if not trouve:
        print("Aucun dataset ne porte ce nom.")


def sauvegarder(datasets):
    with open("datasets.csv", "w", newline="", encoding="utf-8") as fichier:
        colonnes_csv = ["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"]
        writer = csv.DictWriter(fichier, fieldnames=colonnes_csv)
        writer.writeheader()
        for d in datasets:
            writer.writerow(d)
    print(f"{len(datasets)} dataset(s) sauvegardé(s) dans datasets.csv")


def recharger(datasets):
    try:
        with open("datasets.csv", "r", newline="", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier)
            datasets.clear()
            for ligne in reader:
                ligne["lignes"] = int(ligne["lignes"])
                ligne["colonnes"] = int(ligne["colonnes"])
                ligne["taille"] = float(ligne["taille"])
                ligne["public"] = ligne["public"] == "True"
                datasets.append(ligne)
        if len(datasets) == 0:
            print("Le fichier datasets.csv est vide.")
        else:
            print(f"{len(datasets)} dataset(s) rechargé(s) depuis datasets.csv")
    except FileNotFoundError:
        print("Le fichier datasets.csv n'existe pas encore. Faites d'abord une sauvegarde.")