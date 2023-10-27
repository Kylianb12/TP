import random
from force_mot_de_passe import ForceMotDePasse

minuscules = 'abcdefghijklmnopqrstuvwxyz'
majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chiffres = '0123456789'
caracteres_speciaux = '!@#$%^&*()_+-=[]{}|;:,.<>?'

class GenerateurMotDePasse:
    @staticmethod
    def generer_mot_de_passe(longueur, num_minuscules, num_majuscules, num_chiffres, num_speciaux):
        caracteres_mot_de_passe = (
            random.choices(minuscules, k=num_minuscules) +
            random.choices(majuscules, k=num_majuscules) +
            random.choices(chiffres, k=num_chiffres) +
            random.choices(caracteres_speciaux, k=num_speciaux)
        )

        longueur_restante = longueur - len(caracteres_mot_de_passe)
        caracteres_mot_de_passe += random.choices(minuscules + majuscules + chiffres + caracteres_speciaux, k=longueur_restante)

        random.shuffle(caracteres_mot_de_passe)
        mot_de_passe = ''.join(caracteres_mot_de_passe)

        entropie = ForceMotDePasse.calculer_entropie(longueur, 94)
        force = ForceMotDePasse.estimer_force(entropie)

        return mot_de_passe, entropie, force
