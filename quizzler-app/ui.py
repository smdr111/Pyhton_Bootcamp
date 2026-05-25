from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_barin):
        self.quiz = quiz_barin
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = Label(text='Score: 0',bg=THEME_COLOR,fg='white')
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg='white',highlightthickness=0)
        self.q_text = self.canvas.create_text(150,125,width=280,text='',fill=THEME_COLOR,font=('Arial',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image,highlightthickness=0,borderwidth=0,command=self.answer_false)
        self.false_button.grid(row=2,column=0)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image,highlightthickness=0,borderwidth=0,command=self.answer_true)
        self.true_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            new_question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text,text=new_question)
        else:
            self.canvas.itemconfig(self.q_text,text=f"You've completed the quiz!"
                                   f"\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')


    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)


