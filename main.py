from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:  # for every dictionary in question_data
    # Take the values in the dictionaries
    questionText = question["text"]  # The actual question text
    questionAnswer = question["answer"]  # The actual answer (True or False)

    newQuestion = Question(questionText, questionAnswer)  # make a new Question object
    questionBank.append(newQuestion)   # Append new Question to questionBank

quiz = QuizBrain(questionBank)

while quiz.stillhasquestions():
    quiz.nextquestion()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score} / 12")
