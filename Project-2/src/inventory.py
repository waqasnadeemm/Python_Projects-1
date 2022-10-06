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

    def __str__(self):  # magic method
        return f"\tItem added lastly \n-----> {self.item_num} - {self.item_name}."

    def decorator1(func):
        def inner(self):
            print("*" * 40)
            func(self)
            print("*" * 40)
        return inner

    def decorator2(func):
        def inner(self):
            print("#" * 40)
            func(self)
            print("#" * 40)
        return inner

    @decorator2
    @decorator1
    def display_menu(self):
        """Display menu."""
        print('\tHousehold Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. Load Inventory')
        print('\t\t3. List Inventory')
        print('\t\t4. Search Inventory')
        print('\t\t0. Exit')

    def get_inputs(self):
        # Inputs
        self.item_num = int(input("Enter the item number: "))
        self.item_name = input("Enter the item name: ").capitalize()
        self.room_name = input("Enter the room name you want to place the item: ").capitalize()
        self.item_price = int(input("Enter the item price: $"))
        self.item_quantity = int(input("Enter the item quantity: "))

    @decorator1
    def new_inventory(self):
        """Create new inventory."""
        new = {}
        new["Name"] = input("Enter the name of the inventory: ").capitalize()
        new["Date Modified"] = date.today().strftime("%m-%d-%y")
        print('new_inventory() method called...')
        Inventory.get_inputs(self)
        new["Items"] = {self.item_num: {"Item Name": self.item_name, "Room": self.room_name,
                                        "Item Price": self.item_price, "Item Quantity": self.item_quantity}}
        with open("database.json", "w") as db:
            json.dump(new, db, indent=2)

    def load_inventory(self):
        """Load inventory from file."""
        print('load_inventory() method called...')

        with open("database.json", "r+") as db:
            data = json.load(db)
            print("List of Item numbers in the inventory:")
            for k, v in data.items():
                if k == "Items":
                    i = 1
                    for k1 in data[k].keys():
                        li = [k1]
                        print(f"\t{i}. {k1}")
                        i += 1
            Inventory.get_inputs(self)
            if str(self.item_num) in li[:]:
                print("\n\tItem number is already used.")
            else:
                new1 = {
                    self.item_num: {"Item Name": self.item_name, "Room": self.room_name, "Item Price": self.item_price,
                                    "Item Quantity": self.item_quantity}}
                data["Date Modified"] = date.today().strftime("%m/%d/%y")
                data["Items"].update(new1)
                db.seek(0)
                json.dump(data, db, indent=2)

    @decorator2
    def list_inventory(self):
        """List inventory."""
        print('list_inventory() method called...\n')
        with open("database.json", "r") as db:
            output = json.load(db)
        print("Items list:")
        for k, v in output.items():
            if k == "Items":
                for k1, v1 in output[k].items():
                    for k2, v2 in v1.items():
                        if k2 == "Item Name":
                            print(f'{k1} : {v2}')
        choice = int(input("For brief information of items. Press 1 : "))
        if choice == 1:
            for k, v in output.items():
                if k == "Items":
                    for k1, v1 in output[k].items():
                        print(f"Item Number: {k1}")
                        for k2, v2 in v1.items():
                            print(f"\t{k2}: {v2}")
                        print("\n")
        else:
            pass

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
