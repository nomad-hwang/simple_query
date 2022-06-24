
from query.operator import Operator

class Comparison(Operator):
	def __init__(self, field, value) -> None:
		self.field = field
		self.value = value
	
	def __str__(self) -> str:
		return f'{self.field} {self.SYMBOL} {self.value}'

class EQ(Comparison):
	SYMBOL = '='

class NEQ(Comparison):
	SYMBOL = '!='

class GT(Comparison):
	SYMBOL = '>'

class GTE(Comparison):
	SYMBOL = '>='

class LT(Comparison):
	SYMBOL = '<'

class LTE(Comparison):
	SYMBOL = '<='
