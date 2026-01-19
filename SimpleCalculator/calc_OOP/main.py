# OOP calculator


class calculator:
    def add(self , a , b):
        return a + b
    def substract(self , a , b):
        return a - b
    def multiply(self , a , b):
        return a * b
    def divide(self , a , b):
        
        if b == 0:
            return "cannot divide by 0"
        return a / b
    
def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(" please enter a valid number")
            


calc = calculator()





while True:
    num1 = get_number("enter first number : ")
    num2 = get_number("enter seconnd number")
    ops = input("choose operation + - / * :")
    
    if ops == "+":
        print(calc.add(num1 , num2))
    elif ops == "-":
        print(calc.substract(num1 , num2))
    elif ops == "*":
        print(calc.multiply(num1, num2))
    elif ops == "/":
        print(calc.divide(num1, num2))
    else:
        print("Invalid operation")

    if input("Continue? (y/n): ").lower() != "y":
        break