"""Implements Team Roster Operations"""
import os
from datetime import date
import json
from json import JSONDecodeError


class Roster(object):
    """Implements Team Roster Operations"""

    def __init__(self):
        """Initialize object."""

        # Constants
        self.NEW_ROSTER = '1'
        self.LOAD_ROSTER = '2'
        self.PRINT_ROSTER = '3'
        self.ADD_MEMBERS = '4'
        self.SAVE_ROSTER = '5'
        self.EXIT = '7'

        # Fields
        self.menu_choice = 1
        self.keep_going = True

        # inputs
        self.roaster_type = None
        self.sport = None
        self.country = None
        self.name = None
        self.age = None

    def clear_screen(self):
        os.system('clear')

    def display_menu(self):
        """Display menu."""
        print('\t\t\tTeam Roster Application')
        print()
        print('\t\t1. New Roster')
        print('\t\t2. Load Roster')
        print('\t\t3. Print Roster')
        print('\t\t4. Add Team Members to Roster')
        print('\t\t5. Save Roster')
        print('\t\t7. Exit')
        print()

    def new_roster(self):
        """Create new roster."""
        self.clear_screen()
        if __debug__:
            print('new_roster() method called...')
            self.roaster_type = input("Enter the type of roster:")
            self.sport = input("Enter the sport name:")
            self.country = input("Enter the name of the country:")

            with open("../data/team_roster.json", "r+") as rs:
                try:
                    old = json.load(rs)
                except JSONDecodeError:
                    old = {}
                new = {'Type': self.roaster_type, 'Date': date.today().strftime("%Y-%m-%d"), 'Sport': self.sport,
                       'Country': self.country, 'Members': []}
                old.update(new)
                rs.seek(0)
                json.dump(old, rs, indent=2)

    def load_roster(self):
        """Load roster from file."""
        self.clear_screen()
        if __debug__:
            print('load_roster() method called...')

    def print_roster(self):
        """Print roster."""
        self.clear_screen()
        if __debug__:
            print('print_roster() method called...')

    def save_roster(self):
        """Save roster to file."""
        self.clear_screen()
        if __debug__:
            print('save_roster() method called...')

    def add_members(self):
        """Add items to roster."""
        self.clear_screen()
        if __debug__:
            print('print_roster() method called...')
