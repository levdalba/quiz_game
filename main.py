import requests
from question_model import Question
from quiz_brain import QuizBrain

url = "https://opentdb.com/api.php?amount=10&category=9&type=boolean"
response = requests.get(url)
question_data = response.json()["results"]

question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
