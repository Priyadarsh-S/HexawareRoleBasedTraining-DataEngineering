create database retail_capstone_db;
use retail_capstone_db;

-- 1. Customers
CREATE TABLE customers 
( 
    customer_id INT PRIMARY KEY, 
    customer_name VARCHAR(100), 
    city VARCHAR(50), 
    state VARCHAR(50), 
    gender VARCHAR(10), 
    membership_type VARCHAR(30) 
);

-- 2. Products
CREATE TABLE products 
( 
    product_id INT PRIMARY KEY, 
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2) 
);

-- 3. Orders
CREATE TABLE orders 
( 
    order_id INT PRIMARY KEY, 
    customer_id INT, 
    order_date DATE, 
    order_status VARCHAR(30) ,
    CONSTRAINT fk_orders_customer
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 4. Order_items
CREATE TABLE order_items 
( 
    item_id INT PRIMARY KEY, 
    order_id INT, 
    product_id INT, 
    quantity INT,
    CONSTRAINT fk_orderitems_order
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT fk_orderitems_product
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 5. Payments
CREATE TABLE payments 
( 
    payment_id INT PRIMARY KEY, 
    order_id INT, 
    payment_mode VARCHAR(30), 
    payment_status VARCHAR(30), 
    amount DECIMAL(10,2),
    CONSTRAINT fk_payments_order
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- 6. Deliveries
CREATE TABLE deliveries 
( 
    delivery_id INT PRIMARY KEY, 
    order_id INT, 
    delivery_partner VARCHAR(50), 
    delivery_status VARCHAR(30), 
    delivery_city VARCHAR(50),
    CONSTRAINT fk_deliveries_order
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);