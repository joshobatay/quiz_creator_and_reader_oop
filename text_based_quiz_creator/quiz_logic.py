# I will convert my prevoius code into a class-based structure.
# This code will be used to create a quiz and read it.

import json
from pathlib import Path
import os

class Question:
    def __init__(self, question, choices, correct_answer, explanation):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
        self.explanation = explanation

    def convert_questions_to_dictionary(self):
        return {
            "Question": self.question,
            "Choices": self.choices,
            "Correct Answer": self.correct_answer,
            "Explanation": self.explanation
        }
        
        