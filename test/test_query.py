
import unittest

from query.build import _where, _separate_field_value, delete, insert, select, update
from query.operator.comparison import EQ, GT, GTE, LT, LTE, NEQ
from query.operator.logical import AND, OR

class TestQuery(unittest.TestCase):
	def test_where(self):
		conditions = [EQ('a', 1), AND(), EQ('b', 2), OR(), EQ('c', 3)]
		self.assertEqual(_where(conditions), 'WHERE a = 1 AND b = 2 OR c = 3')

		conditions = [LT('a', 1), AND(), NEQ('b', 2), OR(), GT('c', 3), AND(), GTE('d', 4)]
		self.assertEqual(_where(conditions), 'WHERE a < 1 AND b != 2 OR c > 3 AND d >= 4')

		conditions = [EQ('a', 1), AND(), EQ('b', 2), OR(), LTE('c', 3), AND(), LT('d', 4)]
		self.assertEqual(_where(conditions), 'WHERE a = 1 AND b = 2 OR c <= 3 AND d < 4')

		# Test without AND/OR -> should raise ValueError
		conditions = [EQ('a', 1), EQ('b', 2)]
		with self.assertRaises(ValueError):		_where(conditions)
		
		# Test without AND/OR -> should raise ValueError
		conditions = [EQ('a', 1), EQ('b', 2), EQ('a', 1)]
		with self.assertRaises(ValueError):		_where(conditions)

		# Test without EQ/NEQ/GT/GTE/LT/LTE -> should raise ValueError
		conditions = [AND(), OR()]
		with self.assertRaises(ValueError):		_where(conditions)

		# Test without EQ/NEQ/GT/GTE/LT/LTE -> should raise ValueError
		conditions = [AND(), OR(), EQ('a', 1)]
		with self.assertRaises(ValueError):		_where(conditions)

		# Test in invalid order -> should raise ValueError
		conditions = [AND(), EQ('a', 1), EQ('b', 2)]
		with self.assertRaises(ValueError):		_where(conditions)
		
		# Test in invalid order -> should raise ValueError
		conditions = [EQ('a', 1), EQ('b', 2), AND()]
		with self.assertRaises(ValueError):		_where(conditions)

	def test_separate_field_value(self):
		field_value = {'a': 1, 'b': 2, 'c': 3}
		self.assertEqual(_separate_field_value(field_value), ('a, b, c', '1, 2, 3'))

		field_value = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
		self.assertEqual(_separate_field_value(field_value), ('a, b, c, d', '1, 2, 3, 4'))
		pass

	def test_insert(self):
		field_value = {'a': 1, 'b': 2, 'c': 3}
		self.assertEqual(insert('chicken_table', field_value), 'INSERT INTO chicken_table (a, b, c) VALUES (1, 2, 3)')

		field_value = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
		self.assertEqual(insert('chicken_table', field_value), 'INSERT INTO chicken_table (a, b, c, d) VALUES (1, 2, 3, 4)')

	def test_delete(self):
		conditions = [EQ('a', 1), AND(), EQ('b', 2), OR(), EQ('c', 3)]
		self.assertEqual(delete('chicken_table', conditions), 'DELETE FROM chicken_table WHERE a = 1 AND b = 2 OR c = 3')

		conditions = [LT('a', 1), AND(), NEQ('b', 2), OR(), GT('c', 3), AND(), GTE('d', 4)]
		self.assertEqual(delete('chicken_table', conditions), 'DELETE FROM chicken_table WHERE a < 1 AND b != 2 OR c > 3 AND d >= 4')

		conditions = [EQ('a', 1), AND(), EQ('b', 2), OR(), LTE('c', 3), AND(), LT('d', 4)]
		self.assertEqual(delete('chicken_table', conditions), 'DELETE FROM chicken_table WHERE a = 1 AND b = 2 OR c <= 3 AND d < 4')

	def test_update(self):
		conditions = [EQ('a', 1), AND(), EQ('b', 2), OR(), EQ('c', 3)]
		field_value = {'a': 1, 'b': 2, 'c': 3}
		self.assertEqual(update('chicken_table', field_value, conditions), 'UPDATE chicken_table SET a = 1, b = 2, c = 3 WHERE a = 1 AND b = 2 OR c = 3')

		conditions = [LT('a', 1), AND(), NEQ('b', 2), OR(), GT('c', 3), AND(), GTE('d', 4)]
		field_value = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
		self.assertEqual(update('chicken_table', field_value, conditions), 'UPDATE chicken_table SET a = 1, b = 2, c = 3, d = 4 WHERE a < 1 AND b != 2 OR c > 3 AND d >= 4')

		conditions = [EQ('a', 1), AND(), EQ('b', 2), OR(), LTE('c', 3), AND(), LT('d', 4)]
		field_value = {'a': 1, 'b': 2, 'c': 3}
		self.assertEqual(update('chicken_table', field_value, conditions), 'UPDATE chicken_table SET a = 1, b = 2, c = 3 WHERE a = 1 AND b = 2 OR c <= 3 AND d < 4')

	def test_select(self):
		self.assertEqual(select('chicken_table'), 'SELECT * FROM chicken_table')

		self.assertEqual(select('chicken_table', conditions=[EQ('a', 1), AND(), EQ('b', 2), OR(), EQ('c', 3)]), 'SELECT * FROM chicken_table WHERE a = 1 AND b = 2 OR c = 3')
		
