1
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    
    
    contacts[name] = {
        'Phone': phone,
        'Email': email
    }
    
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    else:
        print("\nNo contacts available.")

def manage_contacts():
    while True:
        print("\nContact Manager")
        print("1. Add new contact")
        print("2. View contacts")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


manage_contacts()