import json

from src.inventory import Inventory

global number_of_items


class ItemsList(Inventory):     # Inheritance
    number_of_items = 0

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

    def new_inventory(self):
        """Create new inventory."""
        new = {self.item_num: {"Item Name": self.item_name, "Room": self.room_name, "Item Price": self.item_price,
                               "Item Quantity": self.item_quantity}}
        with open("database.json", "w") as db:
            json.dump(new, db, indent=2)
        print('new_inventory() method called...')
        print(f'Number of items = {ItemsList.number_of_items + 1}')

    def load_inventory(self):
        """Load inventory from file."""
        global number_of_items
        number_of_items = 0
        new1 = {self.item_num: {"Item Name": self.item_name, "Room": self.room_name, "Item Price": self.item_price,
                                "Item Quantity": self.item_quantity}}
        with open("database.json", "r+") as db:
            data = json.load(db)
            # print(type(data))  # Dict
            data.update(new1)
            for item in data.items():
                number_of_items += 1
            # print(data)
            db.seek(0)
            json.dump(data, db, indent=2)
        print('load_inventory() method called...')
        print(f'Number of items = {number_of_items}')

    def list_inventory(self):
        """List inventory."""
        print(f'Number of items = {number_of_items}')
        with open("database.json", "r") as db:
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
