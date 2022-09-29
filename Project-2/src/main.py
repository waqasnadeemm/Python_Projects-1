from inventory import Inventory


def main():
    """Execute when it's the main execution module."""
    home_inventory_app = Inventory()
    home_inventory_app.start_application()


# Call main() if this is the main execution module
if __name__ == '__main__':
    main()
