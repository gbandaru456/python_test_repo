import os
import json

CONTACTS_FILE = "C:/Users/gbandaru/python_new_project/contacts.json"
def load_contact():
    with open(CONTACTS_FILE,'r') as file:
        return json.load(file)
    return {}
def save_contacts(contacts):
    with open(CONTACTS_FILE,'w') as file:
        json.dump(contacts,file)

def add_contact(contacts):
    name=input('please entre your name here : ').strip()
    phone=input('please enter your conract number here : ').strip()
    contacts[name]=phone    
    print(f"Contact for {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found")
    else:
        for name,phone in contacts.items():
            print(f'{name}:{phone}')

def serach_contact(contacts):
    name=input('Enter name to search : ').strip()
    if name in contacts:
        print(f'{name}:{contacts[name]}')
    else:
        print("Contact not found.")
    
def delete_contact(contacts):
    name=input('Enter your name to delete: ').strip()
    if name in contacts:
        del contacts[name]
        print(f'Deleted contact for {name}.')
    else:
        print("Contact not found")

def main():
    contacts=load_contact()
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5.Exit")
        choice=input('choose your options (1 to 5) :')
        if choice=='1':
            add_contact(contacts)
        elif choice=='2':
            view_contacts(contacts)
        elif choice=='3':
            serach_contact(contacts)
        elif choice=='4':
            delete_contact(contacts)
        elif choice=='5':
            save_contacts(contacts)
            print("Contacts saved: Good Bye!")
            break
        else:
            print("Invalid choice. please try later")
if __name__=='__main__':
    main()

