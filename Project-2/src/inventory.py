import json
from datetime import date


class Inventory:
    """Implements household inventory control features."""

    def __init__(self):
        """Initialize object."""
        # Constants
        self.NEW_INVENTORY = '1'
        self.LOAD_INVENTORY = '2'
        self.LIST_INVENTORY = '3'
        self.SEARCH_INVENTORY = '4'
        self.EXIT = '0'
        # Fields
        self.menu_choice = 1
        self.keep_going = True
        # Inputs
        self.item_name = None
        self.room_name = None
        self.item_price = None
        self.item_quantity = None
        self.item_num = None

    def display_menu(self):
        """Display menu."""
        print('\n\tHousehold Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. Load Inventory')
        print('\t\t3. List Inventory')
        print('\t\t4. Search Inventory')
        print('\t\t0. Exit')
        print()

    def get_inputs(self):
        # Inputs
        self.item_name = input("Enter the item name: ").capitalize()
        self.item_num = int(input("Enter the item number: "))
        self.room_name = input("Enter the room name you want to place the item: ").capitalize()
        self.item_price = int(input("Enter the item price: $"))
        self.item_quantity = int(input("Enter the item quantity: "))

    def new_inventory(self):
        """Create new inventory."""
        print('new_inventory() method called...')
        new = {}
        new["Type"] = input("Enter the type: ").capitalize()
        new["Date"] = date.today().strftime("%m-%d-%y")
        new["Items"] = {self.item_num: {"Item Name": self.item_name, "Room": self.room_name,
                                        "Item Price": self.item_price, "Item Quantity": self.item_quantity}}
        with open("database.json", "w") as db:
            json.dump(new, db, indent=2)

    def load_inventory(self):
        """Load inventory from file."""
        print('load_inventory() method called...')
        new1 = {self.item_num: {"Item Name": self.item_name, "Room": self.room_name, "Item Price": self.item_price,
                                "Item Quantity": self.item_quantity}}

        with open("database.json", "r+") as db:
            data = json.load(db)
            print(type(data["Items"]))  # Dict
            data["Items"].update(new1)
            db.seek(0)
            json.dump(data, db, indent=2)

    def list_inventory(self):
        """List inventory."""
        print('list_inventory() method called...\n')
        with open("database.json", "r") as db:
            output = json.load(db)
        for k, v in output.items():
            if k == "Items":
                for k1, v1 in output[k].items():
                    print(f"Item Number: {k1}")
                    for k2, v2 in v1.items():
                        print(f"\t{k2}: {v2}")
                    print("\n")

    def search_inventory(self):
        """Search Inventory"""
        print("Search_inventory() method is called...\n")
        with open("database.json", "r") as db:
            search = json.load(db)
        print("Enter 1 or 2 to lookup or any other key for main menu.")
        print("\nChoose the lookup option: \n 1. Item Number \n 2. Item Name")
        search_opt = input("Enter your choice: ")
        if search_opt == '1':
            i_num = int(input("Enter the item number you want to search: "))
            for k, v in search.items():
                if k == "Items":
                    for k1, v1 in search[k].items():
                        if int(k1) == i_num:
                            print(f"\nItem Number: {k1}")
                            for k2, v2 in v1.items():
                                print(f"\t{k2}: {v2}")
                            print("\n")
                        else:
                            pass
        elif search_opt == '2':
            i_name = str(input("Enter the item name you want to search: ")).capitalize()
            for k, v in search.items():
                if k == "Items":
                    for k1, v1 in search[k].items():
                        for k2, v2 in search[k][k1].items():
                            if v2 == i_name:
                                print(f"\nItem Number: {k1}")
                                for k3, v3 in v1.items():
                                    print(f"\t{k3}: {v3}")
                                print("\n")
                        else:
                            pass
        else:
            return

