# Simple SQL query builder

Just a simple one day project

- Not tested with database yet.
- tests are in `tests` folder
- to run test, run
```
python3 -m unittest
```

- to see more about the syntax, checkout **/query/operator**

# syntaxes
- **insert**('product', {'id': 10, 'price': 10, 'stock': 30})
	- *INSERT INTO product (id, price, stock) VALUES (10, 10, 30)**
	- in **'product'** table, insert a new row with **'id' = 10, 'price' = 10, 'stock' = 30**

- **select**('product', fields=['id', 'price', 'stock'], conditions=[LT('price', 20), OR(), GT('price', 10)])
	- *SELECT id,price,stock FROM product WHERE price < 20 OR price > 10*
	- in **'product'** table, select rows with **'price < 20' 'OR' 'price > 10'**
	

- **update**('product', field_value={'price': 20}, conditions=[EQ('id', 10)])
	- *UPDATE product SET price = 20 WHERE id = 10*
	- in **'product'** table, update rows's **'price' to 20** where **'id' = 10**

- **delete**('product', conditions=[EQ('id', 10)])
	- *DELETE FROM product WHERE id = 10*
	- in **'product'** table, delete rows where **'id' = 10**