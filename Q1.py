#TASK1
'''
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
'''
l1 = []

#Function to create the task
def create(task):
    global l1
    try:
        l1.append(task)
    
    except:
        print("Error while adding task.")
    
    else:
        print("Successfully added the task.")

#Function to update the task
def update():
    global l1
    if len(l1) == 0:
        print("No tasks currently.")
    else:
        print("Current to do list.")
        for i in range(len(l1)):
            print(f"    {i+1}:",l1[i])
        print('''
Choose the option
1.Change the task
2.Remove the task
              ''')
        choice = int(input("\nEnter the option. "))
        if choice == 1:
            task_no = int(input("\nEnter the task number to change "))
            new_task = input("Enter the new task. ")
            try:
                l1[task_no-1] = new_task
            except IndexError:
                print("\nThe task number do not exist. ")
            else:
                print("\nSuccessfuly replaced. ")
                print("\nNew todo list. ")
                for i in range(len(l1)):
                    print(f"    {i+1}:",l1[i])
        
        elif choice == 2:
            task_no = int(input("\nEnter the task number to delete "))
            try:
                l1.pop(task_no - 1)
            
            except IndexError:
                print("\nThe task number do not exist. ")
            
            else:
                print("\nSuccessfuly removed. ")
                print("\nNew todo list. ")
                for i in range(len(l1)):
                    print(f"    {i+1}:",l1[i])
        
        else:
            print("Invalid option. ")

#Function to track the task
def track():
    global l1
    if len(l1) == 0:
        print("You do not have any tasks left in your todo list.")
    
    else:
        print("Current to do list.")
        for i in range(len(l1)):
            print(f"    {i+1}:",l1[i])

print("TODO LIST")
while(True):

    print('''
    1.Create
    2.Update
    3.Track
    4.Exit''')
    choice = int(input("Enter the choice "))

    if choice == 1:
        task = input("Enter the task. ")
        create(task)
    
    elif choice == 2:
        update()
    
    elif choice == 3:
        track()
    
    elif choice == 4:
        print("Program ended.")
        break



