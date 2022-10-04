from app import ItemsList


def main():
    """Execute when it's the main execution module."""
    home_inventory_app = ItemsList()
    home_inventory_app.start_application()


# Call main() if this is the main execution module
if __name__ == '__main__':
    main()
