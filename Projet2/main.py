# main.py

# Importation des classes GenerateurMotDePasse et GenerateurPhrasePasse depuis les modules correspondants
from generateur_de_mot_de_passe import GenerateurMotDePasse
from generateur_de_passphrase import GenerateurPassphrase
from force_mot_de_passe import ForceMotDePasse

def tester_mot_de_passe_utilisateur():
    mot_de_passe_utilisateur = input("Veuillez entrer votre mot de passe : ")
    entropie, force = ForceMotDePasse.tester_mot_de_passe(mot_de_passe_utilisateur)
    print(f"Entropie du mot de passe : {int(entropie)} bits")
    print(f"Force du mot de passe : {force}")

def generer_mot_de_passe():
    print("=== Générateur de Mot de Passe ===")

    # Demande à l'utilisateur de spécifier les critères pour le mot de passe
    while True:
        longueur = int(input("Longueur du mot de passe : "))
        num_minuscules = int(input("Nombre de minuscules : "))
        num_majuscules = int(input("Nombre de majuscules : "))
        num_chiffres = int(input("Nombre de chiffres : "))
        num_speciaux = int(input("Nombre de caractères spéciaux : "))    
        # Vérifie si la somme minimale des caractères spécifiés dépasse la longueur du mot de passe
        if (num_minuscules + num_majuscules + num_chiffres + num_speciaux) <= longueur:
            break
        else:
            print("La somme minimale des caractères spécifiés dépasse la longueur du mot de passe. Réessayez.")

    # Instanciation du générateur de mot de passe
    generateur_mot_de_passe = GenerateurMotDePasse()

    # Appel de la méthode pour générer le mot de passe avec les critères spécifiés
    mot_de_passe, entropie, force = generateur_mot_de_passe.generer_mot_de_passe(longueur, num_minuscules, num_majuscules, num_chiffres, num_speciaux)

    # Affichage du mot de passe généré ainsi que son entropie et sa force
    print(f"Mot de passe : {mot_de_passe}")
    print(f"Entropie : {int(entropie)} bits")
    print(f"Force : {force}")
    print()

def generer_passphrase():
    print("=== Générateur de Passphrase ===")
    chemin_fichier = 'C:/Users/kbekh/TP1/Projet2/wordlist.txt'
    passphrase_gen = GenerateurPassphrase()
    generated_passphrase = passphrase_gen.generer_passphrase(chemin_fichier)
    print("Votre passphrase est :", generated_passphrase)

def main():
    while True:
        print("=== Menu Principal ===")
        print("1. Testeur de Mot de Passe")
        print("2. Generateur de Mot de Passe")
        print("3. Generateur de Passphrase")
        print("4. Sortir")

        choix_menu = input("Veuillez choisir un menu (1, 2, 3 ou 4) : ")

        if choix_menu == "1":
            # Testeur de Mot de Passe
            tester_mot_de_passe_utilisateur()

        elif choix_menu == "2":
            # Generateur de Mot de Passe
            generer_mot_de_passe()

        elif choix_menu == "3":
            # Generateur de Passphrase
            generer_passphrase()

        elif choix_menu == "4":
            print("Sortie du programme.")
            break

        else:
            print("Choix invalide. Veuillez choisir un menu valide (1, 2, 3 ou 4).")

# Exécution de la fonction main si le script est exécuté directement
if __name__ == "__main__":
    main()