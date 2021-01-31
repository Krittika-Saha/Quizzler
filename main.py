from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import pandas as pds
from os import path

high_score=0
absolute_high_score=0
high_scorer = ''
user_name = input("Enter your name: ")
user_scores = []
all_scores = []
all_names = []

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

if path.exists('user_score.csv'):
    data = pds.read_csv('user_score.csv').to_dict(orient='records')
    for i in data:
        all_scores.append(i['User Score'])
        all_names.append(i['User Name'])
        if i['User Name'].lower() == user_name.lower():
            user_scores.append(i['User Score'])
        else:
            user_scores.append(0)
    high_score = max(user_scores)
    absolute_high_score = max(all_scores)
    high_scorer = all_names[all_scores.index(max(all_scores))]


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz, high_score, absolute_high_score, high_scorer, user_name)

if path.exists('user_score.csv'):
    data = pds.read_csv('user_score.csv').to_dict(orient='records')
    data.append({'User Name': user_name, "User Score": quiz.score})
    all_scores.append(quiz.score)
    all_scores.sort(reverse=True) #Arranges in descending order
    data1 = []
    for i in range(len(data)):
        for j in data:
            if j['User Score'] == all_scores[i]:
                data1.append(j)
    print("Leaderboard")
    for k in data1:
        print(f"{k['User Name']}    {k['User Score']}")

    pds.DataFrame(data1).to_csv('user_score.csv', index=False)
else:
    pds.DataFrame({'User Name': user_name, "User Score": quiz.score}, index=[0]).to_csv('user_score.csv', index=False)