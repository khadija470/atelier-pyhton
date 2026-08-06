# --- Domaines autorisés ---
domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")

# --- Liste des datasets ---
datasets = []

# --- Menu principal ---
while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Trier les datasets")
    print("5. Modifier un dataset")
    print("6. Supprimer un dataset")
    print("7. Statistiques")
    print("8. Quitter")
    print("========================")

    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom du dataset : ")
        domaine = input("Domaine : ")
        if domaine not in domaines_autorises:
            print(f"Attention : « {domaine} » n'est pas un domaine autorisé.")
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

    elif choix == "2":
        if len(datasets) == 0:
            print("Aucun dataset enregistré.")
        else:
            for d in datasets:
                print(f"- {d['nom']} ({d['domaine']}, {d['lignes']} lignes, format {d['format']})")

    elif choix == "3":
        recherche = input("Nom du dataset à rechercher : ")
        trouve = False
        for d in datasets:
            if d["nom"] == recherche:
                print(f"Trouvé : {d['nom']} ({d['domaine']}, {d['lignes']} lignes)")
                trouve = True
        if not trouve:
            print("Aucun dataset ne porte ce nom.")

    elif choix == "4":
        datasets.sort(key=lambda d: d["nom"])
        print("Datasets triés par nom.")
        for d in datasets:
            print(f"- {d['nom']}")

    elif choix == "5":
        recherche = input("Nom du dataset à modifier : ")
        trouve = False
        for d in datasets:
            if d["nom"] == recherche:
                d["domaine"] = input("Nouveau domaine : ")
                d["lignes"] = int(input("Nouveau nombre de lignes : "))
                print(f"Dataset « {recherche} » modifié.")
                trouve = True
        if not trouve:
            print("Aucun dataset ne porte ce nom.")

    elif choix == "6":
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
    elif choix == "7":
        if len(datasets) == 0:
            print("Aucun dataset enregistré.")
        else:
            total = len(datasets)
            total_lignes = sum(d["lignes"] for d in datasets)
            moyenne_colonnes = sum(d["colonnes"] for d in datasets) / total
            publics = len([d for d in datasets if d["public"]])
            prives = total - publics
            nb_csv = len([d for d in datasets if d["format"] == "csv"])
            nb_json = len([d for d in datasets if d["format"] == "json"])

            print(f"Nombre de datasets : {total}")
            print(f"Nombre total de lignes : {total_lignes}")
            print(f"Nombre moyen de colonnes : {moyenne_colonnes:.1f}")
            print(f"Datasets publics : {publics}")
            print(f"Datasets privés : {prives}")
            print(f"Datasets CSV : {nb_csv}")
            print(f"Datasets JSON : {nb_json}")

            repartition = {dom: len([d for d in datasets if d["domaine"] == dom])
                           for dom in domaines_autorises}
            print("Répartition par domaine :")
            for dom, nb in repartition.items():
                print(f"  {dom} : {nb}")
    elif choix == "8":
        print("Au revoir !")
        break

    else:
        print("Choix invalide, réessayez.")

    input("\nAppuyez sur Entrée pour continuer...")