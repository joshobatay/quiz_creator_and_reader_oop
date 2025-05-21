# I will convert my prevoius code into a class-based structure.
# This code will be used to create a quiz and read it.

import json
from pathlib import Path

class Question:
    def __init__(self, question, choices, correct_answer, explanation):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
        self.explanation = explanation

    def convert_questions_to_list(self):
        return {
            "Question": self.question,
            "Choices": self.choices,
            "Correct Answer": self.correct_answer,
            "Explanation": self.explanation
        }
        
class QuizCreator:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.question = []
    
    def add_question(self, question):
        self.question.append(question)
        
    def convert_questions_to_list(self):
        return {
            "quiz_name": self.quiz_name,
            "questions": {
                f"quiz_question_{question_index + 1}": question.convert_questions_to_list()
                for question_index, question in enumerate(self.question)
            }
        }
        
    def save_to_json(self, file_path):
        file_path = Path(file_path)
        with open(file_path, 'w') as file:
            json.dump(self.convert_questions_to_list, file, indent=4)
        print(f"Quiz saved to {file_path}")