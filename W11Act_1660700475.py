import sqlite3
from tkinter import messagebox
from tkinter import *
from unittest import result

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('DB/week11_1660700475.db')
    cursor = conn.cursor()
    
def mainwindow() :
    global mainfrm
    
    root = Tk()
    w = 1100 # width of application
    h = 650  # height of application
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#ffadc6')
    root.title("Login/Register Application: ")
    root.option_add('*font',"Calibri 18 bold")
    root.rowconfigure((0,1,2,3),weight=1) # set  4 rows
    root.columnconfigure((0,1,2,3),weight=1) # set  4 columns
    
    mainfrm = Frame(root,bg='lightyellow')
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')
    return root

def loginlayout() :
    global mainfrm
    global userentry, pwdentry
    
    mainfrm.destroy() # destroy old frame

    mainfrm = Frame(root)  # new frame on root​
    mainfrm.rowconfigure(0,weight=1)    # set mainfrm 1 rows
    mainfrm.columnconfigure((0,1),weight=1) # set mainfrm 2 columns
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')  # grid on root
    
    leftfrm = Frame(mainfrm,bg='#4b778d')
    leftfrm.rowconfigure((0,1,2,3),weight=1) # set leftfrm 4 rows
    leftfrm.columnconfigure((0,1),weight=1)  # set leftfrm 2 columns
    leftfrm.grid(row=0,column=0,sticky='news')
    
    rightfrm = Frame(mainfrm,bg='#4b778d')
    rightfrm.rowconfigure(0,weight=1) # set rightfrm 1 row
    rightfrm.columnconfigure(0,weight=1) # set rightfrm 1 column
    rightfrm.grid(row=0,column=1,sticky='news')
    
    # leftfrm widget
    Label(leftfrm,text="Login",font="Calibri 24 bold",bg='#4b778d',fg='#e4fbff').grid(row=0,columnspan=2)
    Label(leftfrm,text="Username : ",bg='#4b778d',fg='#e4fbff').grid(row=1,column=0)
    userentry = Entry(leftfrm,bg='#e4fbff',width=20, textvariable=userinfo) # spy value is userinfo
    userentry.grid(row=1,column=1,sticky='w',padx=10)
    Label(leftfrm,text="Password  : ",bg='#4b778d',fg='#e4fbff').grid(row=2,column=0)
    pwdentry = Entry(leftfrm,bg='#e4fbff',width=20,show='*',textvariable=pwdinfo)  # spy value is pwdinfo
    pwdentry.grid(row=2,column=1,sticky='w',padx=10)
    resistBtn = Button(leftfrm,text="Register",width=10,bg='lightgray',command=registlayout)
    resistBtn.grid(row=3,column=0,pady=15,padx=20,ipady=2,sticky='e')
    loginBtn = Button(leftfrm,text="Login",width=10,command=loginclick,bg='#5067EC',fg='#e4fbff')
    loginBtn.grid(row=3,column=1,pady=15,padx=20,ipady=2,sticky='w')
    
    # rightfrm widget
    Label(rightfrm,image=imgregist,bg='#4b778d').grid(row=0, sticky='ne')
    
def registlayout() :
    global mainfrm
    global fullname,lastname,newuser,newpwd,cfpwd
    
    mainfrm.destroy() # destroy old frame
    
    mainfrm = Frame(root,bg='#6c5b7b')  # new frame on root​
    mainfrm.rowconfigure(0,weight=1)
    mainfrm.columnconfigure((0,1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news') # grid on root

    leftfrm = Frame(mainfrm,bg='#6c5b7b')
    leftfrm.grid(row=0,column=0,sticky='news')
    leftfrm.rowconfigure(0,weight=1)
    leftfrm.columnconfigure(0,weight=1)
    
    rightfrm = Frame(mainfrm,bg='#6c5b7b')
    rightfrm.grid(row=0,column=1,sticky='news')
    rightfrm.rowconfigure((0,1,2,3,4,5,6),weight=1) # set rightfrm 7 rows
    rightfrm.columnconfigure((0,1),weight=1)        # set rightfrm 2 columns
    
    # leftfrm widget
    Label(leftfrm,image=imgregist,bg='#4b778d').grid(sticky='nw')
    
    # rightfrm widget
    Label(rightfrm,text="Registration Form",font="Garamond 26 bold",fg='#e4fbff',image=imgprofile,compound=LEFT,bg='#1687a7').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(rightfrm,text='Full name : ',bg='#6c5b7b',fg='#f6f5f5').grid(row=1,column=0,sticky='e',padx=10)
    fullname = Entry(rightfrm,width=20,bg='#d3e0ea')
    fullname.grid(row=1,column=1,sticky='w',padx=10)
    Label(rightfrm,text='Last name : ',bg='#6c5b7b',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    lastname = Entry(rightfrm,width=20,bg='#d3e0ea')
    lastname.grid(row=2,column=1,sticky='w',padx=10)
    Label(rightfrm,text="Username : ",bg='#6c5b7b',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    newuser = Entry(rightfrm,width=20,bg='#d3e0ea')
    newuser.grid(row=3,column=1,sticky='w',padx=10)
    Label(rightfrm,text="Password : ",bg='#6c5b7b',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    newpwd = Entry(rightfrm,width=20,bg='#a1cae2',show='*')
    newpwd.grid(row=4,column=1,sticky='w',padx=10)
    Label(rightfrm,text="Confirm Password : ",bg='#6c5b7b',fg='#f6f5f5').grid(row=5,column=0,sticky='e',padx=10)
    cfpwd = Entry(rightfrm,width=20,bg='#a1cae2',show='*')
    cfpwd.grid(row=5,column=1,sticky='w',padx=10)
    backBtn = Button(rightfrm,text="Back to Login",command=loginlayout)
    backBtn.grid(row=6,column=0,ipady=5,ipadx=5,pady=5,sticky='e',padx=10)
    submitBtn = Button(rightfrm,text="Register Submit",command=registration,bg='#4b778d',fg='#e4fbff')
    submitBtn.grid(row=6,column=1,ipady=5,ipadx=5,pady=5,sticky='w')
    fullname.focus_force()
    
def registration() :
    print("Hello from registration")
    #check firstname
    if fullname.get() == "" :
        messagebox.showwarning("Admin","Please enter firstname.")
        fullname.focus_force()
    #check lastname
    elif lastname.get() == "" :
        messagebox.showwarning("Admin","Please enter lastname.")
        lastname.focus_force()
    #check newuser
    elif newuser.get() == "" :
        messagebox.showwarning("Admin","Please enter username.")
        newuser.focus_force()
    #check newpwd
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin","Please enter password.")
        newpwd.focus_force()
    #check cfpwd
    elif cfpwd.get() == "" :
        messagebox.showwarning("Admin","Please confirm password.")
        cfpwd.focus_force()
    else :
        sql = "SELECT * FROM customers WHERE username=?"
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("Admin","Username is already exist")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
            if newpwd.get() == cfpwd.get():
                sql = """INSERT INTO customers (username, password, fname, lname)
                VALUES (?, ?, ?, ?)""" #insert statement
                param = [newuser.get(),newpwd.get(),fullname.get(),lastname.get()]
                cursor.execute(sql,param)
                conn.commit()
                messagebox.showinfo("Admin","Register successfully.")
                retrivedata()
                cleardata()
            else :
                messagebox.showwarning("Admin","Incorrect confirm password\n Try again")
    #check The username is already exists
def cleardata():
    fullname.delete(0,END)
    lastname.delete(0,END)

def loginclick() :
    global user_result
    
    user = userinfo.get()
    pwd = pwdinfo.get()
    if userentry.get() == "" or pwdentry.get() == "":
        messagebox.showwarning("Admin:","Please enter Username and Password.")
        userentry.focus_force()
    else :
        sql = "SELECT * FROM customers WHERE username=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            sql = "SELECT * FROM customers WHERE username=? AND password=? "
            cursor.execute(sql, [user,pwd])   #case1
            user_result = cursor.fetchone()
            if user_result :
                messagebox.showinfo("Admin:","Login Successfully")
                print(user_result)
                userinfo.set("") # clear username input
                pwdinfo.set("")  # clear password input
                welcomepage()
            else :
                messagebox.showwarning("Admin:","Incorrect Username or Password.")
                pwdentry.delete(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login.")
            userentry.delete(0,END)
            userentry.focus_force()
    
def welcomepage() :
    global mainfrm
    
    mainfrm.destroy() # destroy old frame
    mainfrm = Frame(root,bg='#4a3933')
    mainfrm.rowconfigure((0,1,2),weight=1)
    mainfrm.columnconfigure((0,1),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')
    
    Label(mainfrm,text="Welcome to Main Page",fg='yellow',bg='#4a3933',font='Mali 32 bold',image=imgprofile,compound=LEFT).grid(row=0,columnspan=4)
    Label(mainfrm,text="Welcome : ").grid(row=1,column=0, sticky='ne')
    Label(mainfrm,text=user_result[2]+" "+user_result[3]).grid(row=1,column=1, sticky='nw')
    Button(mainfrm,text="Exit",width=10,height=1,command=loginlayout).grid(row=2,column=1,pady=10,padx=15,sticky=E)

def retrivedata() :
    sql = "select * from customers"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)
        
createconnection()
root = mainwindow()

#login spy
userinfo = StringVar() #spy for getting user data
pwdinfo = StringVar() #spy for getting password data

imgregist = PhotoImage(file='images/profile.png')
imgprofile = PhotoImage(file='images/profile.png').subsample(5,5)

loginlayout()
root.mainloop()

cursor.close() #close cursor
conn.close() #close database connection