from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
mytree = None
def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('school.db')
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

def loginclick() :
    global result
    #เช็คusername/password หรือยัง
    if userentry.get() == "" or pwdentry.get() == "":
        messagebox.showwarning("Admin:","Enter Username and Password first")
        userentry.focus_force()
    else:
        #เช็คว่ามีข้อมูลใน Databaseไหม
        sql = "SELECT * FROM login WHERE user=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            #มีuser ในdb แล้วเช็ค
            print(result)
            sql = "SELECT * FROM login WHERE user=? AND pwd=?"
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
    global mainfrm,midfrm
    
    mainfrm.destroy() # destroy old frame
    mainfrm = Frame(root,bg='#DFAB99')
    mainfrm.rowconfigure((0,1,2,3,4,5),weight=1)
    mainfrm.columnconfigure((0,1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')

    midfrm = Frame(mainfrm,bg='#00BFFF')
    midfrm.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    midfrm.columnconfigure((0,1),weight=1)
    midfrm.grid(row=2,column=0,columnspan=2,sticky='news')

    root.title("Welcome " + result[2] + " " + result[3])

    img= Label(mainfrm,image=img1,bg='#DFAB99')
    img.grid(row=0,columnspan=2,sticky='')

    name=Label(mainfrm,text='Name :'+result[2]+' '+result[3],bg='#DFAB99')
    name.grid(row=1,column=0,sticky='w',padx=15)

    createTreeview()

    Button(mainfrm,text='Add Student',width=10,command=registlayout).grid(row=4,columnspan=2,column=0,sticky='s')
    Button(mainfrm,text='Logut',command=loginlayout).grid(row=5,columnspan=2,column=0)

def createTreeview():
    global mytree, i, treeframe
    # Destroy existing treeframe if it exists

    # Create TreeView Frame
    treeframe = Frame(midfrm)
    treeframe.grid(row=1, column=0, columnspan=2, pady=20, sticky='nwes')

    # Create Scrollbar
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT, fill=Y)
    # Create Treeview with scrollbar(yscrollcommand)
    mytree = ttk.Treeview(treeframe, columns=("std_id", "first_name", "last_name", "username", "password"))
    mytree.pack()
    # config scrollbar on the treeview
    # create headings
    mytree.heading("#0", text="", anchor=W)
    mytree.heading("std_id", text="Student ID", anchor=W)
    mytree.heading("first_name", text="First Name", anchor=W)
    mytree.heading("last_name", text="Last Name", anchor=W)
    mytree.heading("username", text="Username", anchor=W)
    mytree.heading("password", text="Password", anchor=W)
    # Format our columns
    mytree.column("#0", width=0, minwidth=0)  # set minwidth=0 for disable the first default column
    mytree.column("std_id", anchor=W, width=200)
    mytree.column("first_name", anchor=W, width=200)
    mytree.column("last_name", anchor=W, width=200)
    mytree.column("username", anchor=W, width=200)
    mytree.column("password", anchor=W, width=200)
    # clear treeview data
    mytree.delete(*mytree.get_children())  # delete old data from treeview
    # fetch data
    sql = "SELECT * FROM students  ORDER BY std_id ASC"
    cursor.execute(sql)
    result = cursor.fetchall()

    # Add data into treeview
    for i, data in enumerate(result):
        if i % 2 == 1:
            mytree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4]))
        else:
            mytree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4]))

def registlayout() :
    global mainfrm
    global firstname,lastname,stid,username,password,confrm
    treeframe.destroy()

    Label(midfrm,text="  Registration Form",font="Garamond 26 bold",fg='#e4fbff',bg='#1687a7').grid(row=0,column=0,columnspan=2,sticky='news')

    Label(midfrm,text='Student ID :',bg='#00BFFF',fg='#f6f5f5').grid(row=1,column=1,columnspan=2,sticky='w',padx=40)
    stid = Entry(midfrm,width=20,bg='#d3e0ea')
    stid.grid(row=1,column=1,columnspan=2,sticky='',padx=0)

    Label(midfrm,text='First Name :',bg='#00BFFF',fg='#f6f5f5').grid(row=2,column=1,columnspan=2,sticky='w',padx=40)
    firstname = Entry(midfrm,width=20,bg='#d3e0ea')
    firstname.grid(row=2,column=1,columnspan=2,sticky='',padx=0)
    
    Label(midfrm,text='Last Name :',bg='#00BFFF',fg='#f6f5f5').grid(row=3,column=1,columnspan=2,sticky='w',padx=40)
    lastname = Entry(midfrm,width=20,bg='#d3e0ea')
    lastname.grid(row=3,column=1,columnspan=2,sticky='',padx=0)

    Label(midfrm,text='UserName :',bg='#00BFFF',fg='#f6f5f5').grid(row=4,column=1,columnspan=2,sticky='w',padx=40)
    username = Entry(midfrm,width=20,bg='#d3e0ea')
    username.grid(row=4,column=1,columnspan=2,sticky='',padx=0)

    Label(midfrm,text='Password :',bg='#00BFFF',fg='#f6f5f5').grid(row=5,column=1,columnspan=2,sticky='w',padx=40)
    password = Entry(midfrm,width=20,bg='#d3e0ea')
    password.grid(row=5,column=1,columnspan=2,sticky='',padx=0)

    Label(midfrm,text='Confrim Password :',bg='#00BFFF',fg='#f6f5f5').grid(row=6,column=1,columnspan=2,sticky='w',padx=0)
    confrm = Entry(midfrm,width=20,bg='#d3e0ea')
    confrm.grid(row=6,column=1,columnspan=2,sticky='',padx=0)

    cancel=Button(midfrm,text='Cancel',command=welcomepage,bg='#FFFFFF',fg='#000000')
    cancel.grid(row=7,column=0,sticky='w')
    
    summit=Button(midfrm,text='Sumit',command=registration,bg='#0004FF',fg='#FF0000')
    summit.grid(row=7,column=1,sticky='e')


def registration():
    if stid.get() == "":
        messagebox.showwarning("Admin", "Please enter student id.")
        stid.focus_force()
    elif firstname.get() == "":
        messagebox.showwarning("Admin", "Please enter firstname.")
        firstname.focus_force()
    elif lastname.get() == "":
        messagebox.showwarning("Admin", "Please enter lastname.")
        lastname.focus_force()
    elif username.get() == "":
        messagebox.showwarning("Admin", "Please enter username.")
        username.focus_force()
    elif password.get() == "":
        messagebox.showwarning("Admin", "Please enter password.")
        password.focus_force()
    elif confrm.get() == "":
        messagebox.showwarning("Admin", "Please confirm password.")
        confrm.focus_force()
    else:
        sql = "SELECT * FROM students WHERE username=?"
        cursor.execute(sql, [username.get()])
        result = cursor.fetchall()
        if result:
            messagebox.showerror("Admin", "Student ID is already exist. Please try again.")
            username.select_range(0, END)
            username.focus_force()
        if password.get() == confrm.get():
                sql = '''INSERT INTO students  
                VALUES (?, ?, ?, ?, ?)
                '''
                param = [stid.get(), firstname.get(), lastname.get(), username.get(), password.get()]
                cursor.execute(sql, param)
                conn.commit()
                messagebox.showinfo("Admin", "Registration successfully")













createconnection()
root = mainwindow()
img1 = PhotoImage(file='images/profile.png').subsample(2,2)
img2 = PhotoImage(file='images/login.png').subsample(5,5)
img3 = PhotoImage(file='images/search.png')
userinfo = StringVar() #spy for getting user data
pwdinfo = StringVar()  #spy for getting password data
loginlayout()
root.mainloop()
cursor.close()
conn.close()