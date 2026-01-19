
def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(" please enter a valid number")

def calculator(a , b , operations):
    if operations == '+':
        return a + b
    elif operations == '-':
        return a - b
    elif operations == "*":
        return a * b
    elif operations == "/":
        if b == 0:
            return "❌ Error: Cannot divide by zero"
        return a / b
    else:
        return "❌ Invalid operation"
    
while True:
    print("\n ---- simple calculator----")

    num1 = get_number("enter first number : ")
    num2 = get_number("enter seconnd number")
    ops = input("choose operation + - / * :")

    result = calculator(num1 , num2 , ops)
    print("result : " , result)
    
    
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != "y":
        print("Calculator closed 👋")
        break