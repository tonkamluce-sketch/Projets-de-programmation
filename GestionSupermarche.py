# 1- Remplir la liste initiale de produits
def remplir_liste_produit():
    produits_liste = []

    for i in range(1, 4):
        print(f"\n--- Saisie du produit {i} ---")
        nom = " ".join(input("Entrer le nom du produit : ").split())

        while not nom:
            print("Entrer un nom c'est obligatoire")
            nom = " ".join(input("Nom obligatoire : ").split())

        while True:
            try:
                quantite = int(input("Quantite : "))
                if quantite > 0:
                    break
                print("La quantite doit etre superieure a 0")
            except ValueError:
                print("Veuillez entrer un nombre entier valide pour la quantite")

        produit = {"Nom": nom, "Quantite": quantite}
        produits_liste.append(produit)

    print("\nCette liste a été correctement remplie !")
    return produits_liste


# 2- Ajout d'un produit individuel
def ajouter_produit(produits):
    print("\n--- Saisie d'un nouveau produit ---")
    nom = " ".join(input("Entrer le nom du produit : ").split())

    while not nom:
        print("Entrer un nom c'est obligatoire")
        nom = " ".join(input("Nom obligatoire : ").split())

    while True:
        try:
            quantite = int(input("Quantite : "))
            if quantite > 0:
                break
            print("La quantite doit etre superieure a 0")
        except ValueError:
            print("Veuillez entrer un nombre entier valide pour la quantite")

    produit = {"Nom": nom, "Quantite": quantite}
    produits.append(produit)
    print("L'ajout de ce produit a été un véritable succès !")


# 3- Affichage de la liste des produits
def afficher_produit(produits):
    if not produits:
        print("\nAucun produit à afficher.")
        return

    print("\n--- Liste des produits ---")
    for produit in produits:
        print(f"Nom : {produit['Nom']} | Quantite : {produit['Quantite']}")


# 4- Recherche d'un produit par son nom
def rechercher_produit(produits):
    if not produits:
        print("\nLa liste des produits est vide.")
        return

    produit_cherche = " ".join(input("\nEntrer le nom du produit à chercher : ").split())
    trouve = False

    for produit in produits:
        if produit['Nom'].lower() == produit_cherche.lower():
            print(f"\nTrouvé ! Nom : {produit['Nom']} | Quantite : {produit['Quantite']}")
            trouve = True
            break

    if not trouve:
        print("\nProduit introuvable.")


# 5- Affichage du menu
def afficher_menu():
    print("\n========== GESTION DES PRODUITS ==========")
    print("1. Remplir la liste initiale (3 produits)")
    print("2. Ajouter un produit")
    print("3. Afficher les produits")
    print("4. Rechercher un produit")
    print("5. Quitter")


# Fonction principale de gestion
def gestion_produits():
    produits = []
    
    while True:
        afficher_menu()
        choix = input("Entrer le numero de votre choix : ").strip()

        if choix == "1":
            produits = remplir_liste_produit()
        elif choix == "2":
            ajouter_produit(produits)
        elif choix == "3":
            afficher_produit(produits)
        elif choix == "4":
            rechercher_produit(produits)
        elif choix == "5":
            print("\nAu revoir !")
            break
        else:
            print("\nChoix invalide, veuillez réessayer.")


# Lancement du programme
gestion_produits()