import json


class Inventory:
    """Implements household inventory control features."""

    def __init__(self):
        """Initialize object."""
        # Constants
        self.NEW_INVENTORY = '1'
        self.LOAD_INVENTORY = '2'
        self.LIST_INVENTORY = '3'
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
        print('\tHousehold Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. Load Inventory')
        print('\t\t3. List Inventory')
        print('\t\t0. Exit')
        print()

    def process_menu_choice(self):
        """Process menu choice and execute corresponding methods."""
        self.menu_choice = input('Please enter menu item number:')
        print(f'You entered: {self.menu_choice}\n')
        match self.menu_choice:
            case self.NEW_INVENTORY:
                self.get_inputs()
                self.new_inventory()
            case self.LOAD_INVENTORY:
                self.get_inputs()
                self.load_inventory()
            case self.LIST_INVENTORY:
                self.list_inventory()
            case self.EXIT:
                print('Goodbye!')
                self.keep_going = False
            case _:
                print('Invalid Menu Choice!')

    def get_inputs(self):
        # Inputs
        self.item_name = input("Enter the item name: ").capitalize()
        self.item_num = int(input("Enter the item number: "))
        self.room_name = input("Enter the room name you want to place the item: ").capitalize()
        self.item_price = int(input("Enter the item price: $"))
        self.item_quantity = int(input("Enter the item quantity: "))

    def new_inventory(self):
        """Create new inventory."""
        new = {self.item_num: {"Item Name": self.item_name, "Room": self.room_name, "Item Price": self.item_price,
                               "Item Quantity": self.item_quantity}}
        with open("src/database.json", "w") as db:
            json.dump(new, db, indent=2)
        print('new_inventory() method called...')

    def load_inventory(self):
        """Load inventory from file."""
        new1 = {self.item_num: {"Item Name": self.item_name, "Room": self.room_name, "Item Price": self.item_price,
                                "Item Quantity": self.item_quantity}}
        ls = list(new1)
        with open("src/database.json", "r+") as db:
            data = json.load(db)
            # print(type(data))  # Dict
            data.update(new1)
            # print(data)
            db.seek(0)
            json.dump(data, db, indent=2)
        print('load_inventory() method called...')

    def list_inventory(self):
        """List inventory."""
        with open("src/database.json", "r") as db:
            output = json.load(db)
            # print(type(output))
            for k, v in output.items():
                print(f"Item_num: {k}:\n")
                for k1, v1 in v.items():
                    print(f"\t{k1}: {v1}\n")
        print('list_inventory() method called...\n')

    def start_application(self):
        """Start the applications."""
        while self.keep_going:
            self.display_menu()
            self.process_menu_choice()
