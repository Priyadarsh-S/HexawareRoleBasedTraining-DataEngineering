-- 1. Create Database 
CREATE DATABASE training_sql_db;
USE training_sql_db;
-- 2. Table 1: Books
CREATE TABLE books
(
	book_id INT PRIMARY KEY,
    book_title VARCHAR(100),
    category VARCHAR(50),
    author VARCHAR(50),
    price DECIMAL(10,2),
    stock INT,
    published_year INT
);
INSERT INTO books VALUES
(1, 'Python Basics', 'Programming', 'Ravi Kumar', 550, 30, 2021),
(2, 'Advanced SQL', 'Database', 'Priya Sharma', 750, 15, 2020),
(3, 'Data Engineering Guide', 'Data', 'Amit Verma', 1200, 10, 2023),
(4, 'Machine Learning Start', 'AI', 'Neha Reddy', 950, 8, 2022),
(5, 'Excel for Business', 'Business', 'Kiran Rao', 400, 50, 2019),
(6, 'Power BI Reports', 'Data', 'Sneha Patel', 850, 12, 2021),
(7, 'Java Fundamentals', 'Programming', 'Arjun Mehta', 600, 20, 2018),
(8, 'Cloud Basics', 'Cloud', 'Rahul Nair', 700, 18, 2022),
(9, 'SQL Interview Prep', 'Database', 'Farhan Ali', 500, 25, 2024),
(10, 'AI for Beginners', 'AI', 'Meera Singh', 650, 5, 2023);

-- EXERCISES (SELECT, WHERE, DISTINCT, IN, BETWEEN, LIKE, ORDER BY)
-- Exercise 1
SELECT * FROM books;

-- Exercise 2
SELECT book_title, category, price FROM books;

-- Exercise 3
SELECT DISTINCT category FROM books;

-- Exercise 4
SELECT * FROM books WHERE category='Programming';

-- Exercise 5
SELECT * FROM books WHERE price>700;

-- Exercise 6
SELECT * FROM books WHERE stock<15;

-- Exercise 7
SELECT * FROM books WHERE category IN ('Programming', 'Database', 'AI');

-- Exercise 8
SELECT * FROM books WHERE price BETWEEN 500 AND 900;

-- Exercise 9
SELECT * FROM books WHERE book_title LIKE '%SQL%';

-- Exercise 10
SELECT * FROM books WHERE book_title LIKE 'Data%';

-- Exercise 11
SELECT * FROM books ORDER BY price DESC;

-- Exercise 12
SELECT * FROM books ORDER BY category, price DESC;

-- EXERCISES (Aggregate Functions, GROUP BY, HAVING)
-- Exercise 13
SELECT COUNT(*) AS TotalBooks FROM books;

-- Exercise 14
SELECT MAX(price) AS HighestPricedBook FROM books;

-- Exercise 15
SELECT MIN(price) AS LowestPricedBook FROM books;

-- Exercise 16
SELECT AVG(price) AS AverageBookPrice FROM books;

-- Exercise 17
SELECT SUM(stock) AS TotalStock FROM books;

-- Exercise 18
SELECT category, COUNT(*) AS NumberOfBooks FROM books GROUP BY category;

-- Exercise 19
SELECT category, AVG(price) AS AveragePrice FROM books GROUP BY category;

-- Exercise 20
SELECT category, SUM(stock) AS TotalStock FROM books GROUP BY category;

-- Exercise 21
SELECT category, COUNT(*) AS NumberOfBooks FROM books GROUP BY category HAVING COUNT(*)>1;

-- Exercise 22
SELECT category, AVG(price) AS AveragePrice FROM books GROUP BY category HAVING AVG(price)>700;

-- 3. Table 2 and 3: Departments and Employees
CREATE TABLE departments
(
	department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);
CREATE TABLE employees
(
	employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10,2),
    city VARCHAR(50),
    manager_id INT
);
INSERT INTO departments VALUES 
(10, 'IT', 'Hyderabad'), 
(20, 'HR', 'Bangalore'), 
(30, 'Finance', 'Mumbai'), 
(40, 'Sales', 'Delhi'), 
(50, 'Marketing', NULL); 
INSERT INTO employees VALUES 
(101, 'Rahul Sharma', 10, 75000, 'Hyderabad', 201), 
(102, 'Priya Reddy', 10, 85000, 'Bangalore', 201), 
(103, 'Amit Kumar', 20, 55000, NULL, 202), 
(104, 'Sneha Patel', 30, 65000, 'Mumbai', 203), 
(105, 'Arjun Verma', NULL, 60000, 'Chennai', 204), 
(106, 'Neha Singh', 60, 50000, 'Delhi', NULL), 
(107, 'Farhan Ali', 40, NULL, 'Hyderabad', 205), 
(108, 'Meera Nair', 10, 90000, 'Pune', 201);

-- EXERCISES (INNER JOIN, LEFT JOIN, RIGHT JOIN)
-- Exercise 23
SELECT e.employee_name, e.salary, d.department_name, d.location FROM 
	employees e INNER JOIN departments d ON e.department_id=d.department_id; 
    
-- Exercise 24
SELECT e.employee_name, e.salary, d.department_name, d.location FROM 
	employees e LEFT JOIN departments d ON e.department_id=d.department_id;

-- Exercise 25
SELECT e.employee_name FROM employees e LEFT JOIN departments d
	ON e.department_id=d.department_id WHERE d.department_id IS NULL;
    
-- Exercise 26
SELECT d.department_name, d.location, e.employee_name FROM employees e 
	RIGHT JOIN departments d ON e.department_id=d.department_id;
    
-- Exercise 27
SELECT d.department_name FROM departments d LEFT JOIN employees e
	ON d.department_id=e.department_id WHERE e.employee_id IS NULL;
    
-- Exercise 28
SELECT employee_name FROM employees WHERE salary IS NULL;

-- Exercise 29
SELECT employee_name FROM employees WHERE city IS NULL;

-- Exercise 30
SELECT department_name FROM departments WHERE location IS NULL;

-- Exercise 31
SELECT d.department_name, COUNT(e.employee_id) AS EmployeeCount FROM departments d
	LEFT JOIN employees e ON d.department_id=e.department_id GROUP BY d.department_name;

-- Exercise 32
SELECT d.department_name, AVG(e.salary) AS AverageSalary FROM departments d
	LEFT JOIN employees e ON d.department_id=e.department_id GROUP BY d.department_name;
    
-- Exercise 33
SELECT d.department_name, COUNT(e.employee_id) AS EmployeeCount FROM departments d
	LEFT JOIN employees e ON d.department_id=e.department_id GROUP BY d.department_name HAVING COUNT(e.employee_id)>2;

-- Exercise 34
SELECT d.department_name, MAX(e.salary) AS HighestSalary FROM departments d
	LEFT JOIN employees e ON d.department_id=e.department_id GROUP BY d.department_name;

-- 4. Table 4: Customers and Payments
CREATE TABLE customers_new
(
	customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    membership_type VARCHAR(50)
);
CREATE TABLE payments
(
	payment_id INT PRIMARY KEY,
	customer_id INT,
    amount DECIMAL(10,2),
    payment_mode VARCHAR(30),
    payment_status VARCHAR(30)
);
INSERT INTO customers_new VALUES 
(1, 'Ramesh Gupta', 'Hyderabad', 'Gold'), 
(2, 'Sana Khan', 'Bangalore', 'Silver'), 
(3, 'John Mathew', 'Mumbai', 'Gold'), 
(4, 'Ayesha Begum', 'Chennai', 'Bronze'), 
(5, 'Vikram Rao', 'Delhi', 'Silver'), 
(6, 'Divya Sharma', 'Pune', NULL); 
INSERT INTO payments VALUES 
(1001, 1, 15000, 'UPI', 'Success'), 
(1002, 1, 8000, 'Card', 'Success'), 
(1003, 2, 5000, 'Cash', 'Pending'), 
(1004, 3, 22000, 'UPI', 'Success'), 
(1005, 7, 12000, 'Card', 'Failed'), 
(1006, NULL, 3000, 'Cash', 'Pending'), 
(1007, 4, NULL, 'UPI', 'Success'), 
(1008, 5, 7000, NULL, 'Success'); 

-- EXERCISES (Subqueries)
-- Excercise 35
SELECT customer_name FROM customers_new WHERE customer_id IN 
	(SELECT customer_id FROM payments WHERE customer_id IS NOT NULL);

-- Excercise 36
SELECT customer_name FROM customers_new WHERE customer_id NOT IN 
	(SELECT customer_id FROM payments WHERE customer_id IS NOT NULL);

-- Exercise 37
SELECT * FROM payments WHERE amount > (SELECT AVG(amount) FROM payments);

-- Exercise 38
SELECT customer_name FROM customers_new WHERE customer_id = 
	(SELECT customer_id FROM payments WHERE amount = (SELECT MAX(amount) FROM payments));

-- Exercise 39
SELECT customer_name FROM customers_new WHERE membership_type='Gold' AND customer_id IN 
	(SELECT customer_id FROM payments WHERE customer_id IS NOT NULL);
    
-- Exercise 40
SELECT customer_name FROM customers_new WHERE customer_id IN 
	(SELECT customer_id FROM payments GROUP BY customer_id HAVING SUM(amount)>10000);

-- Exerrcise 41
SELECT payment_id FROM payments WHERE customer_id NOT IN (SELECT customer_id FROM customers_new)
	OR customer_id IS NULL;
    
-- Exercise 42
SELECT customer_name FROM customers_new c WHERE EXISTS 
	(SELECT 1 FROM payments p WHERE p.customer_id=c.customer_id);
    
-- Exercise 43
SELECT customer_name FROM customers_new c WHERE NOT EXISTS 
	(SELECT 1 FROM payments p WHERE p.customer_id=c.customer_id);
    
-- Exercise 44
SELECT DISTINCT c.customer_name FROM customers_new c JOIN payments p ON c.customer_id=p.customer_id
	WHERE p.amount > ALL (SELECT amount FROM payments WHERE customer_id=2);