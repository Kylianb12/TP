import random
import re

class GenerateurPassphrase:
    chemin_fichier = 'C:/Users/kbekh/TP1/Projet2/wordlist.txt'
    @staticmethod
    def generer_passphrase(chemin_fichier, nombre_de_des=5, nombre_d_faces=6, nombre_de_mots=6):
        passphrase = []

        for _ in range(nombre_de_mots):
            resultats_des = [random.randint(1, nombre_d_faces) for _ in range(nombre_de_des)]
            numeros_des = ''.join(map(str, resultats_des))
            mot_secret = GenerateurPassphrase.trouver_mot_secret(chemin_fichier, numeros_des)

            if mot_secret:
                passphrase.append(mot_secret)

        return ' - '.join(passphrase)


    @staticmethod
    def trouver_mot_secret(chemin_fichier, numeros_des):
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            for ligne in fichier.readlines():
                if numeros_des in ligne:
                    ligne_secrete = ligne.strip()
                    mot_secret = re.search('\d+\s+(.*)', ligne_secrete)
                    if mot_secret:
                        return mot_secret.group(1)
        print(f"Aucun mot trouvé pour les dés {numeros_des}")
        return None