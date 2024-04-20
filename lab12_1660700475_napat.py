from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('schools.db')
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
    userentry.delete(0,END)
    pwdentry.delete(0,END)
def loginclick() :
    global result
    #เช็คusername/password หรือยัง
    if userentry.get() == "" or pwdentry.get() == "":
        messagebox.showwarning("Admin:","Enter Username and Password first")
        userentry.focus_force()
    else:
        #เช็คว่ามีข้อมูลใน Databaseไหม
        sql = "SELECT * FROM students WHERE username=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            #มีuser ในdb แล้วเช็ค
            print(result)
            sql = "SELECT * FROM students WHERE username=? AND password=?"
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
    global mainfrm,midfrm,cdty,cn,day,room
    
    mainfrm.destroy() # destroy old frame
    mainfrm = Frame(root,bg='#DFAB99')
    mainfrm.rowconfigure((0,1,2,3,4,5),weight=1)
    mainfrm.columnconfigure((0,1,2,3,4),weight=1)
    mainfrm.grid(row=0,column=0,columnspan=4, rowspan=4,sticky='news')

    midfrm = Frame(mainfrm,bg='#00BFFF')
    midfrm.rowconfigure((0,1,2),weight=1)
    midfrm.columnconfigure((0,1),weight=1)
    midfrm.grid(row=2)

    lastfrms = Frame(mainfrm,bg='#3AD1FF')
    lastfrms.rowconfigure((0,1,2,3,4),weight=1)
    lastfrms.columnconfigure((0,1,2,3,4),weight=1)
    lastfrms.grid(row=3)

    lass = Frame(mainfrm,bg='#DFAB99')
    lass.rowconfigure((0,1,2,3,4),weight=1)
    lass.columnconfigure((0,1,2,3,4),weight=1)
    lass.grid(row=4,column=0,columnspan=4)

    root.title("Welcome " + result[1] + " " + result[2])

    img= Label(mainfrm,image=img1,bg='#DFAB99')
    img.grid(row=0,columnspan=2,sticky='')

    name=Label(mainfrm,text='Name :'+result[1]+' '+result[2],bg='#DFAB99')
    name.grid(row=1,column=0,sticky='w',padx=15)

    id=Label(mainfrm,text='Student ID :'+str(result[0]),bg='#CB7F66')
    id.grid(row=1,column=0,sticky='nw',padx=15,pady=20)

    Label(lastfrms,text='Course Code',bg='#3AD1FF').grid(row=0,column=0,sticky='news',padx=5,pady=5)
    cdty=Entry(lastfrms,bg='lightblue',justify=CENTER)
    cdty.grid(row=1,column=0)
    Label(lastfrms,text='Course name',bg='#3AD1FF').grid(row=0,column=1,sticky='news',padx=5,pady=5)
    cn=Entry(lastfrms,bg='lightblue',justify=CENTER)
    cn.grid(row=1,column=1)
    Label(lastfrms,text='Day:',bg='#3AD1FF').grid(row=0,column=2,sticky='news',padx=5,pady=5)
    day=Entry(lastfrms,bg='lightblue',justify=CENTER)
    day.grid(row=1,column=2)
    Label(lastfrms,text='Room:',bg='#3AD1FF').grid(row=0,column=3,sticky='news',padx=5,pady=5)
    room=Entry(lastfrms,bg='lightblue',justify=CENTER)
    room.grid(row=1,column=3)

    Button(mainfrm,text='Add course',command=add_record).place(x=70,y=700)

    Button(mainfrm,text='Update Record',command=update_record).place(x=270,y=700)

    Button(mainfrm,text='Delete Selected',command=remove_one).place(x=530,y=700)

    Button(mainfrm,text='Clear',command=reset_box).place(x=810,y=700)

    Button(mainfrm,text='Log out',command=loginlayout).place(x=421,y=750)

    
    createTreeview()

def createTreeview():
    global mytree, i, mainfrm,data
    # Destroy existing treeframe if it exists

    # Create TreeView Frame
    treeframe = Frame(midfrm)
    treeframe.grid(row=0)

    # Create Scrollbar
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT, fill=Y)
    # Create Treeview with scrollbar(yscrollcommand)
    mytree = ttk.Treeview(treeframe, columns=("id", "Course_Code", "Course_Name", "Day", "Room"))
    mytree.pack()
    # config scrollbar on the treeview
    # create headings
    mytree.heading("#0", text="", anchor=W)
    mytree.heading("id", text="id", anchor=W)
    mytree.heading("Course_Code", text="Course Code", anchor=W)
    mytree.heading("Course_Name", text="Course Name", anchor=W)
    mytree.heading("Day", text="Day", anchor=W)
    mytree.heading("Room", text="Room", anchor=W)
    # Format our columns
    mytree.column("#0", width=0, minwidth=0)  # set minwidth=0 for disable the first default column
    mytree.column("id", anchor=W, width=200)
    mytree.column("Course_Code", anchor=W, width=200)
    mytree.column("Course_Name", anchor=W, width=200)
    mytree.column("Day", anchor=W, width=200)
    mytree.column("Room", anchor=W, width=200)
    # clear treeview data
    mytree.delete(*mytree.get_children())  # delete old data from treeview
    # fetch data
    sql = "SELECT * FROM course  ORDER BY course_name ASC"
    cursor.execute(sql)
    result = cursor.fetchall()

    # Add data into treeview
    for i, data in enumerate(result):
        if i % 2 == 1:
            mytree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4]))
        else:
            mytree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4]))
    mytree.bind("<Double-1>", on_double_click)
def on_double_click(event):
    global mytree
  # Get the selected item
    item_data = mytree.item(mytree.focus(), "values")
    reset_box()
    cdty.insert(0,item_data[1])
    cn.insert(0,item_data[2])
    day.insert(0,item_data[3])
    room.insert(0,item_data[4])
def reset_box():
    cdty.delete(0,END)
    cn.delete(0,END)
    day.delete(0,END)
    room.delete(0,END)
def add_record() :
    global i 
    #new rows number for set tags
    i = i + 1
    if cdty.get() == "" :
        messagebox.showwarning("Admin","Please enter Course_code.")
        cdty.focus_force
    elif cn.get() == "" :
        messagebox.showwarning("Admin","Please enter Course_name.")
        cn.focus_force
    elif day.get() == "" :
        messagebox.showwarning("Admin","Please enter Day.")
        day.focus_force
    elif room.get() == "" :
        messagebox.showwarning("Admin","Please enter Room.")
        room.focus_force
    else :
        mytree.insert('', 'end', values=(data[1], data[2], data[3], data[4]))
        sql = "INSERT INTO course (course_code,course_name,day,room) VALUES (?,?,?,?)"
        param = [cdty.get(),cn.get(),day.get(),room.get()]
        cursor.execute(sql,param)
        conn.commit()
    
        messagebox.showinfo("Admin:","Registration Successfully")
def remove_one() :
    msg = messagebox.askquestion ('Delete this username','Are you sure you want to delete this course',icon = 'warning')
    if msg == 'no':
        reset_box()
    else:
        deleterow = mytree.selection()
        values = mytree.item(mytree.focus(),'values')
        selected_user = values[1] #get selected username
        # delete selected treeview row item
        mytree.delete(deleterow)
        #delete from login table process : delete command 
        sql = """DELETE FROM course
                WHERE course_code=?;
            """
        #execute sql query command
        cursor.execute(sql,[selected_user]) 
        conn.commit()
        messagebox.showinfo("Admin:","Delete Successfully")
        reset_box()
def update_record() :
    if cdty.get() == "" :
        messagebox.showwarning("Admin","Before updating please enter Course_code.")
        cdty.focus_force
    elif cn.get() == "" :
        messagebox.showwarning("Admin","Before updating please enter Course_name.")
        cn.focus_force
    elif day.get() == "" :
        messagebox.showwarning("Admin","Before updating please enter Day.")
        day.focus_force
    elif room.get() == "" :
        messagebox.showwarning("Admin","Before updating please enter Room.")
        room.focus_force
    else :
        selected = mytree.focus() #get focus record
        values = mytree.item(mytree.focus(),'values') #get selected value
        selected_user = values[1] #get selected username
        # change selected treeview row item to new values
        mytree.item(selected, text="",values=(cdty.get(),cn.get(),day.get(),room.get())) 
        #update to the login table process : write update command here
        sql = """UPDATE course
            SET course_code=?,
            course_name =?,
            day =?,
            room =?
            WHERE course_code=?;
        """
        param = [cdty.get(),cn.get(),day.get(),room.get(),selected_user]
        #execute sql query command
        cursor.execute(sql,param) 
        conn.commit()
        messagebox.showinfo("Admin:","Update Successfully")
        #Clear entry boxes
        reset_box()



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