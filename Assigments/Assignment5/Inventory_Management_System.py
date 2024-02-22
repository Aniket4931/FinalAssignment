"""
Assignment 5: Inventory Management System
Design a Python program to manage an inventory system for a small store.
The inventory should consist of items with attributes like name, quantity, price, and category.
Implement functionality to add new items, update existing items, remove items, and display the inventory.
Allow users to search for items by name or category and display details of the matching items.
Include features for checking the availability of items, adding items to a shopping cart, and generating a bill.
Ensure the program handles errors gracefully, such as attempting to remove a non-existent item or adding a negative quantity.
Implement a simple text-based user interface with a menu system for navigating different functionalities.

"""
def Add_Item(Leo):
    try:
        name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        print("1. Plastic, 2. Grocery, 3. Milk")
        category = int(input("Enter Product No: "))
        if category not in [1, 2, 3]:
            raise ValueError("Invalid category number.")
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price cannot be negative.")
        if category == 1:
            store = "Plastic"
        elif category == 2:
            store = "Grocery"
        elif category == 3:
            store = "Milk"
        Product = (name, quantity, price, store)
        Leo.append(Product)
        print("Item added successfully.")
    except ValueError :
        print("Error:", ValueError)


def Update_Item(Leo):
    try:
        display_Item(Leo)
        update=int(input("Enter Number What is Delete Item :"))-1
        print("Update 1.Name 2.quntity 3.category")
        Index=int(input("Enter Update Number :"))
        if Index==1:
            name=input("Enter Update Name : ")
            Leo[update] = (name, Leo[update][1], Leo[update][2], Leo[update][3])
        elif Index == 2:
            quantity = int(input("Enter Updated Quantity: "))
            Leo[update] = (Leo[update][0], quantity, Leo[update][2], Leo[update][3])
        elif Index == 3:
            price = float(input("Enter Updated Price: "))
            Leo[update] = (Leo[update][0], Leo[update][1], price, Leo[update][3])
        elif Index == 4:
            print("1. Plastic, 2. Grocery, 3. Milk")
            category = int(input("Enter Updated Category: "))
            if category == 1:
                store = "Plastic"
            elif category == 2:
                store = "Grocery"
            elif category == 3:
                store = "Milk"
            Leo[update] = (Leo[update][0], Leo[update][1], Leo[update][2], store)
    except ValueError :
            print("Error:", ValueError)


    


def Remove_Item(Leo):
    display_Item(Leo)
    remove=int(input("Enter Number What is Delete Item :"))-1
    del Leo[remove]
    print("successful delete")


def display_Item(Leo):
    for num,Item in enumerate(Leo):
        print(num + 1,":",Item[0],"(quantity",Item[1], ", price: ",Item[2],",category :",Item[3],")" )

def Search_Item(Leo):
    display_Item(Leo)
    search = input("Enter the product name to search: ")
    for num, Item in enumerate(Leo):
        if search in Item[0]:
            print(num + 1,":", Item[0],"( quantity:", Item[1],", price:", Item[2],", category: ", Item[3])

def Add_cart(Leo,cart):
    display_Item(Leo)
    try:
        product_name = input("Enter the product Name : ")
        Quntity=int(input("Enter quntity :"))
    except ValueError:
        print("Error",ValueError)
    for num, Item in enumerate(Leo):
        if product_name in Item[0]:
        
            cartItem=(Item[0],"quantity:", Quntity," price:", Item[2]*Quntity)
            Leo[num] = (Item[0], Item[1] - Quntity, Item[2], Item[3])
            print("cart Item Added")
    cart.append(cartItem)

def show_cart(cart):
    for num, Item in enumerate(cart):
        print("Product Name :",Item[0],Item[1],Item[2],Item[3],Item[4])

def Bill(cart):
    name=input("Enter Your Name : ")
    print("---------- Leo Store ----------")
    print("Name :",name)
    total=0
    for num, Item in enumerate(cart):
        print("Product Name:",Item[0],Item[1],Item[2],Item[3],Item[4]) 
        total += Item[4]  
    print("Total : ",total)
    print("---------- Thank You ----------")




def main():
    Leo=[]
    cart=[]
    while True:
        print("\nUser Enter 1")
        print("Admin Enter 2\n")
        try:
            User = int(input("Enter Number : "))
        except ValueError:
            print("Please enter a valid integer.")
            continue  
        if User==1:
             print("\nWelcome Leo Store")
             print("1.Show Item ")
             print("2.Search Item ")
             print("3.buy product ")
             print("4.Cart Show ")
             print("5.Bill\n")
             try:                 
                User_input=int(input("choose uper list Enter number  :"))
             except ValueError:
                 print("Enter Number (Integer)")
             if User_input==1:
                 display_Item(Leo)
             elif User_input==2:
                 Search_Item(Leo)
             elif User_input==3:
                 Add_cart(Leo,cart)
             elif User_input==4:
                 show_cart(cart)
             elif User_input==5:
                 Bill(cart)
            
                 

        elif User==2:
            print("\nHello Admin")
            print("Add Item Enter 1 ")
            print("Remove Item Enter 2 ")
            print("Update Item Enter 3 \n")
            try:
                admin = int(input("Enter Number : "))
            except ValueError:
                print("Please enter a valid integer for the option.")
                continue  
            if admin==1:                
                Add_Item(Leo)
            elif admin==2:
                Remove_Item(Leo)
            elif admin==3:
                Update_Item(Leo)
            print(Leo)

if __name__ == "__main__":
    main()

    
