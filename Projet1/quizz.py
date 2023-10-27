# quizz.py

import random
from questions import Question

class QCM:
    def __init__(self):
        self.questions = []  # Liste pour stocker les questions du QCM
        self.score = 0  # Score initialisé à zéro

    def add_question(self, question):
        #Ajoute une question à la liste des questions du QCM.
        self.questions.append(question)

    def start_quiz(self):
        #Lance le quiz en affichant les questions de manière aléatoire et en prenant les réponses de l'utilisateur.
        random.shuffle(self.questions)  # Mélangez les questions avant de commencer le quiz
        for i, question in enumerate(self.questions, 1):
            random.shuffle(question.options)  # Mélangez les options de réponse pour chaque question
            print(f"Question {i}: {question.get_question()}\n")
            options = question.get_options()
            for j, option in enumerate(options, 1):
                print(f"{chr(96 + j)}) {option}")
            while True:
                user_answer = input("Veuillez choisir votre réponse : ").lower()
                if user_answer in ["a", "b", "c"]:
                    user_option_index = ord(user_answer) - ord("a")
                    question.user_answer = options[user_option_index]
                    if question.user_answer == question.correct_answer:
                        self.score += 1  # Incrémente le score si la réponse est correcte
                    break
                else:
                    print("Vous devez choisir les reponses 'a', 'b' ou 'c'.")

    def show_score(self):
        #Affiche le score final et la correction du quiz.
        print("\nScore final :")
        print(f"Vous avez obtenu le score de {self.score}/{len(self.questions)}.\n")
        print("Correction :")
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.get_question()}")
            if question.user_answer:
                user_answer = question.user_answer.lower()
                correct_answer = question.correct_answer.lower()
                if user_answer == correct_answer:
                    print(f"Votre réponse : {question.user_answer} (Correcte)")
                else:
                    print(f"Votre réponse : {question.user_answer} (Incorrecte)")
                print(f"Réponse correcte : {question.correct_answer}\n")
