from tkinter import *
import random


def add_participant():
    participant = entry.get()
    participants.append(participant)
    entry.delete(0, END)


def delete_all():
    participants.clear()


def select_winner():
    if participants:
        winner = random.choice(participants)
        label_winner.config(text=f"{winner}", fg='orange', font="bold 50")
        participants.remove(winner)
    else:
        label_winner.config(text="No participants", fg='red', font="bold 50")


def exit_program():
    root.destroy()


root = Tk()
root.title("PJS Scholarship Award")
app_width = 573
app_height = 770
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.configure(bg='#404040')



participants = []

main_frame = Frame(root, bg='#404040', relief=SUNKEN, bd=2)
main_frame.grid(row=1, columnspan=3, padx=30, pady=30)

button_frame = Frame(main_frame, bg='#404040', relief=SUNKEN, bd=1)
button_frame.grid(row=4, columnspan=3, padx=10, pady=10)

label_title = Label(root, text="Pressure Junkies Scuba\nScholarship Winner", bg='#404040', fg='#D01110', font="bold 35")
label_title.grid(row=0, columnspan=3, pady=20)

win_label = Label(main_frame, bg='#404040', fg='#EEEDE7', text="Winner:", font="bold 36")
win_label.grid(row=1, columnspan=3, pady=20)

label_winner = Label(main_frame, text="Please enter\n participants!", bg='#404040', fg='#145DA0', font="bold 30")
label_winner.grid(row=2, columnspan=3, pady=20)

entry = Entry(button_frame, justify="center", bg='#868B8E', font="bold 30", width=15)
entry.grid(row=0, columnspan=2, pady=10)

winner_button = Button(button_frame, text="Select Winner", bg='green', fg='white', command=select_winner, width=30, height=5)
winner_button.grid(row=1, column=0, padx=10)

exit_button = Button(button_frame, text="Exit", bg='#D01110', fg='white', command=exit_program, width=30, height=5)
exit_button.grid(row=1, column=1, padx=10, pady=10)

add_button = Button(button_frame, text="Add", bg="#145DA0", fg="silver", command=add_participant, width=30, height=5)
add_button.grid(row=2, column=0, padx=10, pady=10)

delete_button = Button(button_frame, text="Delete All", bg="#145DA0", fg="silver", command=delete_all, width=30, height=5)
delete_button.grid(row=2, column=1, padx=10)

#for button in button_frame.winfo_children():
 #   button.configure(width=30, height=5)

root.mainloop()
