
from query.build import delete, insert, select, update  
from query.operator.comparison import EQ, GT, LT
from query.operator.logical import AND, OR

print(insert('product', {'id': 10, 'price': 10, 'stock': 30}))

print(select('product', fields=['id', 'price', 'stock'], conditions=[LT('price', 20), OR(), GT('price', 10)]))

print(update('product', field_value={'price': 20}, conditions=[EQ('id', 10)]))

print(delete('product', conditions=[EQ('id', 10)]))
