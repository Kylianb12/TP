# question.py

class Question:
    #Initialise la classe Question avec les parametres : question (str): La question posée, options (list): Liste des options de réponse, correct_answer (str): La réponse correcte.
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.user_answer = None  # Réponse de l'utilisateur initialisée à None

    def is_correct(self):
        #Vérifie si la réponse de l'utilisateur est correcte.

        return self.user_answer and self.user_answer.lower() == self.correct_answer.lower()

    def get_question(self):
        #Récupère la question.
        return self.question

    def get_options(self):
        #Récupère la liste des options de réponse.
        return self.options