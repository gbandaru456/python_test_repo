import os
import json
CONTACTS_FILE = "C:/Users/gbandaru/python_new_project/contacts.json"
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE,'r') as file:
            return json.load(file)
        return {}
def add_contacts(contacts):
    name = input('Please enter your name: ')
    phone_number =input('Please enter your mobile number: ')
    contacts[name]=phone_number
    print(f'contact added successfully of {name}.')

def view_contact(contacts):
    if not contacts:
        print('contacts found')
    else:
        for name,phone_number in contacts.items():
            print(f'contact details are : {name}:{phone_number}')  

def search_contact(contacts):
    name = input('Enter your name : ')
    if name in contacts:
            print(f'your conttact details are {name}:{contacts[name]}')
    else:
            print('Sorry...... We did not find contact details')

def delete_contact(contacts):
        name = input('Enter your name to delete : ')
        if name in contacts:
             del contacts[name]
             print(f'Deleted contact for {name}.')
        else:
             print(f'Deleted contact not found for {name}.')  

def save_contacts(contacts):
    with open(CONTACTS_FILE,'w') as file:
         json.dump(contacts,file) 

def main():
    contacts=load_contacts()


    while True:
        print('\n📒 Contact Book')
        print('1. Add contact')
        print('2. View contact')
        print('3. Search contact')
        print('4. Delete cotact')
        print('5. Exit')
        choice = input("Choose your options (1 to 5) : ")
        if choice=='1':
            add_contacts(contacts)
        elif choice=='2':
            view_contact(contacts)
        elif choice=='3':
            search_contact(contacts)
        elif choice=='4':
            delete_contact(contacts)
        elif choice=='5':
            save_contacts(contacts)
            print('Contact saved. Good bye!')
            break
        else:
            print('You choose invalid option.Please try again later')
if __name__=='__main__':
    main()
        

