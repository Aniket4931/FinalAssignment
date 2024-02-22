"""
Assignment 3: Contact Book
Develop a Python program to manage a contact book.
Allow users to add new contacts, search for contacts by name, and delete contacts.
Use a dictionary to store contacts where the keys are contact names and the values are dictionaries containing contact information like phone number, email, etc.
Implement error handling for cases where a contact is not found during search or deletion.

"""
def add(di):
    name=input("Enter Name : ")
    phone=int(input("Enter Number : "))
    email=input("Enter Email : ")
    di[name]={"Phone":phone,"Email":email}
    print(di)

def search(di):
    name=input("Enter Name : ")
    if name in di:
        print("Name : ",name)
        print("Phone No : ",di[name]['Phone'])
        print("Email : ",di[name]['Email'])
  
def dele(di):
    name=input("Enter Name : ")
    if name in di:
        del di[name]
        print("Delete Successful")    



def main():
    di={}
    while True:
        print("\n1.add new contact")
        print("2.Search Contact")
        print("3.Delete Contact")

        choice=int(input("Enter number : "))
        
        if(1==choice):
            add(di)
        elif(2==choice):
            search(di)
        elif(3==choice):
            dele(di)

            

if __name__ == "__main__":
    main()
