from inventory import Inventory
import json


class ItemsList(Inventory):     # Inheritance

    def process_menu_choice(self):
        """Process menu choice and execute corresponding methods."""
        self.menu_choice = input('Please enter menu item number:')
        print(f'You entered: {self.menu_choice}\n')
        match self.menu_choice:
            case self.NEW_INVENTORY:
                self.new_inventory()
            case self.LOAD_INVENTORY:
                self.load_inventory()
            case self.LIST_INVENTORY:
                self.list_inventory()
            case self.SEARCH_INVENTORY:
                self.search_inventory()
            case self.COUNT_O_EACH_ITEM:
                self.count_o_each_item()
            case self.EXIT:
                test = open("database.json", "r")
                tdata = json.load(test)
                i = 0
                for key, value in tdata["Items"].items():
                    i += 1
                    while i == len(tdata["Items"]):
                        print("\n\t Items added lastly")
                        print(f'-->\nItem Number: {key}')
                        for k1, v1 in value.items():
                            print(f'\t{k1: <15}\t - {v1}')
                        break
                    print()
                    self.keep_going = False
            case _:
                print('Invalid Menu Choice!')

    def start_application(self):
        """Start the applications."""
        while self.keep_going:
            self.display_menu()
            self.process_menu_choice()
