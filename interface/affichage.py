def afficher_datasets(datasets):
    if len(datasets) == 0:
        print("Aucun dataset enregistré.")
    else:
        for d in datasets:
            print(f"- {d['nom']} ({d['domaine']}, {d['lignes']} lignes, format {d['format']})")