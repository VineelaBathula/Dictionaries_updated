import data
import Functions

# Initialize stock for the menu items
menu_items = data.menu_items
Functions.initialize_stock(menu_items)

def interactive_menu():
    while True:
        print("\nChoose an action:")
        print("1. Change price of an item")
        print("2. Change description of an item")
        print("3. Add a new item")
        print("4. Remove an item")
        print("5. Customer Order")
        print("6. Exit")
       
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            item_id = input("Enter the item ID to change price: ").strip().upper()
            if item_id: 
                inside = False
                for item in menu_items:
                    if item_id in item['id']:
                        inside=True
                        new_price = float(input(f"Enter the new price for item ID {item_id}: ").strip())
                        if new_price < 0:
                            print('Price cannot be negative')
                        else:    
                            Functions.update_stock(menu_items, action='change_price', item_id=item_id, new_price=new_price)
                        
                if not inside: 
                    print('Invalid Input')
            else:
                print('Invalid Input')
                
        
        elif choice == '2':
            item_id = input("Enter the item ID to change description: ").strip().upper()
            inside = False
            if item_id:
                
                for item in menu_items:
                    if item_id in item['id']:
                        inside = True
                        new_name = input(f"Enter the new name for item ID {item_id}: ").strip().upper()
                        if new_name:
                            if new_name == item['name'] :
                                print('Item name exists. Provide another name') 
                            else:
                                Functions.update_stock(menu_items, action='change_description', item_id=item_id, new_name=new_name)
                        else:
                            print('Invalid Input')
            if not inside:
                print('Invalid Input')

        
        

        elif choice == '3':
            new_id = input("Enter new item ID: ").strip().upper()
            id_exists = any(item['id'] == new_id for item in menu_items) # Check if the new ID already exists
            if id_exists:
                print("Item ID already exists. Please enter a different ID.")
            else:
                valid_name = False
                while not valid_name:
                    new_name = input("Enter new item name: ").strip().upper()
                    if new_name.replace(' ', '').isalpha():# Check if new_name only contains letters and spaces
                        valid_name = True
                    else:
                         print("Invalid name. The item name should only contain letters. Please enter a valid name.")

                valid_price = False
                while not valid_price:
                    new_price_input = input("Enter new item price: ").strip()
                   
                    if new_price_input.replace('.', '', 1).isdigit(): #Check if the input is a digit or a valid float
                        new_price = float(new_price_input)
                        if new_price < 0:
                            print("Price cannot be negative. Please enter a valid price.")
                        else:
                            valid_price = True  # Exit the loop if price is valid
                    else:
                        print("Invalid price. Please enter a valid number.")
                Functions.update_stock(menu_items, action='add_item', item_id=new_id, new_name=new_name, new_price=new_price)
            
        elif choice == '4':
            item_id = input("Enter the item ID to remove: ").strip().upper()
            Functions.update_stock(menu_items, action='remove_item', item_id=item_id)


        elif choice == '5':
            print('Customer order')
            Functions.take_customer_order()
        
       
        elif choice == '6':
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the interactive menu
print('                                      ')
print("Welcome to the Order Management system!")

interactive_menu()
