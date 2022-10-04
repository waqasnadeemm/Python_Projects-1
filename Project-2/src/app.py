from src.inventory import Inventory


class ItemsList(Inventory):     # Inheritance

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
            case self.SEARCH_INVENTORY:
                self.search_inventory()
            case self.EXIT:
                print('Goodbye!')
                self.keep_going = False
            case _:
                print('Invalid Menu Choice!')

    def start_application(self):
        """Start the applications."""
        while self.keep_going:
            self.display_menu()
            self.process_menu_choice()
