#TASK5
'''
Contact Information: Store name, phone number, email, and address for each contact
'''
l1 = []

#Function to add details to the contact
def add(name,number,email,address):
    l1.append((name,number,email,address))
    print("Added contact.")

#Function to view the name and the phone of the contact
def view():
    if len(l1) == 0:
        print("No contacts ")
    
    else:
        for i in range(len(l1)):
            print("Name ",l1[i][0],"Phone ",l1[i][1])

#Function to search for a contact using the name or the phone
def search():
    choice = int(input("Do you want to search using 1)Name or 2)Phonenumber "))
    if choice == 1:
        name = input("Enter the name to search ")
        for i in range(len(l1)):
            if l1[i][0] == name:
                print("Contact found in position ",i+1)
                print("Name ",l1[i][0])
                print("Number ",l1[i][1])
                print("Email ",l1[i][2])
                print("Address ",l1[i][3])
                break
        else:
            print("Contact not found.")
        
    elif choice == 2:
        number = int(input("Enter the number to search "))
        for i in range(len(l1)):
            if l1[i][1] == number:
                print("Contact found in position ",i+1)
                print("Name ",l1[i][0])
                print("Number ",l1[i][1])
                print("Email ",l1[i][2])
                print("Address ",l1[i][3])
                break
        else:
            print("Contact not found. ")
    
    else:
        print("Invalid ")

#Function to update the contact details
def update():
    global l1
    if len(l1) == 0:
        print("The contact is empty ")
    else:
        print("The contacts ")
        for i in range(len(l1)):
            print(i+1,l1[i])
        choice = int(input("Enter the contact to update "))

        if choice > len(l1):
            print("The contact do not exist. ")
        
        else:
            name = input("Enter the new name ")
            number = int(input("Enter the new number "))
            email = input("Enter the new email address ")
            address = input("Enter the new address ")
            t1 = (name,number,email,address)

            l1[choice - 1] = t1

            print("Updated ")

#Function to delete the contact 
def delete():
    global l1
    if len(l1) == 0:
        print("The contact is empty ")
    else:
        print("The contacts ")
        for i in range(len(l1)):
            print(i+1,l1[i])
        choice = int(input("Enter the contact to delete "))

        if choice > len(l1):
            print("The contact do not exist. ")
        
        else:
            l1.pop(choice - 1)
            print("Delete the contact ")


print("Contact Book")
while(True):
    print('''\n
    1.Add Contact
    2.View Contact List
    3.Search Contact
    4.Update Contact
    5.Delete Contact
    6.Exit
    ''')
    choice = int(input("Enter the choice "))
    if choice == 1:
        name = input("Enter the name of the contact ")
        number = int(input("Enter the number "))
        email = input("Enter the email ")
        address = input("Enter the address ")
        add(name,number,email,address)

    elif choice == 2:
        view()

    elif choice == 3:
        search()

    elif choice == 4:
        update()
    
    elif choice == 5:
        delete()
    
    elif choice == 6:
        break

    else:
        print("Invalid ")



        

