use retail_capstone_db;

-- Part 3: Basic Queries
SELECT * FROM customers;
SELECT customer_name, city, membership_type FROM customers;
SELECT * FROM products ORDER BY price DESC;
SELECT * FROM customers WHERE city='Hyderabad';
SELECT * FROM customers WHERE membership_type='Gold';
SELECT * FROM products WHERE price BETWEEN 500 AND 5000;
SELECT * FROM products WHERE category IN ('Electronics', 'Fashion');
SELECT * FROM orders WHERE order_date>'2026-01-01';
SELECT * FROM payments WHERE payment_mode='UPI'; 
SELECT * FROM deliveries WHERE delivery_status='Pending';

-- Part 4: Aggregate Queries
SELECT COUNT(*) AS TotalCustomers FROM customers;
SELECT COUNT(*) AS TotalOrders FROM orders;
SELECT COUNT(*) AS TotalProducts FROM products;
SELECT SUM(amount) AS TotalRevenue FROM payments WHERE payment_status='Successful';
SELECT AVG(amount) AS AveragePayment FROM payments;
SELECT MAX(amount) AS HighestPayment FROM payments;
SELECT MIN(amount) AS LowestPayment FROM payments;
SELECT city, COUNT(customer_id) AS TotalCustomers FROM customers GROUP BY city;
SELECT category, COUNT(*) AS TotalProducts FROM products GROUP BY category;
SELECT order_status, COUNT(*) AS TotalOrders FROM orders GROUP BY order_status;

-- Part 5: Joins
SELECT c.customer_name, o.order_id, o.order_date FROM customers c INNER JOIN
	orders o ON c.customer_id=o.customer_id;
SELECT oi.order_id, p.product_name, oi.quantity, p.price FROM order_items oi
	INNER JOIN products p ON oi.product_id=p.product_id;
SELECT c.customer_name, p.product_name, oi.quantity, o.order_date FROM customers c
	JOIN orders o ON c.customer_id=o.customer_id
    JOIN order_items oi ON o.order_id=oi.order_id
    JOIN products p ON oi.product_id=p.product_id;
SELECT o.order_id, p.payment_mode, p.payment_status, p.amount FROM orders o
	INNER JOIN payments p ON o.order_id=p.order_id;
SELECT o.order_id, d.delivery_partner, delivery_status FROM orders o
	INNER JOIN deliveries d ON o.order_id=d.order_id;
SELECT c.customer_name, c.city, o.order_id, o.order_date, p.product_name, p.category,
	oi.quantity, p.price, py.payment_status, d.delivery_status FROM customers c
    JOIN orders o ON c.customer_id=o.customer_id
    JOIN order_items oi ON o.order_id=oi.order_id
    JOIN products p ON oi.product_id=p.product_id
    JOIN payments py ON o.order_id=py.order_id
    JOIN deliveries d ON o.order_id=d.order_id;
    
-- Part 6: Group by and Having
SELECT c.city, SUM(py.amount) AS Revenue FROM customers c JOIN
	orders o ON c.customer_id=o.customer_id JOIN
    payments py ON o.order_id=py.order_id WHERE
    py.payment_status='Successful' GROUP BY c.city;
SELECT c.customer_name, SUM(py.amount) AS Revenue FROM customers c JOIN
	orders o ON c.customer_id=o.customer_id JOIN
    payments py ON o.order_id=py.order_id WHERE
    py.payment_status='Successful' GROUP BY c.customer_name;
SELECT p.product_name, SUM(oi.quantity) AS QuantitySold FROM products p
	JOIN order_items oi ON p.product_id=oi.product_id GROUP BY p.product_name;
SELECT p.category, SUM(oi.quantity*p.price) AS Revenue FROM products p
	JOIN order_items oi ON p.product_id=oi.product_id GROUP BY p.category;
SELECT c.customer_name, COUNT(o.order_id) AS TotalOrders FROM customers c
	JOIN orders o ON c.customer_id=o.customer_id GROUP BY c.customer_name;
SELECT c.customer_name, COUNT(o.order_id) AS TotalOrders FROM customers c
	JOIN orders o ON c.customer_id=o.customer_id GROUP BY c.customer_name HAVING COUNT(o.order_id)>1;
SELECT p.category, SUM(oi.quantity*p.price) AS Revenue FROM products p
	JOIN order_items oi ON p.product_id=oi.product_id 
    GROUP BY p.category HAVING Revenue>10000;
SELECT city, COUNT(customer_id) AS TotalCustomers FROM customers 
	GROUP BY city HAVING COUNT(customer_id)>2;
SELECT p.product_name, SUM(oi.quantity) AS TotalQuantity FROM products p
	JOIN order_items oi ON p.product_id=oi.product_id 
    GROUP BY p.product_name HAVING TotalQuantity>3;
    
-- Part 7: Subqueries
SELECT * FROM customers WHERE customer_id IN 
	(SELECT customer_id FROM orders);
SELECT * FROM customers WHERE customer_id NOT IN 
	(SELECT customer_id FROM orders);
SELECT * FROM products WHERE product_id NOT IN 
	(SELECT product_id FROM order_items);
SELECT * FROM payments WHERE amount>(SELECT AVG(amount) FROM payments);
SELECT c.customer_name FROM customers c JOIN orders o 
	ON c.customer_id=o.customer_id JOIN payments p ON o.order_id=p.order_id
	WHERE p.amount=(SELECT MAX(amount) FROM payments);
SELECT * FROM products WHERE price>(SELECT AVG(price) FROM products);
SELECT DISTINCT c.* FROM customers c JOIN orders o ON 
	c.customer_id = o.customer_id JOIN order_items oi ON 
    o.order_id = oi.order_id JOIN products p ON 
    oi.product_id = p.product_id WHERE p.category = 'Electronics';
SELECT * FROM orders WHERE order_id IN 
	(SELECT order_id FROM payments WHERE payment_status='Successful');
SELECT * FROM orders WHERE order_id NOT IN 
	(SELECT order_id FROM deliveries WHERE delivery_status='Delivered');
SELECT c.customer_name, SUM(p.amount) AS TotalSpending FROm customers c JOIN
	orders o ON c.customer_id = o.customer_id JOIN payments p
    ON o.order_id = p.order_id GROUP BY c.customer_id, c.customer_name
    HAVING SUM(p.amount) > (SELECT AVG(TotalSpending) FROM 
    (SELECT SUM(amount) AS TotalSpending FROM orders o JOIN payments p
    ON o.order_id = p.order_id GROUP BY o.customer_id)x);
    
-- Part 8: Data Quality Checks
SELECT o.* FROM orders o LEFT JOIN payments p
	ON o.order_id = p.order_id WHERE p.order_id IS NULL;
SELECT o.* FROM orders o LEFT JOIN deliveries d
	ON o.order_id = d.order_id WHERE d.order_id IS NULL;
SELECT * FROM payments WHERE amount IS NULL OR amount=0;
SELECT o.*, p.payment_status FROM orders o JOIN payments p ON 
	o.order_id = p.order_id WHERE o.order_status = 'Cancelled' 
    AND p.payment_status = 'Successful';
SELECT o.order_id, d.delivery_status, p.payment_status FROM orders o
	JOIN deliveries d ON o.order_id = d.order_id JOIN payments p 
    ON o.order_id = p.order_id WHERE d.delivery_status = 'Delivered'
	AND p.payment_status = 'Failed';
SELECT oi.* FROM order_items oi LEFT JOIN products p ON
	oi.product_id=p.product_id WHERE p.product_id IS NULL;
SELECT o.* FROM orders o LEFT JOIN customers c ON 
	o.customer_id = c.customer_id WHERE c.customer_id IS NULL;