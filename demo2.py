import tkinter as tk
from tkinter import messagebox

# Login function
def login():
    username = entry_user.get()
    password = entry_pass.get()

    # Dummy credentials
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome, Login Successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("350x250")
root.resizable(False, False)

# Heading
tk.Label(root, text="Login", font=("Arial", 20, "bold")).pack(pady=10)

# Username
tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root, width=30)
entry_user.pack(pady=5)

# Password
tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, width=30, show="*")
entry_pass.pack(pady=5)

# Login Button
tk.Button(root, text="Login", width=15, command=login).pack(pady=20)

# Run app
root.mainloop()