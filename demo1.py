import tkinter as tk
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("380x520")
        self.root.resizable(False, False)

        self.expression = ""
        self.memory = 0

        self.entry = tk.Entry(
            root, font=("Arial", 20),
            borderwidth=5, relief="ridge",
            justify="right"
        )
        self.entry.pack(fill="both", padx=10, pady=10)

        self.create_buttons()
        self.bind_keys()

    def update_entry(self, value):
        self.expression += str(value)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
            self.expression = str(result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            self.expression = ""

    def scientific(self, func):
        try:
            value = float(self.entry.get())
            if func == "sqrt":
                result = math.sqrt(value)
            elif func == "sin":
                result = math.sin(math.radians(value))
            elif func == "cos":
                result = math.cos(math.radians(value))
            elif func == "tan":
                result = math.tan(math.radians(value))

            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
            self.expression = str(result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            self.expression = ""

    def memory_add(self):
        try:
            self.memory += float(self.entry.get())
        except:
            pass

    def memory_recall(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.memory)
        self.expression = str(self.memory)

    def memory_clear(self):
        self.memory = 0

    def bind_keys(self):
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<BackSpace>", lambda e: self.backspace())

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
            ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
            ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
            ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
        ]

        for (text, r, c) in buttons:
            if text == "=":
                cmd = self.calculate
            else:
                cmd = lambda t=text: self.update_entry(t)

            tk.Button(
                frame, text=text,
                width=6, height=2,
                font=("Arial", 14),
                command=cmd
            ).grid(row=r, column=c, padx=5, pady=5)

        # Extra buttons
        tk.Button(frame, text="C", width=6, height=2,
                  font=("Arial",14), command=self.clear).grid(row=5,column=0)
        tk.Button(frame, text="⌫", width=6, height=2,
                  font=("Arial",14), command=self.backspace).grid(row=5,column=1)
        tk.Button(frame, text="√", width=6, height=2,
                  font=("Arial",14), command=lambda:self.scientific("sqrt")).grid(row=5,column=2)
        tk.Button(frame, text="x²", width=6, height=2,
                  font=("Arial",14), command=lambda:self.update_entry("**2")).grid(row=5,column=3)

        # Scientific
        tk.Button(frame, text="sin", width=6, height=2,
                  font=("Arial",14), command=lambda:self.scientific("sin")).grid(row=6,column=0)
        tk.Button(frame, text="cos", width=6, height=2,
                  font=("Arial",14), command=lambda:self.scientific("cos")).grid(row=6,column=1)
        tk.Button(frame, text="tan", width=6, height=2,
                  font=("Arial",14), command=lambda:self.scientific("tan")).grid(row=6,column=2)

        # Memory
        tk.Button(frame, text="M+", width=6, height=2,
                  font=("Arial",14), command=self.memory_add).grid(row=7,column=0)
        tk.Button(frame, text="MR", width=6, height=2,
                  font=("Arial",14), command=self.memory_recall).grid(row=7,column=1)
        tk.Button(frame, text="MC", width=6, height=2,
                  font=("Arial",14), command=self.memory_clear).grid(row=7,column=2)

# Run app
root = tk.Tk()
AdvancedCalculator(root)
root.mainloop()