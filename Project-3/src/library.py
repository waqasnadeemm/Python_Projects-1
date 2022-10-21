import maskpass as mp
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate


class Library:

    def __init__(self):

        self.CREATE_TABLE = '1'
        self.INSERT = '2'
        self.REMOVE = '3'
        self.PRINT = '4'
        self.EXIT = '0'
        self.choice = ''
        self.tab_name = ''
        self.db_name = input('Enter the database name: ').capitalize()
        self.connect = mysql.connector.connect(
            host='localhost',
            user='veera',
            passwd=mp.askpass(prompt='Enter the password for user VEERA: '),
            autocommit=True,
            db=self.db_name
            )
        print("")

    def display_menu(self):
        print(f'\n\t Details')
        print('\n\t 1. Create Table.')
        print('\t 2. Insert.')
        print('\t 3. Remove record.')
        print('\t 4. Print File.')
        print('\t 0. Exit.')

        self.choice = int(input("\n Enter the operation number you want to perform: "))

    def create_database(self):

        try:
            print("Connection to MySQL DB successful")
            curs = self.connect.cursor()
            # self.db_name = input("Enter the database name: ").capitalize()
            create_db = f"CREATE DATABASE IF NOT EXISTS {self.db_name};"
            curs.execute(create_db)
            print(f"{self.db_name} Database is created.")
            curs.fetchall()
            curs.close()
            self.connect.close()
        except Error as e:
            print(f"The Error is {e}")

    def create_table(self):
        self.connect.reconnect()
        curs = self.connect.cursor()
        tab_count = int(input("Enter number of tables you want to create: "))
        print(f"The list of tables: ")

        for i in range(tab_count):
            self.connect.reconnect()
            self.tab_name = input(f"Enter the table-{i + 1} name: ").capitalize()
            col_name, col_len = input("Enter the column name and column length: ").capitalize().split()
            add_tab = f"CREATE TABLE IF NOT EXISTS {self.tab_name} " \
                      f"({col_name} CHAR({col_len}) NOT NULL)"
            curs.execute(add_tab)
            curs.close()
            self.connect.close()
            while True:
                self.connect.reconnect()
                curs = self.connect.cursor()
                try:
                    col_name1, col_len1 = input("Enter the column name and column length: ").capitalize().split()
                    if col_name1 != '':
                        add_tab = f" ALTER TABLE {self.tab_name} " \
                                  f"ADD {col_name1} CHAR({col_len1}) NOT NULL"
                    curs.execute(add_tab)
                    curs.close()
                    self.connect.close()
                except ValueError:
                    print("Table created")
                    break
            i += 1

    def insert(self):
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
        for item in tbs[:]:
            print(f"\t {i}. {item[0]}")
            tables.append(item[0])
            i += 1
        print("\n")
        file_name = input("Enter the name of the file(table): ").capitalize()
        col_names = []
        if file_name in tables[:]:
            print(f"\n\tColumn Names in {file_name} table. \n")
            self.connect.reconnect()
            curs = self.connect.cursor()
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
            print(col_names[:])
        else:
            print("Entered table_name doesn't exist.")

        det = []
        choice = True
        while choice:
            self.connect.reconnect()
            curs = self.connect.cursor()
            # i = 0
            for i in range(len(col_names[:])):
                x = input(f"Enter the {col_names[i]}: ").capitalize()
                det.append(x)
                i += 1
            sql = f"""INSERT INTO {file_name}  """ \
                  f"""({",".join(col_names[i] for i in range(len(col_names)))})""" \
                  f""" VALUES ('{"','".join(det[i] for i in range(len(det)))}');"""
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

    def remove(self):

        self.connect.reconnect()
        curs = self.connect.cursor()
        print("\n\t Welcome to delete operation\n ")
        file = input("Enter the name of the file: ").capitalize()
        col_name = input("Enter the column name you want to lookup: ").capitalize()
        value = str(input("Enter the value you want to delete: ")).capitalize()
        del_row = f""" UPDATE {file} SET col1 = '#' WHERE {col_name} = '{value}';"""
        curs.execute(del_row)
        print("Successfully added to delete after exit")
        curs.close()
        self.connect.close()

    def print(self):
        file = input("Enter the table name: ").capitalize()
        try:
            self.connect.reconnect()
            curs = self.connect.cursor()
            p = f" SELECT * FROM {file}"
            curs.execute(p)
            pp = curs.fetchall()
            print(pp)
            # result = curs.fetchall()
            self.connect.close()
            columns = []
            self.connect.reconnect()
            curs.execute(f" SHOW COLUMNS FROM {file}")
            out = curs.fetchall()
            print(out)
            for column in out[:]:
                columns.append(column[0])
            print(columns)
            print(tabulate(pp, headers=columns, tablefmt='psql'))
            pass

        except Error:
            print(f"{file} table doesn't exist.")

    def purge(self):
        self.connect.connect()
        curs = self.connect.cursor()
        try:
            file, col = input("Enter the file name and column name to delete selected files: ").split()
            curs.execute(f"DELETE FROM {file} WHERE {col} LIKE '%#%';")
        except ValueError:
            print("\n Connection Disabled successfully")

    def application(self):
        match str(self.choice):
            case self.CREATE_TABLE:
                self.create_database()
                self.create_table()
            case self.INSERT:
                self.insert()
            case self.REMOVE:
                self.remove()
            case self.PRINT:
                self.print()
            case self.EXIT:
                self.purge()
                return
        self.display_menu()
        self.application()
