import sqlite3
from tkinter import messagebox
from tkinter import *

def createconnection() :
    global conn, cursor
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1000
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#4a3933')
    root.title("Grade Report by Napat Phinitsap")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout(root) :
    global userentry
    global pwdentry
    global loginframe
    
    loginframe = Frame(root,bg='#f0a500')
    loginframe.rowconfigure((0,1,2,3,4),weight=1)
    loginframe.columnconfigure((0,1,2),weight=1)
    loginframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    
    loginLb = Label(loginframe,image=pic,compound=LEFT,bg='#f0a500')
    loginLb.grid(row=1,columnspan=1,sticky='es',padx=20,pady=30)
    userLb = Label(loginframe,text="User name",bg='#f0a500',fg='#4a3933')
    userLb.grid(row=1,column=1,sticky='nw',pady=80)
    userentry = Entry(loginframe,bg='#e6d5b8',fg='#4a3933',width=20,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w')
    pwdentry = Entry(loginframe,bg='#e6d5b8',fg='#4a3933',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=1,column=1,sticky='ws',pady=40)
    passLb = Label(loginframe,text="Password",bg='#f0a500',fg='#4a3933')
    passLb.grid(row=1,column=1,sticky='ws',pady=80)
    Button(loginframe,text="Reset",width=5,command=resetclick).grid(row=2,column=0,pady=20,sticky='ne',padx=20)
    Button(loginframe,text="Login",width=5,command=loginclick).grid(row=2,column=1,pady=20,sticky='nw',padx=40)

def loginclick() :
    global result
    #เช็คusername/password หรือยัง
    if userentry.get() == "" or pwdentry.get() == "":
        messagebox.showwarning("Admin","Enter user of pass first")
        userentry.focus_force()
    else:
        #เช็คว่ามีข้อมูลใน Databaseไหม
        sql = "SELECT * FROM Students WHERE username=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            #มีuser ในdb แล้วเช็ค
            print(result)
            sql = "SELECT * FROM Students WHERE username=? AND password=?"
            cursor.execute(sql,[userinfo.get(), pwdinfo.get()])
            result = cursor.fetchone()
            if result:
                #ถ้าUser ถูกต้อง
                print(result[0],result[1],result[2])
                messagebox.showinfo('Admin','Login Succesfully.')
                welcomepage()#เรียกใช้ฟังก์ชันไปอีกหน้า
            else: #ถ้าUser ผิดพลาด
                messagebox.showwarning("Admin","Username or Password is invaild")
                userentry.focus_force()
        else:
            messagebox.showwarning("Admin","Username or Password is invaild")
            userentry.focus_force()
def resetclick() :
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    userentry.focus_force()
def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
def welcomepage() :
    welcomeframe = Frame(root,bg='#33CCFF')
    welcomeframe.rowconfigure((0,1,2),weight=1)
    welcomeframe.columnconfigure((0,1,2,3),weight=1)
    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')
    Label(welcomeframe,image=pic,compound=LEFT,bg='#33CCFF').grid(row=0,columnspan=4)
    score = result[3]  # ข้อมูลคะแนนอาจต้องแก้ไขตามโครงสร้างฐานข้อมูลของคุณ
    grade = calculate_grade(score)

    Label(welcomeframe,text='%41s'%'Students ID',bg='#33CCFF').grid(row=1,column=0,sticky='w',padx=5)
    Label(welcomeframe,text=str(result[0]),bg='#33CCFF').grid(row=1,column=1,sticky='w')
    Label(welcomeframe,text='%35s'%'Name',bg='#33CCFF').grid(row=2,column=0,sticky='nw')
    Label(welcomeframe,text=str(result[1]+""+result[2]),bg='#33CCFF').grid(row=2,column=1,sticky='nw')
    Label(welcomeframe,text='%33s'%'Score',bg='#33CCFF').grid(row=2,column=0,sticky='nw',padx=20,pady=80)
    Label(welcomeframe,text=str(result[3]),bg='#33CCFF').grid(row=2,column=1,sticky='nw',pady=80)
    Label(welcomeframe,text='%36s'%'Grade',bg='#33CCFF').grid(row=2,column=0,sticky='nw',pady=160)
    Label(welcomeframe,text=str(grade),bg='#33CCFF').grid(row=2,column=1,sticky='nw',pady=160)
    Button(welcomeframe,text="Logout",width=5,command=welcomeframe.destroy,bg='#33CCFF').grid(row=2,column=1,sticky='sw',pady=70)
createconnection()
root = mainwindow()
pic = PhotoImage(file='images/profile.png').subsample(2,2)
userinfo = StringVar() #spy for getting user data
pwdinfo = StringVar()  #spy for getting password data
loginlayout(root)
root.mainloop()