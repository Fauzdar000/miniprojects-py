import tkinter as tk

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operator.get()

        if op == "+":
            result.set(a + b)
        elif op == "-":
            result.set(a - b)
        elif op == "*":
            result.set(a * b)
        elif op == "/":
            result.set("Error" if b == 0 else a / b)
    except:
        result.set("Invalid Input")


root = tk.Tk()
root.title("Calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

operator = tk.StringVar()
tk.Entry(root, textvariable=operator).pack()

tk.Button(root, text="Calculate", command=calculate).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
