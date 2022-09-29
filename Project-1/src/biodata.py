import json

global inventory


class Biodata:
    """ Collect the information from the user. Such as Name, Age, Gender, Mobile_Number, State, Country. """
    customer_details = []

    def __init__(self):
        self.cust_id = None
        self.name = None
        self.age = None
        self.gender = None
        self.mobile_number = None
        self.state = None
        self.country = None
        # self.get_inputs()

    def display_menu(self):
        menu = {}
        menu['1'] = "Start a new inventory."
        menu['2'] = "Save inventory to file."
        menu['3'] = "Read inventory from file."
        menu['4'] = "Add items to active inventory."
        menu['5'] = "Search inventory."
        menu['6'] = "Display inventory."
        for key in menu.keys():
            print(f"{key}. {menu[key]}")

    def get_inputs(self):
        self.cust_id = int(input("Enter the customer Id: "))
        self.name = input("Enter your name: ").capitalize()
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ").capitalize()
        self.mobile_number = int(input("Enter your mobile number: "))
        self.state = input("Enter your state: ").capitalize()
        self.country = str(input("Enter your country: ").capitalize())

    def new_inv(self):
        global inventory   # Dict
        inventory = {self.cust_id: {"Name": self.name, "Age": self.age, "Gender": self.gender,
                                    "Mobile_Number": self.mobile_number,
                                    "State": self.state, "Country": self.country}}

        print(f'The details you entered are {inventory}')
        print("To save the details enter 2. ")

    def read_inv(self):
        with open("database.json", "r") as db:
            file = db.readline()
            print(type(file))           # String
            if len(file) == 0:
                print(f"{db.name} file is empty.")
            else:
                print(file)

    def save_inv(self):
        global inventory
        with open("database.json", "w") as db:
            json.dump(inventory, db, indent=2)

    def add_item(self):
        new = {self.cust_id: {"Name": self.name, "Age": self.age, "Gender": self.gender,
                              "Mobile_Number": self.mobile_number,
                              "State": self.state, "Country": self.country}}
        with open("database.json", "r+") as db:
            data = json.load(db)
            print(type(data))           # Dict
            data.update(new)
            print(data)
            db.seek(0)
            json.dump(data, db, indent=2)
        print("New data is added to inventory")

    def search_inv(self):
        num = input("Enter the customer Id to search: ")
        f = open("database.json", "r")
        print(type(f))          # TextIOWrapper
        dic = json.load(f)
        print(type(dic))        # Dict
        f.close()
        for key, value in dic.items():
            # print(value)
            if num == key:
                print(value)

    def dis_inv(self):
        with open("database.json", "r") as db:
            output = json.load(db)
            print(type(output))
            for k, v in output.items():
                print(f"Cust_ID: {k}:")
                for k1, v1 in v.items():
                    print(f"\t{k1}: {v1}")
