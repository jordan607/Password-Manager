from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_number + password_symbol

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_date():

    website =website_entry.get()
    username =username_entry.get()
    password =password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror(title="Error", message="Please Enter credentials")
    else:
        confirmation = messagebox.askokcancel(title= website, message=f"These are details:\n"
                                                   f" Username: {username}\n"
                                                   f" Password: {password}\n"
                                                   f" Is this ok?")

    if confirmation:
        with open("secret_data.txt", "a") as sdfile:
            sdfile.write(f"{website} | {username} | {password}\n")



    website_entry.delete(0, END)
    username_entry.delete(0,END)
    password_entry.delete(0, END)
    username_entry.insert(END, "@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)


canvas = Canvas(width = 200, height = 200)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image= lock_img)
canvas.grid(row = 1, column = 2)

#Labels
website_label = Label(text = "website:" , font = ("Ariel", 10, "bold"), fg = "Teal")
website_label.grid(row = 2, column = 1)

username_label = Label(text = "Email/Username:", font = ("Ariel", 10, "bold"), fg ="Teal")
username_label.grid(row= 3, column = 1)

password_label = Label(text = "Password:", font = ("Ariel",10, "bold"), fg = "Teal")
password_label.grid(row = 4, column = 1)

#Entry

website_entry = Entry(width = 35)
website_entry.grid(row = 2, column = 2, columnspan = 2)
website_entry.focus()

username_entry = Entry(width = 35)
username_entry.grid(row = 3, column = 2, columnspan=2)
username_entry.insert(END, "@gmail.com")

password_entry = Entry(width = 20)
password_entry.grid(row= 4, column = 2)

#Buttons

genpwd_button = Button(text = "Generate Password", width = 15 , command = gen_password, bg= "Lavender")
genpwd_button.grid(row =4, column = 3)


addpwd_button = Button(text = "Add", width = 30, command = save_date, bg = "Lavender")
addpwd_button.grid(row = 5, column = 2, columnspan=2)

window.mainloop()