'''
Assignment instructions

Create an inventory tracking system that has all of the following features:

Each item will have a name, quantity, and description as a dictionary.
All dictionaries will be saved in a master inventory list.
A function that adds something to that list (creates the dictionary and adds to the list).
A function that displays the inventory in a readable format (i.e. do not just print out the list or dictionary, separate them out).
A function that will change the quantity of an item (this is difficult to do and many ways to do it).
A function that removes an item from the list. Research required :)

Questions for this assignment
Q:What was the most challenging part about this.
A: 
First challenge: Writing the function for updating the quantity required some trial and error. I eventually got the 
if statement nested in the for loop correctly. 
Second challenge: I wrote this code without input functionality first to get the fuctions working properly. 
Adding this took some research. I added a while loop on line 68 to proplt the user to mke a selection of what they 
wanted to do in the inventory system.
Note: I would like to add functionality to this program by writting the inventory to a database so that the invenotry persists 
once the program ends, however that is outside the scope of this project and I will continue on with the course. 
'''
inventory_main = []

def display():
    #Displays all items in the inventory
    print('Current Inventory')
    for item in inventory_main:
        print(f'Name: {item['name']}, Quantity: {item['quantity']}, Description: {item['description']}')

def add():
    #adds new item to the inventory
    name = input('Enter item name: ')
    try:
        quantity = int(input('Enter item quantity(must be a number): '))
    except ValueError:
        print('Quanitity must be an integer')
        return
    description = input('Enter item description: ')
    item = {'name': name, 'quantity': quantity, 'description': description}
    inventory_main.append(item)

def update():
    #Updates the quantity of an item in the inventory
    for item in inventory_main:
        name = input('Enter the item name to update: ')
        try:
            quantity = int(input('Enter updated item quantity: '))
        except ValueError:
            print('Quanitity must be an integer')
            return
        if item['name'] == name:
            item['quantity'] = quantity
            print(f"Updated {name}'s quantity to {quantity}")
            return
        else:
            print(f"Item '{name}' not found.")

def remove():
    #Removes an item from the inventory
    name = input('Enter the item you want to remove from the inventory. (Warning! This action is permanent): ')
    global inventory_main
    item_exists = any(item for item in inventory_main if item['name'] == name)
    if item_exists:
        inventory_main = [item for item in inventory_main if item['name'] != name]
        print(f"Removed '{name}' from inventory")
        return
    else:
        print(f"Item '{name}' not found.")

# Prompt the user to decide if they wish to manage the inventory system
manage = input('Would you like to manage the inventory? y/n ')

# Check if the user input is not one of the accepted responses ('y', 'n', in both uppercase and lowercase)
if manage not in ('y', 'n', 'Y', 'N'):
    # Inform the user that the input was invalid and prompt for a correct response ('y' or 'n')
    print('Please enter y or n')

# If the user expresses interest in managing the inventory by responding with 'y' or 'Y'
elif manage in ('y', 'Y'):
    # Enter a loop to continuously provide the inventory management options
    while True: 
        try:
            # Prompt the user to select an action from the inventory management menu
            select = int(input("What would you like to do? \n 1: Display inventory \n 2: Add to the inventory \n 3: Update an inventory item \n 4: Remove an inventory item \n 5: Exit \n Selection>> "))
            
            # Display the current inventory
            if select == 1:
                display()  # Invoke the function to display inventory items
                continue  # Return to the start of the loop for further actions

            # Add a new item to the inventory
            elif select == 2:
                add()  # Invoke the function to add a new inventory item
                continue  # Return to the start of the loop for further actions

            # Update the details of an existing inventory item
            elif select == 3:
                update()  # Invoke the function to update an inventory item
                continue  # Return to the start of the loop for further actions

            # Remove an item from the inventory
            elif select == 4:
                remove()  # Invoke the function to remove an inventory item
                continue  # Return to the start of the loop for further actions

            # Exit the inventory management system
            elif select == 5:
                print('Exiting inventory management system') 
                exit()  # Terminate the program upon user request

            # Handle invalid selection (not within 1-5)
            else:
                print('Please use a number between 1 and 5 to make your selection')
                continue  # Return to the start of the loop for a valid selection

        # Catch and handle exceptions for non-integer inputs
        except ValueError:
            print('Please use a number between 1 and 5 to make your selection')
            continue  # Return to the start of the loop for a valid selection

# If the user chooses not to manage the inventory by responding with 'n' or 'N'
elif manage == 'n' or 'N':
    print('Exiting inventory management system')  # Inform the user that the system is exiting
    # Note: The code to actually exit the program (e.g., exit() or break) is missing here

