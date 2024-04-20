import sqlite3
from tkinter import messagebox
from tkinter import *

def createconnection() :
    global conn, cursor
    conn = sqlite3.connect('week11_1660700475.db')
    cursor = conn.cursor()

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
    loginpng = Label(loginframe,text="Account Login",font="Garamond 26 bold",fg='#EA8CFF',image=loginl,compound=TOP,bg='#EA8CFF')
    loginpng.grid(row=0,columnspan=2)
    userLb = Label(loginframe,text="User name : ",bg='#f0a500',fg='#4a3933',padx=20)
    userLb.grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e6d5b8',fg='#4a3933',width=20,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e6d5b8',fg='#4a3933',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    passLb = Label(loginframe,text="Password  : ",bg='#f0a500',fg='#4a3933',padx=20)
    passLb.grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Register",width=10,command=registlayout).grid(row=3,columnspan=2,pady=20,ipady=15,sticky='')#ปุ่มregister
    Button(loginframe,text="Login",width=10,command=loginclick).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=20)#ปุ่มlogim
    Button(loginframe,text="exit",command=exit,width=10).grid(row=3,column=0,pady=20,ipady=15,sticky='w',padx=30)#ปุ่มexit
def loginclick() :
    global result
    #เช็คusername/password หรือยัง
    if userentry.get() == "" or pwdentry.get() == "":
        messagebox.showwarning("Admin:","Enter Username and Password first")
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
                
                messagebox.showinfo('Admin','Login Succesfully.')
                welcomepage()#เรียกใช้ฟังก์ชันไปอีกหน้า
            else: #ถ้าUser ผิดพลาด
                messagebox.showwarning("Admin:","Username or Password is invalid")
                userentry.focus_force()
        else:
            messagebox.showwarning("Admin:","Username or Password is invalid")
            userentry.focus_force()
def registlayout() :
    global mainfrm
    global fristname,lastname,stid,genderinfo,ss,username,password,confrm
    
    mainfrm.destroy() # destroy old frame
    
    mainfrm = Frame(root,bg='#6c5b7b')  # new frame on root​
    mainfrm.rowconfigure(0,weight=1)
    mainfrm.columnconfigure((0,1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news') # grid on root
    
    rightfrm = Frame(mainfrm,bg='#6c5b7b')
    rightfrm.grid(row=0,column=0,columnspan=2,sticky='news')
    rightfrm.rowconfigure((0,1),weight=1) # set rightfrm 11 rows
    rightfrm.rowconfigure((2),weight=1)
    rightfrm.rowconfigure((3,4,5,6,7,8,9,10,11),weight=1)
    rightfrm.columnconfigure((0,1),weight=1)


    
    Label(rightfrm,text="  Registration Form",font="Garamond 26 bold",fg='#e4fbff',image=profile,compound=LEFT,bg='#1687a7').grid(row=0,column=0,columnspan=2,sticky='news')
    
    Label(rightfrm,text='Student ID:',bg='#6c5b7b',fg='#f6f5f5').grid(row=1,column=0,sticky='ne',padx=15)
    stid = Entry(rightfrm,width=20,bg='#d3e0ea')
    stid.grid(row=1,column=1,sticky='nw',padx=10)
    
    Label(rightfrm,text='First Name : ',bg='#6c5b7b',fg='#f6f5f5').grid(row=2,column=0,sticky='ne')
    fristname = Entry(rightfrm,width=20,bg='#d3e0ea')
    fristname.grid(row=2,column=1,sticky='nw',padx=10)
    
    Label(rightfrm,text='Last name : ',bg='#6c5b7b',fg='#f6f5f5').grid(row=3,column=0,sticky='ne',padx=10)
    lastname = Entry(rightfrm,width=20,bg='#d3e0ea')
    lastname.grid(row=3,column=1,sticky='nw',padx=10)
    
    Label(rightfrm,text='Gender :',bg='#6c5b7b',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    gendermale=Radiobutton(rightfrm,text='Male',fg='#000000',bg='#6c5b7b',variable=genderinfo,value='Male')
    gendermale.grid(row=4,column=1,sticky='w',padx=10,)

    genderwoman = Radiobutton(rightfrm,text='Female',fg='#000000',bg='#6c5b7b',variable=genderinfo,value='Female')
    genderwoman.grid(row=5,column=1,sticky='w',padx=10)


    genderother = Radiobutton(rightfrm,text='Other',fg='#000000',bg='#6c5b7b',variable=genderinfo,value='Other')
    genderother.grid(row=6,column=1,sticky='w',padx=10)

    
    Label(rightfrm,text='Year :',bg='#6c5b7b',fg='#f6f5f5').grid(row=7,column=0,sticky='e',padx=10,)
    ss=Spinbox(rightfrm,from_=1,to=4,justify=LEFT,textvariable=year)
    ss.grid(row=7,column=1,sticky='w',padx=10)
    
    
    Label(rightfrm,text='Username :',bg='#6c5b7b',fg='#f6f5f5').grid(row=8,column=0,sticky='e',padx=10,)
    username = Entry(rightfrm,width=20)
    username.grid(row=8,column=1,sticky='w',padx=10)
    
    Label(rightfrm,text='Password :',bg='#6c5b7b',fg='#f6f5f5').grid(row=9,column=0,sticky='e',padx=10,)
    password = Entry(rightfrm,width=20,show='*')
    password.grid(row=9,column=1,sticky='w',padx=10)
    
    Label(rightfrm,text='Confrim Password :',bg='#6c5b7b',fg='#f6f5f5').grid(row=10,column=0,sticky='e',padx=10,)
    confrm = Entry(rightfrm,width=20,show='*')
    confrm.grid(row=10,column=1,sticky='w',padx=10)
    
    cancel=Button(rightfrm,text='Cancel',command=loginlayout)
    cancel.grid(row=11,column=0,sticky='w',padx=10,)
    sumit=Button(rightfrm,text='Register Now',command=registration)
    sumit.grid(row=11,column=1,sticky='e',padx=10,)


def registration() :
    if  stid.get() == "" :
        messagebox.showwarning("Admin","Please enter student id.")
        stid.focus_force()
    elif fristname.get() == "" : 
        messagebox.showwarning("Admin","Please enter firstname.")
        fristname.focus_force()
    elif lastname.get() == "" :
        messagebox.showwarning("Admin","Please enter lastname.")
        lastname.focus_force()
    elif genderinfo == "" :
        messagebox.showwarning("Admin","Please select gender.")
        #focus ไม่ได้เพราะอะไร งงเหมือนกัน
    elif ss.get() == "" :
        messagebox.showwarning("Admin","Please select year.")
        ss.focus_force
    elif username.get() == "" :
        messagebox.showwarning("Admin","Please enter username.")
        username.focus_force()
    elif password.get() == "" :
        messagebox.showwarning("Admin","Please enter password.")
        password.focus_force()
    elif confrm.get() == "" :
        messagebox.showwarning("Admin","Please confirm password.")
        confrm.focus_force()
    else : 
        sql = "SELECT * FROM Students WHERE username=?"
        cursor.execute(sql,[username.get()])
        result = cursor.fetchall()
        if result  : 
            messagebox.showerror("Admin","Student ID is already exist \n Please try again.") 
            username.select_range(0,END)
            username.focus_force()
        else:
            if password.get() == confrm.get() :
                sql = '''INSERT INTO Students 
                (std_id,first_name,last_name,gender,year,username,password) 
                VALUES (?,?,?,?,?,?,?) 
                '''
                param = [stid.get(),fristname.get(),lastname.get(),genderinfo.get(),year.get(),username.get(),password.get()]
                cursor.execute(sql,param)
                conn.commit()
                messagebox.showinfo("Admin","Registration successfully")
                cleardata() #เมื่อสมัครจะเคลียร์ทุกอย่างที่เคยกรอก
def cleardata() : #ฟังก์ชันเคลียร์
    stid.delete(0,END)
    fristname.delete(0,END)
    lastname.delete(0,END)
    ss.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)
    confrm.delete(0,END)

def welcomepage() :
    global mainfrm
    
    mainfrm.destroy() # destroy old frame
    mainfrm = Frame(root,bg='#DFAB99')
    mainfrm.rowconfigure((0,1,2,3,4,5),weight=1)
    mainfrm.columnconfigure((0,1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')

    img= Label(mainfrm,image=profile,bg='#DFAB99')
    img.grid(row=0,columnspan=2,sticky='')

    Label(mainfrm,text='Students ID :',bg='#DFAB99').grid(row=1,column=0,sticky='e')
    idLb = Label(mainfrm,text=result[0],bg='#DFAB99')
    idLb.grid(row=1,column=1,sticky='w')

    Label(mainfrm,text='Name :',bg='#DFAB99').grid(row=2,column=0,sticky='e')
    namelb = Label(mainfrm,text=result[1]+result[2],bg='#DFAB99')
    namelb.grid(row=2,column=1,sticky='w')

    Label(mainfrm,text='Gender :',bg='#DFAB99').grid(row=3,column=0,sticky='e')
    genderlb = Label(mainfrm,text=result[3],bg='#DFAB99')
    genderlb.grid(row=3,column=1,sticky='w')

    Label(mainfrm,text='Year :',bg='#DFAB99').grid(row=4,column=0,sticky='e')
    yearlb = Label(mainfrm,text=result[4],bg='#DFAB99')
    yearlb.grid(row=4,column=1,sticky='w')

    logout=Button(mainfrm,text='logout',command=mainfrm.destroy)
    logout.grid(row=5,columnspan=2,sticky='')
    #กดlogout จะเคลียร์รหัสที่เคยกรอกด้วย
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    userentry.focus_force()


createconnection()
root = mainwindow()
loginl = PhotoImage(file='images/login.png').subsample(5,5)
profile = PhotoImage(file='images/profile.png').subsample(3,3)
userinfo = StringVar() #spy for getting user data
pwdinfo = StringVar()  #spy for getting password data
genderinfo = StringVar()
year = StringVar()
loginlayout()
root.mainloop()