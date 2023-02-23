from tkinter import *
from PIL import ImageTk, Image
from newadmission import newadmsnpage
from fees import feespage
from displaystudents import displayStudents

# from login import session, loginpage
windowSize2 = "1000x600+180+50"
mButtCol = "#80edaf"
mFontStyle = "Segoe Print"
mFontSize = 14

def handlelogout():
    session = False
    mainPage.destroy()
    # lambda : loginpage()

def mainpage(session):

        global mainPage
        mainPage = Tk()
        mainPage.title("Dashboard")
        mainPage.geometry(windowSize2)

        canvas = Canvas(mainPage, width=300, height=600, bg='#3e1199')
        canvas.place(x=0, y=0)
        canvas.config(borderwidth=0, border=0)

        logo = Canvas(canvas, width=300, height=80)
        logo.place(x=0, y=0)
        img = ImageTk.PhotoImage(Image.open("sm_image.jpg"), master=logo)
        logo.create_image(8, 0, anchor=NW, image=img)

        Button(canvas, text="Enroll New Student", font=(mFontStyle, mFontSize), command=lambda : newadmsnpage(mainPage), borderwidth=0, bg="#80edaf").place(x=60, y=120)
        Button(canvas, text="Fees", font=(mFontStyle, mFontSize),command=lambda : feespage(mainPage), borderwidth=0, bg="#80edaf").place(x=60, y=220)
        Button(canvas, text="Students List", font=(mFontStyle, mFontSize), command=lambda: displayStudents(mainPage) , borderwidth=0, bg="#80edaf").place(x=60, y=320)
        Button(canvas, text="Log Out", font=(mFontStyle, mFontSize),borderwidth=1, bg="#b03d35", command=handlelogout, foreground="white").place(x=60, y=460)




        mainPage.mainloop()

# mainpage(True)

