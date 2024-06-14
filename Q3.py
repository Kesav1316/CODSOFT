#TASK3
'''
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
'''

import random

l1 = [chr(i) for i in range(33,127)]

#Function to generate the random password
def generate(length):
    global l1
    password = ""
    for i in range(length):
        rand = random.randrange(len(l1))
        password = password + l1[rand]
    print("The random password is ",password)

print("PASSWORD GENERATOR")
while(True):
    print('''
1.Generate Password
2.Exit
''')
    choice = int(input("Enter the option "))
    if choice == 1:
        length = int(input("Enter the length of the password to generate "))
        if(length <=0):
            print("The length must be a positive number ")
        
        elif length > 0:  
            generate(length)
        
        else:
            print("Invalid. ")
    
    elif choice == 2:
        print("Program ended.")
        break

    else:
        print("Invalid. ")
