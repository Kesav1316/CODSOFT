#TASK2
'''
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result
'''

def addition(x,y):
    print(f"The value of {x} + {y} is {x+y}")

def subtraction(x,y):
    print(f"The value of {x} - {y} is {x-y}")

def multiplication(x,y):
    print(f"The value of {x} * {y} is {x*y}")

def division(x,y):
    try:
        divide = x/y
    
    except ZeroDivisionError:
        print("The denominator should not be 0.")
    
    else:
        print(f"The value of {x} / {y} is {divide}")
        

while(True):
    print("CALCULATOR")
    print('''
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Exit
    ''')

    choice = int(input("Enter the choice "))

    if choice == 1:
        x = float(input(("Enter the first number ")))
        y = float(input(("Enter the second number ")))
        addition(x,y)
    
    elif choice == 2:
        x = float(input(("Enter the first number ")))
        y = float(input(("Enter the second number ")))
        subtraction(x,y)
    
    elif choice == 3:
        x = float(input(("Enter the first number ")))
        y = float(input(("Enter the second number ")))
        multiplication(x,y)

    elif choice == 4:
        x = float(input(("Enter the first number ")))
        y = float(input(("Enter the second number ")))
        division(x,y)
    
    elif choice == 5:
        break

    else:
        print("Invalid.")
        
    
