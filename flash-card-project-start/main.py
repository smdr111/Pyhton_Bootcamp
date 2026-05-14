from tkinter import *
import pandas as pd
import random as rd
BACKGROUND_COLOR = "#B1DDC6"

#-------DATA-------#
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#------GENERATE NEW WORD------#
def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rd.choice(to_learn)
    canvas.itemconfig(language_text,text='French',fill='black')
    canvas.itemconfig(word_text,text=current_card['French'],fill='black')
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = flip_timer = window.after(3000,func=flip_card)


#--------FLIPCARD--------#
def flip_card():
        canvas.itemconfig(language_text,text='English',fill='white')
        canvas.itemconfig(word_text,text=current_card['English'],fill='white')
        canvas.itemconfig(canvas_image,image=card_back)
#------IS KNOWN--------#
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

#--------CANVAS-------#
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400,263,image=card_front)
language_text = canvas.create_text(400,150,text='',fill='Black',font=('Ariel',40,"italic"))
word_text = canvas.create_text(400,263,text='',fill='Black',font=('Ariel',60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#------BUTTONS------#
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

right_button = Button(image=right_image,borderwidth=0,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

wrong_button = Button(image=wrong_image,borderwidth=0,highlightthickness=0,command=generate_word)
wrong_button.grid(row=1,column=0)

generate_word()



window.mainloop()