# saves calculations permanently

from datetime import datetime

def save_history(text):
    with open("history.txt" , "a") as file:
        file.write(text + "\n")

        

while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Operation (+ - * /): ")

    if op == "/" and b == 0:
        result = "Error: Divide by zero"
    elif op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        result = "Invalid operation"

    record = f"{datetime.now()} | {a} {op} {b} ={result}"
    print(record)
    save_history(record)

    if input("Continue? (y/n): ").lower() != "y":
        break
