class QuizBrain:

    def __init__(self, questionlist):
        self.questionNumber = 0
        self.questionList = questionlist
        self.score = 0

    def stillhasquestions(self):
        return self.questionNumber < len(self.questionList)
        # Compares current questionlist index (0 -> 11) with questionlist length (12)

    def nextquestion(self):
        currentquestion = self.questionList[self.questionNumber]  # Prepare the question
        self.questionNumber += 1  # Prepare the question number
        useranswer = input(f"Q.{self.questionNumber}: {currentquestion.text} (True / False)?: ")  # Ask the user
        self.checkanswer(useranswer, currentquestion.answer)  # Compare user answer to correct answer

    def checkanswer(self, useranswer, correctanswer):
        if useranswer.lower() == correctanswer.lower():
            print("You got it right!")
            self.score += 1  # Increase player score
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correctanswer}.")
        print(f"Your current score is: {self.score} / {self.questionNumber}\n")
