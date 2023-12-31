import hashlib 
from tkinter import *
from firebase import firebase
from tkinter import messagebox

registration_window = Tk()
registration_window.geometry("400x400")

firebase = firebase.FirebaseApplication("https://spyder-project-cp-188-189-default-rtdb.firebaseio.com/",None)
login_username = ""
login_password = ""


def login(): 
    print("login function")
    global login_username
    global login_password
    username = login_username.get()
    password = login_password.get()
    encrypted_pass = hashlib.md5(password.encode())
    hex_pass = encrypted_pass.hexdigest()
    print(hex_pass)
    get_password = firebase.get('/',username)
    print(get_password)
    if(get_password != None):
        if(get_password == hex_pass ):
            messagebox.showinfo("Success","Successfully Logged In")
        else:
            messagebox.showinfo("Incorrect","Incorrect Password")
            
    else:
        messagebox.showinfo("Error","User is not Registered")
    
    
    
def register(): 
    print("register function")
    
    password = password_entry.get()
    username = username_entry.get()
    passw = hashlib.md5(password.encode())
    pass_hexdigest = passw.hexdigest()
    print(passw.hexdigest())
    final = firebase.put( "/", username, pass_hexdigest)
    messagebox.showinfo("Registered", "User is Registered")
    
def login_window():
    
    global login_username
    global login_password
    
    login_window = Tk()
    login_window.geometry("400x400")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold')
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13')
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username = Entry(login_window)
    login_username.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13')
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password = Entry(login_window)
    login_password.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT)
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold')
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13')
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13')
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT)

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()