from app import ItemsList


def main():
    """Execute when it's the main execution module."""
    home = ItemsList()
    home.start_application()
    print(f"\n {home}\n \n\t Goodbye!")


# Call main() if this is the main execution module
if __name__ == '__main__':
    main()
