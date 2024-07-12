import json

contacts = {}

def add_contact(name, phone_number, email):
    if name in contacts:
        print(f"Contact with name '{name}' already exists. Use edit option to update.")
    else:
        contacts[name] = {'phone_number': phone_number, 'email': email}
        print(f"Contact '{name}' added successfully!")

def view_contacts():
    if contacts:
        for name in contacts:
            print(f"Name: {name}")
            print(f"Phone Number: {contacts[name]['phone_number']}")
            print(f"Email: {contacts[name]['email']}")
    else:
        print("No contacts found.")


def edit_contact(name, phone_number, email):
    if name in contacts:
        contacts[name]['phone_number'] = phone_number
        contacts[name]['email'] = email
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)
        print("Contacts saved successfully.")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
            print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("No contacts found. Start adding contacts.")



load_contacts()  # Load existing contacts from file if available
while True:
    print("\n===== Contact Manager Menu =====")
    print("1. Add a new contact")
    print("2. View contact list")
    print("3. Edit a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone_number, email)

    elif choice == '2':
            print("===== List of Contacts =====")
            view_contacts()

    elif choice == '3':
            name = input("Enter name to edit: ")
            phone_number = input("Enter new phone number (enter same phone number to keep current): ")
            email = input("Enter new email (enter same email to keep current): ")
            edit_contact(name, phone_number, email)

    elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)

    elif choice == '5':
            print("Exiting program. Goodbye!")
            break
    save_contacts()  # Save contacts before exiting


