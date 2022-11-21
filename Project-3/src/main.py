from library import Library


def main():
    """
    This is the main module of the project, from where we run the code.

    :return: performs the task according to the user input.
    """
    lib = Library()

    lib.display_menu()
    lib.application()


if __name__ == '__main__':
    main()
