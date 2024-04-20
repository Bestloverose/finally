import sqlite3
from tkinter import messagebox
from tkinter import *

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('lab12_1660700475.db')
    cursor = conn.cursor()
    return(conn,cursor)

def mainwindow() :
    root = Tk()
    w = 1000
    h = 600
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#28b5b5')
    #root.config(bg='#4a3933')
    root.title("Login/Register Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout() : #activity of week10
    global userentry,pwdentry,loginframe
    
    loginframe = Frame(root,bg='#8fd9a8')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    
    Label(loginframe,text="Login/Register Application",font="Garamond 26 bold",image=img1,compound=LEFT,bg='#8fd9a8',fg='#e4fbff').grid(row=0,columnspan=2)
    Label(loginframe,text="User name : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',fg="black",width=20)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',fg="black",width=20,show='*')
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#8fd9a8',fg='#e4fbff',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userentry.get(),pwdentry.get())).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=20)
    Button(loginframe,text="Register",width=10,command=regiswindow).grid(row=3,column=1,pady=20,ipady=15,sticky='w',padx=20)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def loginclick(user,pwd) :   #activity of week10 user pwd คือlamda บรรทัด40
    global result
    print("Hello FROM login click")
    if user == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
        userentry.focus_force()
    else :
        sql = "select * FROM students where username=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "SELECT * FROM students WHERE username=? AND password=? "
                cursor.execute(sql,[user,pwd])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    update_page(result[1],result[2])   #call update_page and pass firstname and lastname via parameter
                else :
                    messagebox.showwarning("Admin:","Incorrect Username or Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")
            userentry.focus_force()

def update_page(fname,lname) :
    global upatepage,left,right,findoption,searchbox
    loginframe.destroy()
    root.title("Welcome to DIY Application")
    print(result[1],result[2])
    #name = result[1]+" "+result[2]
    name = fname+" "+lname
    upatepage = Frame(root,bg='#709fb0')
    upatepage.option_add("*font","Garamond 20")
    upatepage.rowconfigure((0,1,2,3,4,5,6),weight=1)
    upatepage.columnconfigure((0,1,2),weight=1)

    left = Frame(upatepage,bg='#8fd9a8')
    left.columnconfigure((0,1,2,3),weight=1)
    left.grid(row=0,column=0,sticky='news',rowspan=7)
    right = Frame(upatepage,bg='#d2e69c')
    right.columnconfigure((0,1),weight=1)
    right.grid(row=0,column=1,columnspan=2,sticky='news',rowspan=7)

    heading = Label(right,text="Name : "+name,bg="#d2e69c",fg='blue')
    heading.grid(row=0,column=0,columnspan=2,pady=20)

    findoption = StringVar()
    findoption.set("User Name")
    option = OptionMenu(left,findoption,"User Name","First Name","Last Name")
    option.grid(row=0,column=0,pady=20,sticky='e')

    searchbox = Entry(left,width=25)
    searchbox.grid(row=0,column=1,columnspan=2,pady=20,sticky='e')

    search_button = Button(left,image=img2,command=clickoptionaction)
    search_button.grid(row=0,column=3,pady=20)

    upatepage.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def clickoptionaction() :
    #color hex code bg='#d2e69c' for userbox, pwdbox, fnamebox, lnamebox
    #Entry box for display a selected record
    global search_result, userbox,pwdbox,fnamebox,lnamebox,radiospy
    optiondata = findoption.get()
    if optiondata == "User Name":
        sql = "SELECT * FROM students WHERE username=?"
    elif optiondata == "First Name":
        sql = "SELECT * FROM students WHERE fname=?"
    elif optiondata == "Last Name":
        sql = "SELECT * FROM students WHERE lname=?"

    cursor.execute(sql, [searchbox.get()])
    search_result = cursor.fetchall() #ผลของการfetมา
    if search_result :
        leftnew = Frame(upatepage,bg='#8fd9a8')
        leftnew.columnconfigure((0,1,2,3),weight=1)
        for i,data in enumerate(search_result) : #เอามาใส่เพื่อให้เปลี่ยนเป็นข้อมูลdata
            fullname = data[1]+ " " + data[2]#
            Radiobutton(leftnew,text="",value=i,variable=radiospy,command=clickradio,bg='#8fd9a8').grid(row=i+1,column=0,sticky='e')#คือการ+rowไปเรื่อยๆ
            Label(leftnew,text=fullname).grid(row=i+1,column=1,sticky='w')
        leftnew.grid(row=1,column=0,rowspan=7,sticky='news')
    else :
        messagebox.showwarning("Admin","Data not found.")
        leftnew = Frame(upatepage,bg='#8fd9a8')
        leftnew.grid(row=1,column=0,rowspan=7,stick='news')

    
    #color hex code bg='#d2e69c' for userbox, pwdbox, fnamebox, lnamebox
    Label(right,text="Username : ",bg='#d2e69c').grid(row=1,column=0,stick='e')
    userbox = Entry(right,width=20)
    userbox.grid(row=1,column=1,sticky='w',pady=10)
    Label(right,text="Password : ",bg='#d2e69c').grid(row=2,column=0,stick='e')
    pwdbox = Entry(right,width=20)
    pwdbox.grid(row=2,column=1,sticky='w',pady=10) 
    Label(right,text="First name : ",bg='#d2e69c').grid(row=3,column=0,stick='e')
    fnamebox = Entry(right,width=20)
    fnamebox.grid(row=3,column=1,sticky='w',pady=10) 
    Label(right,text="Last name : ",bg='#d2e69c').grid(row=4,column=0,stick='e')
    lnamebox = Entry(right,width=20)
    lnamebox.grid(row=4,column=1,sticky='w',pady=10) 

                            
def clickradio() : #คลิ๊กเพื่อขึ้นข้อมูลที่เราclick
    #use delete method clear old data all of entry box userbox,pwdbox,fnamebox,lnamebox
    row = radiospy.get()
    userbox.delete(0,END)
    pwdbox.delete(0,END)
    fnamebox.delete(0,END)
    lnamebox.delete(0,END)
    

    #use insert method to display data into entry box insert(0,data_for_display)
    userbox.insert(0,search_result[row][3])
    pwdbox.insert(0,search_result[row][4])
    fnamebox.insert(0,search_result[row][1])
    lnamebox.insert(0,search_result[row][2])


    update_button = Button(right,text="Update Now",command=updateclick)
    update_button.grid(row=5,column=1,ipadx=5,ipady=5,pady=20)
    login_button = Button(right,text="Back to Login",command=loginlayout)
    login_button.grid(row=5,column=0,ipadx=5,ipady=5,pady=20)

def updateclick() :
    rownumber = radiospy.get()       #get row/record number
    updateuser = search_result[rownumber][3]   #get a username of index position [3]
    print("Old user -> ",updateuser)
    sql = ''' UPDATE students 
            SET username=? ,
            password=? ,
            fname=? ,
            lname=?
            WHERE username=? ;
    '''
    param = [userbox.get(),pwdbox.get(),fnamebox.get(),lnamebox.get(),updateuser]
    #execute sql query command
    cursor.execute(sql,param) 
    conn.commit()
    messagebox.showinfo("Admin:","Update Successfully")
    #clear old data
    leftnew = Frame(upatepage,bg='#8fd9a8')
    leftnew.grid(row=1,column=0,sticky='news',rowspan=7)
    #reset all entry box at the right side 
    userbox.delete(0,END)
    pwdbox.delete(0,END)
    fnamebox.delete(0,END)
    lnamebox.delete(0,END)
def regiswindow() : #activity of week11
    global fullname,lastname,newuser,newpwd,cfpwd,regisframe
    #destroy()
    root.title("Welcome to User Registration : ")
    root.config(bg='#d2e69c')
    regisframe = Frame(root,bg='#8fd9a8')
    regisframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    Label(regisframe,text="Registration Form",font="Garamond 26 bold",fg='#e4fbff',image=img1,compound=LEFT,bg='#28b5b5').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(regisframe,text='Full name : ',bg='#8fd9a8',fg='#f6f5f5').grid(row=1,column=0,sticky='e',padx=10)
    fullname = Entry(regisframe,width=20,bg='#d3e0ea')
    fullname.grid(row=1,column=1,sticky='w',padx=10)
    Label(regisframe,text='Last name : ',bg='#8fd9a8',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    lastname = Entry(regisframe,width=20,bg='#d3e0ea')
    lastname.grid(row=2,column=1,sticky='w',padx=10)
    Label(regisframe,text="Username : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    newuser = Entry(regisframe,width=20,bg='#d3e0ea')
    newuser.grid(row=3,column=1,sticky='w',padx=10)
    Label(regisframe,text="Password : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    newpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    newpwd.grid(row=4,column=1,sticky='w',padx=10)
    Label(regisframe,text="Confirm Password : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=5,column=0,sticky='e',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    cfpwd.grid(row=5,column=1,sticky='w',padx=10)
    regisaction = Button(regisframe,text="Register Submit",command=registration)
    regisaction.grid(row=6,column=0,ipady=5,ipadx=5,pady=5,sticky='e')
    fullname.focus_force()
    loginbtn = Button(regisframe,text="Back to Login",command=loginlayout)
    loginbtn.grid(row=6,column=1,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')


def registration() :    #activity of week11 
    print("Hello from registration")
    if fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter firstname")
        fullname.focus_force()
    elif lastname.get() == "" :
        messagebox.showwarning("Admin: ","Pleasse enter lastname")
        lastname.focus_force()
    elif newuser.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a new username")
        newuser.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a password")
        newpwd.focus_force()
    elif cfpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a confirm password")
        cfpwd.focus_force()
    else :
        sql = "SELECT * FROM students WHERE username=?"
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("Admin:","The username is already exists")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
            if newpwd.get() == cfpwd.get() : #a new pwd / confirm is correct 
                sql = "INSERT INTO students VALUES (?,?,?,?)"
                param = [newuser.get(),newpwd.get(),fullname.get(),lastname.get()]
                cursor.execute(sql,param)
                conn.commit()
                #retrivedata()
                messagebox.showinfo("Admin:","Registration Successfully")
                newuser.delete(0,END)
                newpwd.delete(0,END)
                cfpwd.delete(0,END)
                fullname.delete(0,END)
                lastname.delete(0,END)
            else :
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpwd.selection_range(0,END)
                cfpwd.focus_force()

conn,cursor = createconnection()
root = mainwindow()
regisframe = Frame(root)
radiospy = IntVar()

img1 = PhotoImage(file='images/profile.png').subsample(5,5)
img2 = PhotoImage(file='images/search.png').subsample(5,5)

loginlayout()

root.mainloop()
cursor.close()
conn.close()
