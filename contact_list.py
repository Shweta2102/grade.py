import json


def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts_data = json.load(file)
    except FileNotFoundError:
        contacts_data = {}
    return contacts_data


def search_contacts(contacts_data, name):
    matching_contacts = []
    for contact in contacts_data:
        if name.lower() in contact['name'].lower():
            matching_contacts.append(contact)
    return matching_contacts


def main():
    filename = "contacts.json"
    contacts_data = load_contacts(C:\Users\shwet\OneDrive\Desktop)

    while True:
        search_name = input("Enter name to search for (or type 'quit' to exit): ")
        if search_name.lower() == 'quit':
            break
        
        matching_contacts = search_contacts(contacts_data, search_name)
        
        if matching_contacts:
            print("Matching contacts:")
            for contact in matching_contacts:
                print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")
        else:
            print("No contacts found matching the search name.")

if __name__ == "__main__":
    main()
