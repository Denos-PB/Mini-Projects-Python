from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

q_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    qi = Question(question_text,question_answer)
    q_bank.append(qi)

quiz = Quiz_brain(q_bank)

while quiz.still_have_q():
    quiz.next_q()

print("You have complet a quiz")
print(f"Your final score: {quiz.score}/{quiz.q_num}")
