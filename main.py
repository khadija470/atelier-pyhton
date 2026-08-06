# --- Domaines autorisés (tuple) ---
domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")

# --- Saisie des métadonnées du dataset ---
nom = input("Nom du dataset : ")
domaine = input("Domaine : ")

if domaine in domaines_autorises:
    print(f"Domaine « {domaine} » valide.")
else:
    print(f"Attention : « {domaine} » n'est pas dans la liste des domaines autorisés.")

lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))
taille = float(input("Taille en Mo : "))
format_dataset = input("Format (csv ou json) : ")
public = input("Public ? (true ou false) : ") == "true"

# --- Dictionnaire du dataset ---
dataset = {
    "nom": nom,
    "domaine": domaine,
    "lignes": lignes,
    "colonnes": colonnes,
    "taille": taille,
    "format": format_dataset,
    "public": public,
}

# --- Affichage du résumé ---
print("\n===== Résumé du dataset =====")
print(f"Nom      : {dataset['nom']}")
print(f"Domaine  : {dataset['domaine']}")
print(f"Lignes   : {dataset['lignes']}")
print(f"Colonnes : {dataset['colonnes']}")
print(f"Taille   : {dataset['taille']} Mo")
print(f"Format   : {dataset['format']}")
print(f"Public   : {dataset['public']}")
print("=============================")

# --- Partie 2 Structure de controle ---
while True:
    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    print("========================")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Vous avez choisi : Ajouter un dataset")
    elif choix == "2":
        print("Vous avez choisi : Afficher les datasets")
    elif choix == "3":
        print("Vous avez choisi : Rechercher")
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, réessayez.")