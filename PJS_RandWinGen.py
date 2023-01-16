from tkinter import *
from random import randint
import random
 
root = Tk()
root.title('PinPassGen 1.5')
root.geometry("500x300")
root.configure(bg="lightgrey")
app_width = 500
app_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

TYPE = IntVar()
result = "12345"
 
 
# Create Password
def make_Password(length):
    my_password = "".join([chr(randint(33, 126)) for _ in range(length)])
    return my_password
 
#Create a PIN
def make_Pin(length):
    my_pin = "".join([chr(randint(48,57)) for _ in range(length)])
    return my_pin
 
#Copy to Clipboard 
def clipper():
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()
 
def passpin():
    global result
    pw_result.delete(0, END)                # Clear result field
    len_str = my_entry.get()                # Get length as a string
    if len_str.isdigit():                   # Check for numeric length
        res_length = int(len_str)           # get required length of Pin or Password
        if TYPE.get() == 1:                 # Compute a PIN
            if res_length > 15:
                result = "Max Pin length is 15"
            else:
                result = make_Pin(res_length)       # Call make_Pin(), telling it the length required
        else:                                   # Generate a Password
            result = make_Password(res_length)  # Call make_Password(), telling it the length required
    else:
        result = "Invalid length"
    pw_result.insert(0, result)             # Display PIN or Password in output field
 
 
# Create a frame for our input box
lf = LabelFrame(root, text="How Many Characters?", bg="lightgrey", width=10)
lf.grid(row=0, columnspan=3, padx=50, pady=5)
 
# Create a frame for our Radio Buttons
radf = LabelFrame(root, text="Choose Security Type", bg="lightgrey")
radf.grid(row=1, column=0, padx=50, pady=5)
 
# create a frame for our buttons
my_frame = LabelFrame(root, text="Generate/Copy", bg="lightgrey")
my_frame.grid(row=2, column=0, padx=50, pady=5)
 
# create a frame for our output box
my_output = LabelFrame(root, text="Your New Pin/Password", bg="lightgrey")
my_output.grid(row=3, column=0, padx=50, pady=5)
 
# Create entry box to designate number of characters
my_entry = Entry(lf, font=("helvetica", 24), width=7, justify="center")
my_entry.grid(row=0, column=0, padx=5, pady=2)
 
# create result box for our returned password
pw_result = Entry(my_output, text='', font=("helvetica", 24), bd=0, bg="lightgrey")
pw_result.grid(row=0, columnspan=3)
 
# create our buttons
# my_button = Button(my_frame, text="Generate Pin/Pass", command=Password, bg="lightgrey")
my_button = Button(my_frame, text="Generate Pin/Pass", command=passpin, bg="lightgrey")
my_button.grid(row=1, column=0, padx=10)
 
clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper, bg="lightgrey")
clip_button.grid(row=1, column=1)
 
# create radio buttons
Radiobutton(radf, text="Pin", bg="lightgrey", padx=20, variable=TYPE, value=1).pack(anchor=W)
Radiobutton(radf, text="Password", bg="lightgrey", padx=20, variable=TYPE, value=2).pack(anchor=W)

credlabel = Label(root, text="Programmed by David J. Kingsley Jr. with aid from Mike K.") 
 
# function
Pin = "1234567890"
 
root.mainloop()
