class Inventory:
    """Implements household inventory control features."""
    number_of_items = 0

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

    def get_inputs(self):
        # Inputs
        self.item_name = input("Enter the item name: ").capitalize()
        self.item_num = int(input("Enter the item number: "))
        self.room_name = input("Enter the room name you want to place the item: ").capitalize()
        self.item_price = int(input("Enter the item price: $"))
        self.item_quantity = int(input("Enter the item quantity: "))
