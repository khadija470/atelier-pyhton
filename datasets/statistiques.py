def statistiques(datasets, domaines_autorises):
    if len(datasets) == 0:
        print("Aucun dataset enregistré.")
        return
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