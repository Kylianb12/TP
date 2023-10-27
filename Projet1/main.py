# main.py
from quizz import QCM  # Importe la classe QCM du module quizz
from questions import Question  # Importe la classe Question du module questions

if __name__ == "__main__":
    # Création des questions de la classe Question pour le QCM
    question1 = Question("Quelle est la capitale de la France ?", ["Paris", "Berlin", "Londres"], "Paris")
    question2 = Question("Quelle est la capitale de l'Allemagne ?", ["Bruxelles", "Berlin", "Amsterdam"], "Berlin")
    question3 = Question("Quelle est la capitale de la Belgique ?", ["Bruges", "Bruxelles", "Lisbonne"], "Bruxelles")
    question4 = Question("Quelle est la capitale de l'Espagne ?", ["Madrid", "Vienne", "Barcelone"], "Madrid")
    question5 = Question("Quelle est la capitale de l'Italie ?", ["Milan", "Vatican", "Rome"], "Rome")
    question6 = Question("Quelle est la capitale de l'Angleterre ?", ["Édimbourg", "Dublin", "Londres"], "Londres")
    question7 = Question("Quelle est la capitale de la Suisse ?", ["Berne", "Amsterdam", "Budapest"], "Berne")
    question8 = Question("Quelle est la capitale du Portugal ?", ["Porto", "Lisbonne", "Athènes"], "Lisbonne")
    question9 = Question("Quelle est la capitale de l'Australie ?", ["Sydney", "Canberra", "Wellington"], "Canberra")
    question10 = Question("Quelle est la capitale de la Norvège ?", ["Oslo", "Stockholm", "Helsinki"], "Oslo")

    qcm = QCM()
    qcm.add_question(question1)  # Ajoute les questions au QCM
    qcm.add_question(question2)
    qcm.add_question(question3)
    qcm.add_question(question4)
    qcm.add_question(question5)
    qcm.add_question(question6)
    qcm.add_question(question7)
    qcm.add_question(question8)
    qcm.add_question(question9)
    qcm.add_question(question10)

    qcm.start_quiz()  # Démarre le quiz
    qcm.show_score()  # Affiche le score final et les corrections du quiz
