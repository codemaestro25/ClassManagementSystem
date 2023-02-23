from tkinter import *
from dbtest import connection
import tkinter.messagebox as msg

xL = 130
xE = 370
fontStyle = "Tahoma"
fontSize = 14
bg="#96f781"

def showDetails():
    print("Show details button")

    Label(fees, text="Student ID: ", font=(fontStyle, fontSize), bg=bg).place(x=xL, y=140)
    Label(fees, text="Student Name: ", font=(fontStyle, fontSize), bg=bg).place(x=xL, y=200)
    Label(fees, text="Course Name: ", font=(fontStyle, fontSize), bg=bg).place(x=xL, y=260)
    Label(fees, text="Total Fees: ", font=(fontStyle, fontSize), bg=bg).place(x=xL, y=320)
    Label(fees, text="Remaining Fees: ", font=(fontStyle, fontSize), bg="#8199f0").place(x=xL, y=380)
    Label(fees, text="Installment Amount: ", font=(fontStyle, fontSize), bg=bg).place(x=xL, y=440)

    # labels from database
    Entry(fees, textvariable=stId, state="disabled", font=(fontStyle, fontSize)).place(x=xE, y=140)
    Entry(fees, textvariable=sName, state="disabled", font=(fontStyle, fontSize)).place(x=xE, y=200)
    Entry(fees, textvariable=sCourse, state="disabled", font=(fontStyle, fontSize)).place(x=xE, y=260)
    Entry(fees, textvariable=totFee, state="disabled", font=(fontStyle, fontSize)).place(x=xE, y=320)
    Entry(fees, textvariable=remFee, state="disabled", font=(fontStyle, fontSize)).place(x=xE, y=380)
    Entry(fees, textvariable=instAmt, font=(fontStyle, fontSize)).place(x=xE, y=440)

    Button(fees, text="Update Installment", font=(fontStyle, fontSize), command=updatefees).place(x=300, y=510)

    id = stId.get()
    conn = connection()
    cursor = conn.cursor()
    str = "select id, name, course, rem_fees, tot_fees from details where id='"+id+"'"
    cursor.execute(str)
    result = cursor.fetchone()
    # print(result[1])
    sName.set(result[1])
    sCourse.set(result[2])
    totFee.set(result[4])
    remFee.set(result[3])

def updatefees():
    print("Updated Fees clicked")
    id = stId.get()
    inst = instAmt.get()
    print(inst)
    conn = connection()
    cursor = conn.cursor()
    str="update details set rem_fees = rem_fees-'"+inst+"' where id = '"+id+"'"

    if(cursor.execute(str)):
        msg.showinfo("Success","Fee installment updated succesfully")
    else:
        msg.showerror("Error", "Some error occurred")
    conn.commit()
    conn.close()
    stId.set('')
    instAmt.set('')
    sName.set('')
    sCourse.set('')
    totFee.set('')
    remFee.set('')




def feespage(root):
    global fees, instAmt
    fees = Frame(root, bg="#96f781", width=700, height=600)
    fees.place(x=300, y=0)
    global stId, sName, sCourse, totFee, remFee
    instAmt = StringVar()
    stId = StringVar()

    sName = StringVar()

    totFee = StringVar()
    sCourse = StringVar()
    remFee = StringVar()

    Label(fees, text="EnterStudent ID: ", font=(fontStyle, fontSize),bg=bg).place(x=xL-50, y=50)
    Entry(fees, textvariable=stId, font=(fontStyle,fontSize)).place(x=xE-50, y =50)
    Button(fees, text="View Details", font=(fontStyle,fontSize), command=showDetails).place(x=xE+200, y=50)


    



    return fees


