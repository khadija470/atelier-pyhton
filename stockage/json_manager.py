import json


def sauvegarder_json(datasets):
    with open("data/datasets.json", "w", encoding="utf-8") as fichier:
        json.dump(datasets, fichier, ensure_ascii=False, indent=2)
    print(f"{len(datasets)} dataset(s) sauvegardé(s) dans data/datasets.json")


def recharger_json(datasets):
    try:
        with open("data/datasets.json", "r", encoding="utf-8") as fichier:
            datasets.clear()
            datasets.extend(json.load(fichier))
        if len(datasets) == 0:
            print("Le fichier data/datasets.json est vide.")
        else:
            print(f"{len(datasets)} dataset(s) rechargé(s) depuis data/datasets.json")
    except FileNotFoundError:
        print("Le fichier data/datasets.json n'existe pas encore. Faites d'abord une sauvegarde JSON.")