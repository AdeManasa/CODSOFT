def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    search = input("Enter name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details['phone']:
            print(f"\nFound Contact - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave the field empty to keep the current value.")
        new_phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        new_email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
        new_address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()

        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email
        if new_address:
            contacts[name]['address'] = new_address
        
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
        
