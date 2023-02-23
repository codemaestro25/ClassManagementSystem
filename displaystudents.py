from tkinter import *
import tkinter.ttk as ttk
from dbtest import getDetails, connection
import tkinter.messagebox as msg
fontStyle = "Tahoma"
fontSize = 12
mFontStyle = "Segoe Print"
mFontSize = 14
bg="#62a4f5"
x1 = 40
x2 = 260
x3= 480

def save():
    id = stId.get()
    name = sName.get()
    dob = sDob.get()
    email = sEmail.get()
    course = sCourse.get()
    phno = sPhno.get()
    if (id == '' or name == '' or dob == '' or email == '' or course == 'Choose Course' or phno == ''):
        msg.showerror("Empty Fields", "Please Fill all the entry fields properly")
        return
    else:
        conn = connection()
        cursor = conn.cursor()
        str="update details set name='"+name+"' , email='"+email+"' , phnno='"+phno+"' , course='"+course+"' , dob='"+dob+"'  where id='"+id+"'"
        if(cursor.execute(str)):
            msg.showinfo("Success","Updated data successfully!")
        else:
            msg.showerror("Error", "Some error occured")
        conn.commit()
        conn.close()


def updateview():
    global stId, sName, sPhno, sEmail, sCourse, sDob
    stId = StringVar()
    sName = StringVar()
    sCourse = StringVar()
    sDob = StringVar()
    sPhno = StringVar()
    sEmail = StringVar()

    selectedItem = table.selection()[0]
    # stId.set(selectedItem)
    stId.set(table.item(selectedItem)['values'][0])
    sName.set(table.item(selectedItem)['values'][1])
    sCourse.set(table.item(selectedItem)['values'][2])
    sDob.set(table.item(selectedItem)['values'][5])
    sPhno.set(table.item(selectedItem)['values'][4])
    sEmail.set(table.item(selectedItem)['values'][3])

    Entry(dispStud, textvariable=stId,  font=(fontStyle, fontSize)).place(x=x1, y=80)
    Entry(dispStud, textvariable=sName,  font=(fontStyle, fontSize)).place(x=x1, y=140)

    Entry(dispStud, textvariable=sPhno,  font=(fontStyle, fontSize)).place(x=x2, y=80)
    Entry(dispStud, textvariable=sDob,  font=(fontStyle, fontSize)).place(x=x2, y=140)

    Entry(dispStud, textvariable=sEmail,  font=(fontStyle, fontSize)).place(x=x3, y=80)

    course = OptionMenu(dispStud, sCourse, "C/C++", "Python", "Adv.Excel", "Web Development", "ReactJs","Django","SQL","Java",".Net","Typing","DLCOA")
    course.place(x=x3, y=140)
    course.config(font=(fontStyle, fontSize))

    Button(dispStud, text="Save Changes", font=(mFontStyle, mFontSize), command=save, bg="#75e075").place(x=200, y=15)



def delete():
    selectedItem = table.selection()[0]
    id = str(table.item(selectedItem)['values'][0])
    print(id)
    conn = connection()
    cursor = conn.cursor()
    str1 = "delete from details where id ='"+id+"'"
    if(cursor.execute(str1)):
        msg.showinfo("Success","Successfully deleted student record")
    else:
        msg.showerror("Error","Cant delete student record")
    conn.commit()
    conn.close()




def displayStudents(root):
    global dispStud, table
    dispStud = Frame(root, bg=bg, width = 700, height=600)
    dispStud.place(x=300,y=0)

    Button(dispStud, text="Update", font=(mFontStyle, mFontSize), command=updateview).place(x=60, y=15)
    Button(dispStud, text="Delete", font=(mFontStyle, mFontSize), command=delete, bg="#f05656").place(x=500, y=15)


    # setting scrollbar
    sBX = Scrollbar(dispStud, orient=HORIZONTAL)
    sBY = Scrollbar(dispStud, orient=VERTICAL)
    table = ttk.Treeview(dispStud, columns=("ID", "Name", "Course", "Email", "Phone No", "DOB", "Remaining Fees"), selectmode="extended",  height=200, yscrollcommand=sBY.set, xscrollcommand=sBX.set)
    sBY.config(command=table.yview)
    sBY.pack(side=RIGHT, fill=Y)
    sBX.config(command=table.xview)
    sBX.pack(side=BOTTOM, fill=X)
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#8199f0", foreground="black", font=(fontStyle,fontSize))
    # Setting headers of the tree
    table.heading('ID', text='ID', anchor=W)
    table.heading('Name',text='Name', anchor=W)
    table.heading('Course',text='Course', anchor=W)
    table.heading('Email',text='Email', anchor=W)
    table.heading('Phone No',text='Phone No', anchor=W)
    table.heading('DOB',text='DOB', anchor=W)
    table.heading('Remaining Fees', text='Remaining Fees', anchor=W)

    # setting columwidth
    # setting width of the columns
    table.column('#0', stretch=NO, minwidth=0, width=0)
    table.column('#1', stretch=NO, minwidth=0, width=40)
    table.column('#2', stretch=NO, minwidth=0, width=100)
    table.column('#3', stretch=NO, minwidth=0, width=100)
    table.column('#4', stretch=NO, minwidth=0, width=120)
    table.column('#5', stretch=NO, minwidth=0, width=100)
    table.column('#6', stretch=NO, minwidth=0, width=80)

    # table.place(x=70, y=60)
    table.pack(pady=(200))

    getDetails(table)

    return dispStud