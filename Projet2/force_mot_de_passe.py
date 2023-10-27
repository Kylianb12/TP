import math

class ForceMotDePasse:
    @staticmethod
    def calculer_entropie(longueur_mot_de_passe, taille_alphabet):
        return longueur_mot_de_passe * math.log2(taille_alphabet)

    @staticmethod
    def estimer_force(entropie):
        if entropie < 64:
            return "Très faible"
        elif entropie < 80:
            return "Faible"
        elif entropie < 100:
            return "Moyen"
        else:
            return "Fort"

    @staticmethod
    def tester_mot_de_passe(mot_de_passe):
        entropie = ForceMotDePasse.calculer_entropie(len(mot_de_passe), 94)
        force = ForceMotDePasse.estimer_force(entropie)
        return entropie, force
