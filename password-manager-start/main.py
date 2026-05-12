from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_list = []
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get()
    new_data = {
        website:{'email': email,
                "password": password

        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops',message="Don't leave any fields empty" )
    else:
        is_ok = messagebox.askokcancel(title=website,message=f'Details entered:\n{email}\n{password}\nIs it ok to save?')
        if is_ok:
            try:
                with open('data.json','r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json','w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                web_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get().lower()
    try:
        with open('data.json','r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops',message='No Data File Found')
    else:
        if website in data:
            messagebox.showinfo(title=website.title(),message=f"Email:{data[website]['email']}\nPassword:{data[website]['password']}")
        else:
            messagebox.showinfo(title='Oops',message=f"No details for the {website} exists")
    finally:
        web_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

 # ------LABELS-------#
web_label = Label(text='Website:')
web_label.grid(row=1,column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2,column=0)

password_label = Label(text='Password:')
password_label.grid(row=3,column=0)

#-------ENTRIES---------#
web_entry = Entry(width=18)
web_entry.grid(row=1,column=1)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'ovsamandar111@gmail.com')

password_entry = Entry(width=18)
password_entry.grid(row=3,column=1)

#-----BUTTONS-----#
generate_button = Button(text='Generate Password',command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)

#--------CANVAS-------#

canvas = Canvas(width=200,height=200)
pass_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=pass_image)
canvas.grid(row=0,column=1)



window.mainloop()