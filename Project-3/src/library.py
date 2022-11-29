"""Create mysql connection and performs CRUD operations in respective tables."""
# global
import mysql.connector
from tabulate import tabulate
from datetime import date
import os


class Library:
    """Creates databases and tables based on user request."""

    def __init__(self):
        """Initialize the mysql connection."""
        self.CREATE_TABLE = '1'
        self.CREATE_Inventory = '2'
        self.INSERT = '3'
        self.REMOVE = '4'
        self.PRINT = '5'
        self.SEARCH = '6'
        self.EXIT = '0'
        self.choice = ''
        self.tab_name = ''
        self.db_name = 'Home_inventory'
        self.date = date.today()
        self.clear = lambda: os.system('clear')

        # connection to database
        try:
            self.connect = mysql.connector.connect(
                host='127.0.0.1',
                user='veera',
                passwd='',
                port=8889,
                autocommit=True,
                db=self.db_name
            )
        except mysql.connector.errors.InterfaceError as e:
            print(f"\n ********* Connect to mamp before trying... ************ \n\n{e}")
            exit()

        # creating database
        self.create_database()

    def display_menu(self):
        """
        Show the functions that we can perform.

        :input: takes an integer and performs respective operation
        :return: None
        """

        print(f'\n\t {self.db_name} Database')
        print('\n\t 1. Create Table.')
        print('\t 2. Create Inventory.')
        print('\t 3. Insert Items.')
        print('\t 4. Remove record.')
        print('\t 5. Print Inventory.')
        print('\t 6. Search.')
        print('\t 0. Exit.')

        self.choice = input("\n Enter the operation number you want to perform: ")

    def create_database(self):
        """Create a database with given name or open the database if it's already exists.

        :param: None
        :input: Name of the database
        :input type: list[str] or None
        :return: creates database
        :return type: str
        :raise Library.InvalidKindError: If the kind is invalid.
        """
        self.clear()
        try:
            print("Connection to MySQL DB successful")
            curs = self.connect.cursor()
            create_db = f"CREATE DATABASE IF NOT EXISTS {self.db_name};"
            curs.execute(create_db)
            print(f"{self.db_name} Database is created.")
            curs.close()
        except ConnectionError as e:
            print(f"The Error is {e}")

    def create_table(self):
        """
        Create required tables with column names given by the user.

        :param: None
        :input: Number of tables
        :input: Name of the table
        :input: column names
        :return: creates a new table with given name and column names
        """
        self.connect.reconnect()
        curs = self.connect.cursor()
        try:
            tab_count = int(input("Enter number of tables you want to create: "))

            for i in range(tab_count):
                choice = input(" Enter 1 to create a parent table or 2 to create a child table: ")
                if choice == '1':
                    self.tab_name = input(f"Enter the table-{i + 1} name: ").capitalize()
                    col_name = input("Enter the primary key column name: ").capitalize()
                    database = f"USE {self.db_name};"
                    curs.execute(database)
                    add_tab = f"CREATE TABLE IF NOT EXISTS {self.tab_name} " \
                              f"({col_name} INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY);"
                    curs.execute(add_tab)
                    add_tab1 = f"ALTER TABLE {self.tab_name} AUTO_INCREMENT=100;"
                    curs.execute(add_tab1)
                    curs.close()
                    self.connect.close()
                    while True:
                        self.connect.reconnect()
                        curs = self.connect.cursor()
                        try:
                            col_name1, col_len1 = input("Enter column name and column length: ").capitalize().split()
                            database = f"USE {self.db_name};"
                            curs.execute(database)
                            if col_name1 != '':
                                add_tab = f" ALTER TABLE {self.tab_name} " \
                                          f"ADD {col_name1} CHAR({col_len1}) NOT NULL"
                            curs.execute(add_tab)
                            curs.close()
                            self.connect.close()
                        except ValueError:
                            print("Table created")
                            database = f"USE {self.db_name};"
                            curs.execute(database)
                            show_tab = "SHOW TABLES;"
                            curs.execute(show_tab)
                            tab = curs.fetchall()
                            for table in tab[:]:
                                print(table[0])
                            break
                    i += 1
                elif choice == '2':
                    self.tab_name = input(f"Enter the table-{i + 1} name: ").capitalize()
                    parent_table = input("Enter the parent table name: ").capitalize()
                    col_name = input("Enter the primary key column name: ").capitalize()
                    foreign_key = input("Enter the foreign key column name: ").capitalize()
                    database = f"USE {self.db_name};"
                    curs.execute(database)

                    add_tab = f"CREATE TABLE IF NOT EXISTS {self.tab_name} " \
                              f"(`{col_name}` INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
                              f"{foreign_key} INT(10)," \
                              f" FOREIGN KEY ({foreign_key}) REFERENCES `{parent_table}`(`{foreign_key}`));"
                    curs.execute(add_tab)
                    add_tab1 = f"ALTER TABLE {self.tab_name} AUTO_INCREMENT=200;"
                    curs.execute(add_tab1)
                    curs.close()
                    self.connect.close()
                    while True:
                        self.connect.reconnect()
                        curs = self.connect.cursor()
                        try:
                            col_name1, col_len1 = input("Enter the column name and column length:").capitalize().split()
                            database = f"USE {self.db_name};"
                            curs.execute(database)
                            if col_name1 != '':
                                add_tab = f" ALTER TABLE {self.tab_name} " \
                                          f"ADD {col_name1} CHAR({col_len1}) NOT NULL"
                            curs.execute(add_tab)
                            curs.close()
                            self.connect.close()
                        except ValueError:
                            print("\nTable created")
                            database = f"USE {self.db_name};"
                            curs.execute(database)
                            show_tab = "SHOW TABLES;"
                            curs.execute(show_tab)
                            tab = curs.fetchall()
                            for table in tab[:]:
                                print(f'\t {i}. {table[0]}')
                                i += 1
                            break
                    i += 1

        except ValueError:
            print("\n*********** Enter a number *************")
        except mysql.connector.errors.ProgrammingError:
            print("\n*********** Enter the required values *************")

    def create_new_inventory(self):
        """
        Create new inventory and inserts the inventory name into inventory table.

        :param: None
        :input: Name of the inventories table name.
        :input: Name of the inventory we want to create.
        :input: Description of the inventory we created.
        :return: Add the name and description of the created inventory to the inventories table.
        """

        try:
            self.connect.reconnect()
            curs = self.connect.cursor()
            tab_name = input("Enter the inventories table name: ").capitalize()
            inv = f"SELECT NAME FROM {tab_name};"
            curs.execute(inv)
            inv_tab = curs.fetchall()
            inventory_list = []
            print(f'\n Inventories list:\n')
            i = 1
            for inv in inv_tab[:]:
                print(f'\t{i}. {inv[0]}')
                inventory_list.append(inv[0])
                i += 1
            inv_name = input("\nEnter the inventory name you want create: ").capitalize()
            if inv_name in inventory_list[:]:
                print("\n Enter a new inventory name")
            elif inv_name == '':
                print("\n************ Enter the inventory name ***************")
            else:
                desc = input(f"Enter the description for {inv_name}: ").capitalize()
                if desc == '':
                    print("\n************ Enter Inventory description. ***********")
                else:
                    add_inv = f"INSERT INTO {tab_name} (Name, Description, Date) " \
                              f"VALUES ('{inv_name}', '{desc}', '{date.today()}');"
                    curs.execute(add_inv)
        except mysql.connector.errors.ProgrammingError:
            print("\n ***************** Enter required values *****************")

    def insert(self):
        """
        Insert the data into the tables.

        :param: None
        :input: table name
        :input: data you want to insert into table
        :return: adds the data given by user into respective tables
        """
        self.clear()
        try:
            self.connect.reconnect()
            curs = self.connect.cursor()
            print("\nSelect the table you want to edit: \n")
            tb = f"SHOW TABLES FROM {self.db_name} ;"
            curs.execute(tb)
            tbs = curs.fetchall()
            curs.close()
            self.connect.cursor()
            tables = []
            i = 1
            for item in tbs[1:]:
                print(f"\t {i}. {item[0]}")
                tables.append(item[0])
                i += 1
            print("\n")
            file_name = input("Enter the name of the table: ").capitalize().capitalize()
            col_names = []
            if file_name in tables[:]:
                print(f"\n\tColumn Names in {file_name} table. \n")
                self.connect.reconnect()
                curs = self.connect.cursor()
                database = f"USE {self.db_name};"
                curs.execute(database)
                column = f"SHOW COLUMNS FROM {file_name}; "
                curs.execute(column)
                result = curs.fetchall()
                curs.close()
                self.connect.close()
                i = 1
                for row in result[:]:
                    print(f"\t {i}. {row[0]}")
                    col_names.append(row[0])
                    i += 1
            else:
                print("Entered table_name doesn't exist.")

            det = []
            choice = True
            while choice:
                self.connect.reconnect()
                curs = self.connect.cursor()

                for i in col_names[1:]:
                    if i != 'Date':
                        x = input(f"Enter the {i}: ").capitalize()
                        det.append(x)
                    else:
                        sql = f" INSERT INTO {file_name} ({i}) VALUES({date.today()});"
                        curs.execute(sql)
                        curs.close()
                        self.connect.close()
                database = f"USE {self.db_name};"
                curs.execute(database)
                sql = f"""INSERT INTO {file_name}  """ \
                      f"""({",".join(i for i in col_names[1:])})""" \
                      f""" VALUES ('{"','".join(i for i in det[:])}');"""
                curs.execute(sql)
                curs.close()
                self.connect.close()
                ch = input("More entries (Y/n):").lower()
                if ch == 'y':
                    choice = True
                    det.clear()
                elif ch == 'n':
                    choice = False
                    print("Data Inserted.")
                    self.connect.reconnect()
                    curs = self.connect.cursor()
                    database = f"USE {self.db_name};"
                    curs.execute(database)
                    data = f"SELECT * FROM {file_name};"
                    curs.execute(data)
                    tb_data = curs.fetchall()
                    for row in tb_data[:]:
                        print(row)

        except mysql.connector.errors.ProgrammingError or mysql.connector.errors.DataError:
            print("\n **************** Enter required data ***************")
        except mysql.connector.errors.IntegrityError:
            print("\n\t *************** Check the foreign key value. ************\n")
        except mysql.connector.errors.DatabaseError:
            print("\n ******** Enter the correct foreign key value *********")

    def remove(self):
        """
        Remove the item by changing the selected column value to the #, and deletes when existing from the database.

        :param: None
        :input: table name
        :input: column name to lookup
        :input: value to be deleted
        :return: changes the value of selected column in selected table to # and deletes it when user entered 0.
        """
        try:
            self.connect.reconnect()
            curs = self.connect.cursor()
            database = f"USE {self.db_name};"
            curs.execute(database)
            print("\n\t Welcome to delete operation\n ")
            print(f"\n List of tables in {self.db_name} database: ")
            tb = f"SHOW TABLES FROM {self.db_name} ;"
            curs.execute(tb)
            tbs = curs.fetchall()
            i = 1
            for item in tbs[:]:
                print(f"\t {i}. {item[0]}")
                i += 1
            print("\n")
            choice = input("Enter 1 if you want to delete table or other key to remove record from table: ")
            if choice == '1':
                table_name = input("Enter the table name you want to delete: ").capitalize()
                table = f"DROP TABLE {table_name}"
                curs.execute(table)
            else:
                file = input("Enter the name of the table: ").capitalize()
                column = f"SHOW COLUMNS from {file}"
                curs.execute(column)
                columns = curs.fetchall()
                print(f"\nColumns in the table {file}:\n")
                i = 1
                for column in columns[2:]:
                    print(f"\t {i}. {column[0]}")
                    i += 1
                col_name = input("Enter the column name you want to lookup: ").capitalize()
                value = str(input("Enter the value you want to delete: ")).capitalize()
                database = f"USE {self.db_name};"
                curs.execute(database)
                column = f"SHOW COLUMNS from {file}"
                curs.execute(column)
                columns = curs.fetchall()
                col1 = []
                for row in columns[2:]:
                    col1 = row[0]
                    break
                del_row = f"UPDATE {file} SET {col1} = '#' WHERE {col_name} = '{value}';"
                curs.execute(del_row)
                print("Successfully added to delete after exit")
                curs.close()
                self.connect.close()
        except mysql.connector.errors.ProgrammingError:
            print("\n ************* Enter the required data. ************* \n")

    def print(self):
        """
        Display the tables in the database.

        :param: None
        :input: table name you want to print
        :return: shows the data inside the tables based on the user input
        """
        self.clear()
        self.connect.reconnect()
        curs = self.connect.cursor()
        tb = f"SHOW TABLES FROM {self.db_name} ;"
        curs.execute(tb)
        tbs = curs.fetchall()
        i = 2
        print(f"\nTables in {self.db_name}: ")
        print(f'\n\t 1. ALL_TABLES')
        for item in tbs[:]:
            print(f"\t {i}. {item[0]}")
            i += 1
        print("\n")
        file = input("Enter the table name or 1 to print all tables: ").capitalize()

        if file == '1':
            database = f"use {self.db_name};"
            curs.execute(database)
            for item in tbs[:]:
                print(f'\n****** {item[0]} ******')
                p = f'SELECT * FROM {item[0]};'
                curs.execute(p)
                pp = curs.fetchall()
                self.connect.close()
                columns = []
                self.connect.reconnect()
                database = f"USE {self.db_name};"
                curs.execute(database)
                curs.execute(f"SHOW COLUMNS FROM {item[0]};")
                out = curs.fetchall()
                for column in out[:]:
                    columns.append(column[0])
                print(tabulate(pp, headers=columns, tablefmt='psql'))
        else:
            try:
                database = f"USE {self.db_name};"
                curs.execute(database)
                p = f" SELECT * FROM {file};"
                curs.execute(p)
                pp = curs.fetchall()
                self.connect.close()
                columns = []
                self.connect.reconnect()
                database = f"USE {self.db_name};"
                curs.execute(database)
                curs.execute(f"SHOW COLUMNS FROM {file}")
                out = curs.fetchall()
                for column in out[:]:
                    columns.append(column[0])
                print(tabulate(pp, headers=columns, tablefmt='psql'))

            except ConnectionError:
                print(f"{file} table doesn't exist.")

            except mysql.connector.errors.ProgrammingError:
                print("\n**************Enter the existed table name.***************")

    def search(self):
        """
        Display the information of the looked up item.

        :param: None
        :input: table name to lookup
        :input: value to look
        :return: shows the requested value information if exist
        """
        try:
            self.connect.reconnect()
            curs = self.connect.cursor()
            tb = f"SHOW TABLES FROM {self.db_name} ;"
            curs.execute(tb)
            tbs = curs.fetchall()
            i = 1
            print(f"\nTables in {self.db_name}: ")
            for item in tbs[:]:
                print(f"\t {i}. {item[0]}")
                i += 1
            print("\n")
            file = input("Enter the table name to search: ").capitalize()
            c_name = input("Enter the column name to lookup: ").capitalize()
            search_key = input("Enter the value to search: ").capitalize()
            try:
                database = f"USE {self.db_name};"
                curs.execute(database)
                p = f" SELECT * FROM {file} where {c_name} = '{search_key}'"
                curs.execute(p)
                pp = curs.fetchall()
                self.connect.close()
                columns = []
                self.connect.reconnect()
                database = f"USE {self.db_name};"
                curs.execute(database)
                curs.execute(f" SHOW COLUMNS FROM {file}")
                out = curs.fetchall()
                for column in out[:]:
                    columns.append(column[0])
                print(tabulate(pp, headers=columns, tablefmt='psql'))

            except ConnectionError:
                print(f"{file} table doesn't exist.")
        except mysql.connector.errors.ProgrammingError:
            print("\n **************** Enter the required data *************** \n")

    def purge(self):
        """
        Delete the values selected in the remove function and closes the mysql connection.

        :param: None
        :input: table name and column name to lookup for deletion
        :return: closes the connection with mysql database
        """
        self.connect.connect()
        curs = self.connect.cursor()
        database = f"USE {self.db_name};"
        curs.execute(database)
        try:
            file, col = input("Enter the file name and column name to delete selected files: ").split()
            curs.execute(f"DELETE FROM {file} WHERE {col} LIKE '%#%';")
            print("\n Deleted and disabled connection successfully \n ")
        except ValueError:
            print("\n Connection Disabled successfully \n")
        except mysql.connector.errors.ProgrammingError:
            print("\n Connection Disabled successfully \n")

    def application(self):
        """
        Run the application until user enters 0.

        :return: create, insert, or delete databases or tables based on the user input
        """
        match self.choice:
            case self.CREATE_TABLE:
                # self.create_database()
                self.create_table()
            case self.CREATE_Inventory:
                self.create_new_inventory()
            case self.INSERT:
                self.insert()
            case self.REMOVE:
                self.remove()
            case self.PRINT:
                self.print()
            case self.SEARCH:
                self.search()
            case self.EXIT:
                self.purge()
                return
        self.display_menu()
        self.application()
