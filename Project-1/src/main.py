from biodata import Biodata


def main():
    bd = Biodata()      # bd is the object of class Biodata
    bd.display_menu()  # Display menu.

    while True:
        choice = int(input("Enter the index number of the task or 0 to quit : "))
        if choice == 1:  # Start a new inventory
            bd.get_inputs()
            bd.new_inv()
        if choice == 2:     # Save the file
            bd.save_inv()
        if choice == 3:     # Read the file
            bd.read_inv()
        if choice == 4:     # Add items to the file
            bd.get_inputs()
            bd.add_item()
        if choice == 5:
            bd.search_inv()
        if choice == 6:
            bd.dis_inv()
        elif choice == 0:
            break


if __name__ != '__main__':
    pass
else:
    main()
