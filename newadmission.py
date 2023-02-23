from tkinter import *
from dbtest import connection
import tkinter.messagebox as msg

fontStyle = "Tahoma"
fontSize = 14
mFontStyle = "Segoe Print"
mFontSize = 14
bg = "#f2f562"
xL = 150
xE = 350
global windowSize2 , canColour , mButtCol
windowSize2 = "1000x600+180+50"
canColour = '#3e1199'
mButtCol = "#80edaf"



# function to show fees
def showFees(event):


    match sCourse.get():
        case "C/C++":
            cFee.set('5000')
        case "Python":
            cFee.set('12000')
        case "Adv.Excel":
            cFee.set('3000')
        case "Web Development":
            cFee.set('8000')
        case "ReactJs":
            cFee.set('6000')
        case "Django":
            cFee.set('4000')
        case "SQL":
            cFee.set('2000')
        case "Java":
            cFee.set('5000')
        case ".Net":
            cFee.set('3000')
        case "Typing":
            cFee.set("4000")
        case "DLCOA":
            cFee.set("8000")
    # if(sCourse.get()=="Java"):
    #     cFee.set("4000")
    Label(newAdd, text="Course Fees", font=(fontStyle, fontSize)).place(x=xL, y=460)
    Entry(newAdd, font=(fontStyle, fontSize), textvariable=cFee, width="10", state='disabled').place(x=xE, y=460)

# function to add the data
def handleNewAdmission():
    print("new addmission button clicked")

    id = sId.get()
    name = sName.get()
    dob = sDob.get()
    email = sEmail.get()
    course = sCourse.get()
    phno = sPhno.get()
    remfee = cFee.get()
    if(id=='' or name =='' or dob=='' or email=='' or course=='Choose Course' or phno==''):
        msg.showerror("Empty Fields", "Please Fill all the entry fields properly")
        return
    else:
        conn = connection()
        cursor = conn.cursor()
        # str = "insert into details (id, name, course, email, phnno, dob) values(?,?,?,?,?,?)",(id, name, course, email, phno, dob)
        str = "insert into details (id, name, course, email, phnno, dob, rem_fees, tot_fees) values('" + id + "','" + name + "','" + course + "','" + email + "','" + phno + "','" + dob + "','" + remfee + "','" + remfee + "')"
        if (cursor.execute(str)):
            msg.showinfo("Success", "Data Entered Successfully!")
            sId.set('')
            sName.set('')
            sEmail.set('')
            sCourse.set('')
            sDob.set('')
            sPhno.set('')
            cFee.set('')
        else:
            msg.showerror("Error", "Some error occurred")
        conn.commit()
        conn.close()






def newadmsnpage(root):
    global newAdd
    newAdd = Frame(root , bg=bg , width=700, height=600)
    newAdd.place(x=300, y=0)

    global sId, sName, sPhno , sEmail, sCourse, sDob, cFee
    sId = StringVar()
    sName = StringVar()
    sDob = StringVar()
    sEmail = StringVar()
    sCourse = StringVar(newAdd)
    sPhno = StringVar()
    cFee = StringVar()


    # design of the page
    Label(newAdd, text="Student ID: ", font=(fontStyle, fontSize),bg=bg).place(x=xL, y=100)
    Entry(newAdd, font=(fontStyle, fontSize), textvariable=sId).place(x=xE, y=100)
    Label(newAdd, text="Student Name: ", font=(fontStyle, fontSize),bg=bg).place(x=xL, y=160)
    Entry(newAdd, font=(fontStyle, fontSize), textvariable=sName).place(x=xE, y=160)
    Label(newAdd, text="Contact Number: ", font=(fontStyle, fontSize),bg=bg).place(x=xL, y=220)
    Entry(newAdd, font=(fontStyle, fontSize), textvariable=sPhno).place(x=xE, y=220)
    Label(newAdd, text="Email ID: ", font=(fontStyle, fontSize),bg=bg).place(x=xL, y=280)
    Entry(newAdd, font=(fontStyle, fontSize), textvariable=sEmail).place(x=xE, y=280)
    Label(newAdd, text="D.O.B: ", font=(fontStyle, fontSize),bg=bg).place(x=xL, y=340)
    Entry(newAdd, font=(fontStyle, fontSize), textvariable=sDob).place(x=xE, y=340)
    Label(newAdd, text="Course ", font=(fontStyle, fontSize),bg=bg).place(x=xL, y=400)
    sCourse.set("Choose Course")
    course = OptionMenu(newAdd, sCourse, "C/C++", "Python", "Adv.Excel", "Web Development", "ReactJs","Django","SQL","Java",".Net","Typing","DLCOA", command=showFees)
    course.place(x=xE, y= 400)
    course.config(font=(fontStyle,fontSize))




    Button(newAdd, text="Enroll Student", command=handleNewAdmission, font=(fontStyle, fontSize)).place(x= 380, y=550)


    return newAdd


