contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_id = str(len(contacts) + 1)  # Generate ID (you might use UUID for production)
    contacts[contact_id] = {'name': name, 'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added successfully with ID: {contact_id}")

def view_contact_list():
    print("----- Contact List -----")
    for contact_id, contact in contacts.items():
        print(f"{contact_id}: {contact['name']} - {contact['phone']}")

def search_contact():
    term = input("Enter name or phone number to search: ")
    found = False
    for contact_id, contact in contacts.items():
        if term in contact['name'] or term in contact['phone']:
            print(f"{contact_id}: {contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("No matching contacts found.")

def update_contact():
    contact_id = input("Enter contact ID to update: ")
    if contact_id in contacts:
        print(f"Current Details: {contacts[contact_id]}")
        contacts[contact_id]['name'] = input("Enter new name: ")
        contacts[contact_id]['phone'] = input("Enter new phone number: ")
        contacts[contact_id]['email'] = input("Enter new email: ")
        contacts[contact_id]['address'] = input("Enter new address: ")
        print(f"Contact ID {contact_id} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    contact_id = input("Enter contact ID to delete: ")
    if contact_id in contacts:
        del contacts[contact_id]
        print(f"Contact ID {contact_id} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n---- Contact Management System ----")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
