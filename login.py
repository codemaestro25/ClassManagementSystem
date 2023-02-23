from tkinter import *
from signUp import windowSize1, fontSize, fontStyle
import tkinter.messagebox as msgbox
from dbtest import connection
from mainPage import mainpage, mFontStyle, mFontSize
from PIL import ImageTk, Image



global session
session = False
# login working
def handlelogin():
    print("Login button clicked")
    inpUsr = logId.get()
    inpPass = logPass.get()
    if inpUsr == '' or inpPass == '':
        msgbox.showerror("uh-oh!", "Fields cannot be empty")
    else:
        conn = connection()
        cursor = conn.cursor()
        str = "select * from login where username ='" + inpUsr + "' and password ='" + inpPass + "' "
        cursor.execute(str)

        if cursor.fetchone():
            print("login successfull")
            msgbox.showinfo("Success", "Login Validated")
            session = True
            lWindow.destroy()
            mainpage(session)
            logId.set('')
            logPass.set('')

        else:
            print("Invalid Credentials")
            msgbox.showerror("Error", "Invalid Credentials")




# loginpage design
def loginpage():
    global lWindow
    lWindow = Tk()
    lWindow.geometry(windowSize1)
    lWindow.title("Login Page")
    lWindow.config(bg="#9fcaf5")

    canvas = Canvas(lWindow, width=288, height=80)
    canvas.place(x=250, y=50)
    img = ImageTk.PhotoImage(Image.open("sm_image.jpg"), master = canvas)
    canvas.create_image(0, 0, anchor=NW, image=img)

    global logId, logPass
    logId = StringVar()
    logPass = StringVar()
    Label(lWindow, text="Admin Username", font=(mFontStyle, mFontSize),bg="#9fcaf5").pack(pady=(180, 0))
    Entry(lWindow, textvariable=logId, font=(fontStyle, fontSize)).pack(pady=15)
    Label(lWindow, text="Password", font=(mFontStyle, mFontSize),bg="#9fcaf5").pack(pady=15)
    Entry(lWindow, textvariable=logPass, show="$", font=(fontStyle, fontSize)).pack(pady=15)
    login_but = Button(lWindow, text="Login", font=(fontStyle, fontSize, "bold"), command=handlelogin)
    login_but.pack(pady=15)
    lWindow.mainloop()


loginpage()
