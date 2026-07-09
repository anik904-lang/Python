import tkinter as tk
from tkinter import Button, Label, Entry, messagebox
import ttkbootstrap as ttkb

root = tk.Tk()
root.title("Login")
root.geometry("500x500")
root.resizable(True,True)
def check_login():
    if username.get() == "Anik" and password.get() == "ab17":
        messagebox.showinfo("Login successful","Login successful")
    else:
        messagebox.showerror("Login failed","Login failed")
Label(root,text="Login Form",font=("Arial",20)).pack()
Label(root,text="username").pack(pady=5)
username = Entry(root,width = 20)
username.pack()
Label(root,text="password").pack(pady=5)
password = Entry(root,width = 20)
password.pack()
Button(root,text="Login",command=check_login).pack(pady=10)
root.mainloop()
