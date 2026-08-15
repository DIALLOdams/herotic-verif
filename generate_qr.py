import json
import os
import qrcode

# ⚠️ À MODIFIER plus tard : mets ici l'adresse de ton site une fois sur GitHub Pages
# Exemple : "https://tonpseudo.github.io/herotic-verif/"
BASE_URL = "https://tonpseudo.github.io/herotic-verif/"

DATA_FILE = "data.json"
OUTPUT_DIR = "qrcodes"

def generer_qrcodes():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        etudiants = json.load(f)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for etudiant_id in etudiants:
        url = f"{BASE_URL}?id={etudiant_id}"

        img = qrcode.make(url)
        chemin = os.path.join(OUTPUT_DIR, f"{etudiant_id}.png")
        img.save(chemin)

        print(f"QR généré pour {etudiant_id} -> {chemin}")
        print(f"   (renvoie vers : {url})")

    print(f"\nTerminé : {len(etudiants)} QR code(s) créé(s) dans le dossier '{OUTPUT_DIR}/'")

if __name__ == "__main__":
    generer_qrcodes()
