# main.py — Application datasetManager
# Partie 1 : types de base, variables, entrées et sorties

# --- Saisie des métadonnées d'un dataset ---
nom = input("Nom du dataset : ")
domaine = input("Domaine : ")
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))
taille = float(input("Taille en Mo : "))
format_dataset = input("Format (csv ou json) : ")
public = input("Public ? (true ou false) : ") == "true"

# --- Affichage d'un résumé formaté ---
print("\n===== Résumé du dataset =====")
print(f"Nom      : {nom}")
print(f"Domaine  : {domaine}")
print(f"Lignes   : {lignes}")
print(f"Colonnes : {colonnes}")
print(f"Taille   : {taille} Mo")
print(f"Format   : {format_dataset}")
print(f"Public   : {public}")
print("=============================")