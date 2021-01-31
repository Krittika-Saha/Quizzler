from tkinter import *
from quiz_brain import QuizBrain
from turtle import Screen
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain, user_high_score, high_score, high_scorer, name):
        self.user_high_score = user_high_score
        self.name = name
        self.high_score = high_score
        self.user_answer = ''
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.high_score_label = Label(text=f'Your High Score: {self.user_high_score}', fg="white", bg=THEME_COLOR)
        self.high_score_label.grid(row=0, column=0)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2)
        self.absolute_high_score_label = Label(text=f'High Score: {high_scorer}, {self.high_score}', fg="white", bg=THEME_COLOR)
        self.absolute_high_score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.score > self.user_high_score:
            self.high_score_label.config(text=f"Your High Score: {self.quiz.score}")
        if self.quiz.score > self.high_score:
            self.absolute_high_score_label.config(text=f"High Score: {self.name}, {self.quiz.score}")
        if self.user_high_score > self.high_score:
            self.absolute_high_score_label.config(text=f"High Score: {self.name}, {self.user_high_score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            if self.quiz.score <= 5:
                self.canvas.itemconfig(self.question_text, text=f"""You've reached the end of the quiz.
Final Score: {self.quiz.score}/{self.quiz.question_number} 
🤦‍
Try harder next time""")
            else:
                self.canvas.itemconfig(self.question_text, text=f"""You've reached the end of the quiz.
Final Score: {self.quiz.score}/{self.quiz.question_number} 
Good Job!""")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green',highlightthickness=0)
        else:
            self.canvas.config(bg='red', highlightthickness=0)
        self.window.after(1000, self.get_next_question)


