import json

# Function to load inventory data from a JSON file
def load_inventory(filename):
    try:
        with open(filename, 'r') as file:
            inventory_data = json.load(file)
    except FileNotFoundError:
        inventory_data = {}
    return inventory_data

# Function to save inventory data to a JSON file
def save_inventory(inventory_data, filename):
    with open(filename, 'w') as file:
        json.dump(inventory_data, file, indent=4)

# Function to display the entire inventory
def display_inventory(inventory_data):
    print("Inventory:")
    for item, details in inventory_data.items():
        print(f"{item}: Quantity - {details[0]}, Price per unit - ${details[1]}")

# Function to add a new item to the inventory
def add_item(inventory_data, item, quantity, price_per_unit):
    inventory_data[item] = [quantity, price_per_unit]
    print(f"Item '{item}' added to inventory.")

# Function to update an existing item in the inventory
def update_item(inventory_data, item, quantity, price_per_unit):
    if item in inventory_data:
        inventory_data[item] = [quantity, price_per_unit]
        print(f"Item '{item}' updated.")
    else:
        print(f"Item '{item}' not found in inventory.")

# Function to remove an item from the inventory
def remove_item(inventory_data, item):
    if item in inventory_data:
        del inventory_data[item]
        print(f"Item '{item}' removed from inventory.")
    else:
        print(f"Item '{item}' not found in inventory.")


def main():
    filename = "inventory.json"
    inventory_data = load_inventory(filename)

    while True:
        print("\nMenu:")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Save and Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_inventory(inventory_data)
        elif choice == '2':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            add_item(inventory_data, item, quantity, price_per_unit)
        elif choice == '3':
            item = input("Enter item name to update: ")
            if item in inventory_data:
                quantity = int(input("Enter new quantity: "))
                price_per_unit = float(input("Enter new price per unit: "))
                update_item(inventory_data, item, quantity, price_per_unit)
            else:
                print(f"Item '{item}' not found in inventory.")
        elif choice == '4':
            item = input("Enter item name to remove: ")
            remove_item(inventory_data, item)
        elif choice == '5':
            save_inventory(inventory_data, filename)
            print("Inventory saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
