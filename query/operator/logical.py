
from query.operator import Operator

class Logical(Operator):	
	def __str__(self) -> str:
		return f'{self.SYMBOL}'

class AND(Logical):
	SYMBOL = 'AND'

class OR(Logical):
	SYMBOL = 'OR'
