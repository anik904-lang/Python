import tkinter as tk
from tkinter import Button,Label,messagebox
import ttkbootstrap as ttkb  

root=tk.Tk()
root.title("Signup")
root.geometry("500x500")
root.resizable(True,True)
def signup():
    messagebox.showinfo("Signup","Signup successful")
Label(root,text="Signup Form",font=("Arial",20)).pack()
Label(root,text="First name",).pack(pady=5)
firstname=ttkb.Entry(root,width=20)
firstname.pack()
Label(root,text="Last name",).pack(pady=5)
lastname=ttkb.Entry(root,width=20)
lastname.pack()
Label(root,text="Email",).pack(pady=5)
email=ttkb.Entry(root,width=20)
email.pack()
Label(root,text="Password",).pack(pady=5)
password=ttkb.Entry(root,width=20,show="*")
password.pack()
Label(root,text="Confirm Password",).pack(pady=5)
confirmpassword=ttkb.Entry(root,width=20,show="*")
confirmpassword.pack()

Button(root,text="Signup",command=signup).pack(pady=10)
root.mainloop()



