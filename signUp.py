from tkinter import *

fontStyle = "Tahoma"
fontSize = 18

global windowSize1
windowSize1 = "800x500+380+50"

def signuppage():
    signup = Tk()
    signup.geometry(windowSize1)
    signup.title("Sign Up page")
    global username, name, password
    username = StringVar()
    name = StringVar()
    password = StringVar()
    Label(signup, text="Username", font=(fontStyle, fontSize)).pack(pady=15)
    Entry(signup, textvariable=username, font=(fontStyle, fontSize)).pack(pady=15)
    Label(signup, text="Password", font=(fontStyle, fontSize)).pack(pady=15)
    Entry(signup, textvariable=password, show="$", font=(fontStyle, fontSize)).pack(pady=15)
    Button(signup, text="Sign UP").pack(pady=15)

    signup.mainloop()


# signuppage()
