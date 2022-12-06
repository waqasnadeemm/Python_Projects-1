"""Implements application business logic."""

from persistence_wrapper_interface import PersistenceWrapperInterface
from mysql_persistence_wrapper import MySQLPersistenceWrapper
import json


class BusinessLogic:
	"""Implements application business logic."""

	def __init__(self):
		"""Initialize object."""
		self._persistence_wrapper = MySQLPersistenceWrapper()

	def get_all_inventories(self):
		"""Returns a list of inventories."""
		query_results = None
		try:
			query_results = self._persistence_wrapper.get_all_inventories()
		except Exception as e:
			print(f'Exception in business logic: {e}')
		return query_results

	def get_all_inventories_with_format(self, format: str):
		"""Returns all inventories in requested format. Only supported format is JSON. Add others as required."""
		query_results = None
		try:
			query_results = self._persistence_wrapper.get_all_inventories()
		except Exception as e:
			print(f'Exception in business logic: {e}')
		
		return_results = None
		try:
			match format:
				case 'json': return_results = json.dumps(query_results)
		except Exception as e:
			print(f'Exception in business logic: {e}')
		return return_results

	def create_new_inventory(self, name: str, description: str, date_created: str):
		"""Adds a new inventory to the datastore."""
		inventory_id = 0
		try:
			inventory_id = self._persistence_wrapper.create_inventory(name, description, date_created)
		except Exception as e:
			print(f'Exception in business logic: {e}')
		return inventory_id

	def add_new_items(self, inventory_id: int, item: str, count: int):
		"""Adds a new item to the items table."""
		new_item = 0
		try:
			new_item = self._persistence_wrapper.create_item(inventory_id=inventory_id, item=item, count=count)
		except Exception as e:
			print(f'Exception is {e}')
		return new_item

	def search_item_by_id(self, item_id: int):
		"""Search for the item in items table"""
		try:
			search = self._persistence_wrapper.search_by_id(item_id=item_id)
		except Exception as e:
			print(f'Exception is {e}')
		return search

	def search_item_by_name(self, item_name: str):
		"""Search for the item in items table"""
		try:
			search = self._persistence_wrapper.search_by_name(item_name=item_name)
		except Exception as e:
			print(f'Exception is {e}')
		return search

	def get_items_for_inventory_id(self, id):
		"""Gets all items for given inventory id."""
		query_results = None
		try:
			query_results = self._persistence_wrapper.get_items_for_inventory(id)
		except Exception as e:
			print(f'Exception in business logic: {e}')
		return query_results
