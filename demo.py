import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

# Run the application
root.mainloop()