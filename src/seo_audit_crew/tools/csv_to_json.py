import os
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Vérifie si le dossier data existe, sinon le crée
    if not os.path.exists('data'):
        os.makedirs('data')

    # Lecture du fichier CSV
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []

        # Parcours de chaque ligne du CSV
        for row in csv_reader:
            # Conversion des chaînes vides en None pour JSON
            cleaned_row = {key: (value if value else None) for key, value in row.items()}
            data.append(cleaned_row)

    # Ecriture du JSON avec une indentation pour une meilleure lisibilité
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"✅ Conversion terminée ! Le fichier JSON est enregistré à : {json_file_path}")

if __name__ == "__main__":
    # Chemins des fichiers
    csv_file_path = 'exportmagicmorning.csv'
    json_file_path = 'data/exportmagicmorning.json'
    
    # Appel de la fonction de conversion
    csv_to_json(csv_file_path, json_file_path)
