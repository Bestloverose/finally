import sqlite3
from tkinter import messagebox
from tkinter import *

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('DB/lab12_1660700475_napat.db')
    cursor = conn.cursor()
    return(conn,cursor)

def mainwindow() :
    global mainfrm
    root = Tk()
    w = 1000
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#6ACBFF')
    root.title("Student Service System by Napat Phinitsap")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    mainfrm = Frame(root,bg='lightyellow')
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')
    return root

def loginlayout() :
    global mainfrm
    global userentry #ประกาศตัวแปรเป็น global 
    global pwdentry
    global loginframe
    mainfrm.destroy()
    #สร้างframe login
    loginframe = Frame(root,bg='#EA8CFF')
    loginframe.rowconfigure((0,1,2,3,),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    #------------เริ่มเอาlabelลง
    loginpng = Label(loginframe,text="Account Login",font="Garamond 26 bold",fg='#0A0EF6',image=img2,compound=TOP,bg='#EA8CFF')
    loginpng.grid(row=0,columnspan=2)
    
    userLb = Label(loginframe,text="User name : ",bg='#f0a500',fg='#4a3933',padx=20)
    userLb.grid(row=1,column=0,sticky='e')
    
    userentry = Entry(loginframe,bg='#e6d5b8',fg='#4a3933',width=20,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    
    pwdentry = Entry(loginframe,bg='#e6d5b8',fg='#4a3933',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    
    passLb = Label(loginframe,text="Password  : ",bg='#f0a500',fg='#4a3933',padx=20)
    passLb.grid(row=2,column=0,sticky='e')
    
    Button(loginframe,text="Exit",width=10,command=exit).grid(row=3,column=0,pady=20,ipady=15,sticky='')#ปุ่มregister
    Button(loginframe,text="Login",width=10,command=loginclick).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=20)
    
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
def changpwd() :
    global cursor, conn, result
    if newpwdentry.get() == "" or confirmpwdentry.get() == "": # ตรวจสอบว่ามีค่าว่างหรือไม่
        messagebox.showwarning("Admin:", "Please fill in all fields")
    elif newpwdentry.get() != confirmpwdentry.get(): # ตรวจสอบว่ารหัสผ่านใหม่ตรงกับยืนยันรหัสผ่านหรือไม่
        messagebox.showwarning("Admin:", "New Password and Confirm Password do not match")
        newpwdentry.delete(0, END)
        confirmpwdentry.delete(0, END)
        newpwdentry.focus_force()
    else:
        # อัปเดตรหัสผ่านในฐานข้อมูลสำหรับผู้ใช้งานที่ตรงกับชื่อผู้ใช้งานที่กำหนด
        sql = "UPDATE student SET password=? WHERE std_id=?"
        cursor.execute(sql, [newpwdentry.get(),result[0]])
        conn.commit()
        messagebox.showinfo("Admin:", "Password has been changed successfully")





def loginclick() :
    global result
    #เช็คusername/password หรือยัง
    if userentry.get() == "" or pwdentry.get() == "":
        messagebox.showwarning("Admin:","Enter Username and Password first")
        userentry.focus_force()
    else:
        #เช็คว่ามีข้อมูลใน Databaseไหม
        sql = "SELECT * FROM Student WHERE username=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            #มีuser ในdb แล้วเช็ค
            print(result)
            sql = "SELECT * FROM Student WHERE username=? AND password=?"
            cursor.execute(sql,[userinfo.get(), pwdinfo.get()])
            result = cursor.fetchone()
            if result:
                #ถ้าUser ถูกต้อง
                
                messagebox.showinfo('Admin','Login Succesfully.')
                welcomepage()#เรียกใช้ฟังก์ชันไปอีกหน้า
            else: #ถ้าUser ผิดพลาด
                messagebox.showwarning("Admin:","Username or Password is invalid")
                userentry.focus_force()
        else:
            messagebox.showwarning("Admin:","Username or Password is invalid")
            userentry.focus_force()


def welcomepage() :
    global mainfrm
    
    mainfrm.destroy() # destroy old frame
    mainfrm = Frame(root,bg='#DFAB99')
    mainfrm.rowconfigure((0,1,2,3,4,5),weight=1)
    mainfrm.columnconfigure((0,1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')

    root.title("Welcome " + result[1] + " " + result[2])

    img= Label(mainfrm,image=img1,bg='#DFAB99')
    img.grid(row=0,columnspan=2,sticky='')

    Label(mainfrm,text='Students ID :',bg='#DFAB99').grid(row=1,column=0,sticky='e')
    idLb = Label(mainfrm,text=result[0],bg='#DFAB99')
    idLb.grid(row=1,column=1,sticky='w')

    Label(mainfrm,text='Name :',bg='#DFAB99').grid(row=2,column=0,sticky='e')
    namelb = Label(mainfrm,text=result[1]+" "+result[2],bg='#DFAB99')
    namelb.grid(row=2,column=1,sticky='w')

    Label(mainfrm,text='Gender :',bg='#DFAB99').grid(row=3,column=0,sticky='e')
    genderlb = Label(mainfrm,text=result[3],bg='#DFAB99')
    genderlb.grid(row=3,column=1,sticky='w')

    Label(mainfrm,text='Year :',bg='#DFAB99').grid(row=4,column=0,sticky='e')
    yearlb = Label(mainfrm,text=result[4],bg='#DFAB99')
    yearlb.grid(row=4,column=1,sticky='w')

    changb = Button(mainfrm,text='Change Password',width=15,height=2,command=pagechang)
    changb.grid(row=5,column=0,sticky='')

    manab = Button(mainfrm,text='Manage Students',command=pagemana,width=15,height=2)
    manab.grid(row=5,column=1,sticky='w')

    logb = Button(mainfrm,text='Log Out',command=loginlayout,width=10,height=2)
    logb.grid(row=5,column=1,sticky='e')
    userentry.delete(0,END)
    pwdentry.delete(0,END)
def pagechang() :
    global mainfrm
    global newpwdentry
    global confirmpwdentry
    mainfrm.destroy() # destroy old frame
    mainfrm = Frame(root,bg='#DFAB99')
    mainfrm.rowconfigure((0,1,2,3,4,5),weight=1)
    mainfrm.columnconfigure((0,1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')

    newpwdLb = Label(mainfrm,text="New Password : ",bg='#DFAB99',fg='#4a3933',padx=20)
    newpwdLb.grid(row=1,column=0,sticky='e')
    newpwdentry = Entry(mainfrm,fg='#4a3933',width=20,show='*')
    newpwdentry.grid(row=1,column=1,sticky='w',padx=20)

    confirmpwdLb = Label(mainfrm,text="Confirm Password : ",bg='#DFAB99',fg='#4a3933',padx=20)
    confirmpwdLb.grid(row=2,column=0,sticky='e')
    confirmpwdentry = Entry(mainfrm,fg='#4a3933',width=20,show='*')
    confirmpwdentry.grid(row=2,column=1,sticky='w',padx=20)

    Button(mainfrm,text="Confirm",width=10,command=changpwd).grid(row=3,column=0,pady=20,ipady=15,sticky='e',padx=20)
    Button(mainfrm,text="Cancel",width=10,command=loginlayout).grid(row=3,column=1,pady=20,ipady=15,sticky='',padx=20)

def pagemana() :
    global mainfrm
    global sbox
    mainfrm.destroy() # destroy old frame
    mainfrm = Frame(root,bg='#DFAB99')
    mainfrm.rowconfigure((0,1,2,3,4,5),weight=1)
    mainfrm.columnconfigure((0,2,),weight=1)
    mainfrm.columnconfigure((1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')

    Label(mainfrm,text='Student ID:',bg='#DFAB99',fg='#000000').grid(row=0,column=0,sticky='e')

    sbox=Entry(mainfrm,width=20)
    sbox.grid(row=0,column=1,sticky='w',padx=20)

    Button(mainfrm,image=img3,command=search_student).grid(row=0,column=1,sticky='w',padx=300)

    Button(mainfrm,text='Back',command=welcomepage).grid(row=0,column=1,sticky='w',padx=350)
def update_student():
    global name_entry, surname_entry, sbox
    first_name = name_entry.get()
    last_name = surname_entry.get()
    student_id = sbox.get()

    if first_name == "" or last_name == "":
        messagebox.showwarning("Admin", "Please fill in all fields.")
    
    else:
        sql = "UPDATE student SET first_name=?, last_name=? WHERE std_id=?"
        cursor.execute(sql, (first_name, last_name, student_id))
        conn.commit()
        messagebox.showinfo("Admin", "Updated successfully.")
        name_entry.delete(0, END)
        surname_entry.delete(0, END)
        sbox.delete(0, END)
        sbox.focus_force()

def search_student():
    global sbox ,name_entry,surname_entry
    student_id = sbox.get() #สำคัญมากกกกกกกก
    sql = "SELECT * FROM student WHERE std_id=?"
    cursor.execute(sql, (student_id,))
    result = cursor.fetchone()
    
    
    if result:
        name_entry = Entry(mainfrm, width=20)
        name_entry.grid(row=1, column=1, sticky='w', padx=20,)
        Label(mainfrm,text='First Name :',bg='#DFAB99',fg='#FFFFFF').grid(row=1,column=0,sticky='e')

        surname_entry = Entry(mainfrm, width=20)
        surname_entry.grid(row=2, column=1, sticky='w', padx=20)
        Label(mainfrm,text='Last Name :',bg='#DFAB99',fg='#FFFFFF').grid(row=2,column=0,sticky='e')
        
        
        name_entry.insert(0, result[1])
        surname_entry.insert(0, result[2])

        Button(mainfrm,text='Update Now',command=update_student).grid(row=3,column=1,sticky='')
        Button(mainfrm,text='Back to My profile',command=welcomepage).grid(row=3,column=1,sticky='e')

    else:
        messagebox.showwarning("Admin", "Data not found.")
        


    
    




createconnection()
root = mainwindow()
img1 = PhotoImage(file='images/profile.png').subsample(2,2)
img2 = PhotoImage(file='images/login.png').subsample(5,5)
img3 = PhotoImage(file='images/search.png')
userinfo = StringVar() #spy for getting user data
pwdinfo = StringVar()  #spy for getting password data
genderinfo = StringVar()
year = StringVar()
loginlayout()

root.mainloop()
