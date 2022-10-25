"""Implements household roster control features."""

from roster import Roster
from subprocess import call


class RosterApp(Roster):
	"""Implements household roster control features."""

	def process_menu_choice(self):
		"""Process menu choice and execute corresponding methods."""
		self.menu_choice = input('Please enter menu item number: ')
		if __debug__:
			print(f'You entered: {self.menu_choice}')
		match self.menu_choice:
			case self.NEW_ROSTER:
				self.new_roster()
			case self.LOAD_ROSTER:
				self.load_roster()
			case self.PRINT_ROSTER:
				self.print_roster()
			case self.ADD_MEMBERS:
				self.add_members()
			case self.SAVE_ROSTER:
				self.save_roster()
			case self.EXIT:
				if __debug__:
					print('Goodbye!')
				self.keep_going = False
				self.clear_screen()
			case _:
				self.clear_screen()
				print('Invalid Menu Choice!')

	def start_application(self):
		"""Start the applications."""
		# Clear Screen
		self.clear_screen()
		while self.keep_going:
			self.display_menu()
			self.process_menu_choice()
