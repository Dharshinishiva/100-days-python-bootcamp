from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_as_question:
    quiz.next_question()


print("the games has completed")
print(f"your total score {quiz.score}/{quiz.question_number}")
