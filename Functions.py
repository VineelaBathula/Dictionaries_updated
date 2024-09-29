import data
import random

# Initialize stock for non-drink items
def initialize_stock(menu_items):
    for item in menu_items:
        # Assign stock only to non-drink items (IDs that don't start with 'D')
        if not item['id'].startswith('D'):
            item['stock'] = random.randint(25, 50)
        else:
            item['stock'] = "Unlimited"  # Set drinks' stock to None
    print("Stock initialized for non-drink items.")

    for item in menu_items:
        stock_info = "Unlimited" if item['stock'] is None else item['stock']
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}, Stock: {stock_info}")




# Function to update stock information
def update_stock(menu_items, action, item_id=None, new_price=None, new_name=None):
    if action == 'change_price':
        # Update the price of an existing item
        for item in menu_items:
            if item['id'] == item_id:
                item['price'] = new_price
                print(f"Updated price of {item['name']} to ${item['price']}")
                print(menu_items)
                return
        print("Item not found!")
    
    elif action == 'change_description':
        # Update the description/name of an existing item
        for item in menu_items:
            if item['id'] == item_id:
                item['name'] = new_name
                print(f"Updated name of item ID {item_id} to {item['name']}")
                print(menu_items)
                return
        print("Item not found!")
    
    elif action == 'add_item':
        # Add a new item to the menu
        new_item = {
            'id': item_id,
            'name': new_name,
            'price': new_price,
            'stock': random.randint(25, 50)  # Assign stock to the new item
        }
        menu_items.append(new_item)
        print(f"Added new item: {new_item}")
        print(menu_items)
    
    elif action == 'remove_item':
        # Remove an existing item from the menu
        for item in menu_items:
            if item['id'] == item_id:
                menu_items.remove(item)
                print(f"Removed item with ID {item_id}")
                print(menu_items)
                return
        print("Item not found!")
    
    else:
        print("Invalid action!")

# Function to take a customer order
def take_customer_order():
    item_name = input("Enter the name of the item you want to order: ").strip().upper()

    quantity = int(input(f"Enter the quantity of {item_name} you want to order: ").strip())
    
    # Find the item on the menu
    for item in data.menu_items:
        if item['name'] == item_name:
            # Check if it's a drink or has enough stock
            if item['stock'] is 'Unlimited' :
                print(f"{item_name} is a drink and has unlimited stock. Order placed for {quantity} {item_name}.")
                return
            elif item['stock'] >= quantity:
                item['stock'] -= quantity
                print(f"Order placed for {quantity} {item_name}. Remaining stock: {item['stock']}")
                return
            else:
                print(f"Insufficient stock for {item_name}. Only {item['stock']} left.")
                return
    print(f"{item_name} is not available on the menu.")
