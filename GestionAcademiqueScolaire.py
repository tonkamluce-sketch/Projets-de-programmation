# Projet de gestion des étudiants

# 2- Créer un étudiant
def ajouter_etudiant(etudiants):
    print("\n--- Ajout d'un étudiant ---")
    nom = input("Nom : ").strip()
    
    # Saisie et validation de l'âge
    while True:
        try:
            age_saisie = input("Âge : ")
            age = int(age_saisie)
            if age < 0 or age > 120:
                raise ValueError("L'âge doit être compris entre 0 et 120.")
            break
        except ValueError as e:
            print(f"Erreur : Veuillez entrer un âge valide (0-120). ({e})")
            
    # Saisie et validation des trois notes
    notes = []
    for j in range(1, 4):
        while True:
            try:
                note_saisie = input(f"Note {j} (sur 20) : ")
                note = float(note_saisie)
                if note < 0 or note > 20:
                    raise ValueError("La note doit être comprise entre 0 et 20.")
                notes.append(note)
                break
            except ValueError as e:
                print(f"Erreur : Veuillez entrer une note valide (0-20). ({e})")

    etudiant = {
        "nom": nom,
        "age": age,
        "notes": notes
    }
    etudiants.append(etudiant)
    print("L'étudiant a été ajouté avec succès !")

# 4- Calculer la moyenne
def calculer_moyenne(notes):
    if not notes:
        return 0.0
    return sum(notes) / len(notes)

# 3- Afficher les étudiants
def afficher_etudiants(etudiants):
    if not etudiants:
        print("\nAucun étudiant enregistré pour le moment.")
        return
    
    print("\n--- Liste des étudiants ---")
    for etudiant in etudiants:
        moy = calculer_moyenne(etudiant["notes"])
        print(f"{etudiant['nom']} - {etudiant['age']} ans - Moyenne : {moy:.1f}")

# 5- Trouver le meilleur étudiant
def meilleur_etudiant(etudiants):
    if not etudiants:
        print("\nAucun étudiant enregistré.")
        return
    
    meilleur = etudiants[0]
    meilleure_moy = calculer_moyenne(meilleur["notes"])
    
    for etudiant in etudiants[1:]:
        moy = calculer_moyenne(etudiant["notes"])
        if moy > meilleure_moy:
            meilleure_moy = moy
            meilleur = etudiant
            
    print(f"\nMeilleur étudiant : {meilleur['nom']}")
    print(f"Moyenne : {meilleure_moy:.1f}")

# 6- Rechercher un étudiant
def rechercher_etudiant(etudiants):
    if not etudiants:
        print("\nAucun étudiant enregistré.")
        return
        
    recherche = input("\nEntrez le nom de l'étudiant à rechercher : ").strip().lower()
    trouve = False
    
    for etudiant in etudiants:
        if etudiant["nom"].lower() == recherche:
            moy = calculer_moyenne(etudiant["notes"])
            print(f"\nÉtudiant trouvé :")
            print(f"Nom : {etudiant['nom']}")
            print(f"Âge : {etudiant['age']} ans")
            print(f"Notes : {etudiant['notes']}")
            print(f"Moyenne : {moy:.1f}")
            trouve = True
            break
            
    if not trouve:
        print("Étudiant introuvable.")

# Bonus : Afficher les étudiants admis (moyenne >= 10)
def afficher_admis(etudiants):
    print("\n===== ÉTUDIANTS ADMIS =====")
    admis_trouve = False
    for etudiant in etudiants:
        moy = calculer_moyenne(etudiant["notes"])
        if moy >= 10:
            print(f"{etudiant['nom']} : {moy:.1f}")
            admis_trouve = True
    if not admis_trouve:
        print("Aucun étudiant admis pour le moment.")

# 8- Menu principal
def menu():
    etudiants = []
    
    while True:
        print("\n========== GESTION DES ÉTUDIANTS ==========")
        print("1. Ajouter un étudiant")
        print("2. Afficher les étudiants")
        print("3. Rechercher un étudiant")
        print("4. Afficher le meilleur étudiant")
        print("5. Afficher les étudiants admis (Bonus)")
        print("6. Quitter")
        
        choix = input("Votre choix : ").strip()
        
        if choix == '1':
            ajouter_etudiant(etudiants)
        elif choix == '2':
            afficher_etudiants(etudiants)
        elif choix == '3':
            rechercher_etudiant(etudiants)
        elif choix == '4':
            meilleur_etudiant(etudiants)
        elif choix == '5':
            afficher_admis(etudiants)
        elif choix == '6':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez choisir entre 1 et 6.")

# Lancement du programme
if __name__ == "__main__":
    menu()