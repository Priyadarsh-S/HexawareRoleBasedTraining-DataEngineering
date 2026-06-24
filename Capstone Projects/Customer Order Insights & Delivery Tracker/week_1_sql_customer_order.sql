-- Database Creation
create database customer_insights_db;
use customer_insights_db;

-- Table Creation (Customers, Orders, Delivery Status)
create table customers(
	customer_id int auto_increment primary key,
    customer_name varchar(100) not null,
    email varchar(100),
    region varchar(50)
);  

create table orders(
	order_id int auto_increment primary key,
    customer_id int,
    item_name varchar(100) not null,
    order_amount decimal(10,2),
    order_date timestamp default current_timestamp,
    foreign key (customer_id) references customers(customer_id)
);

create table delivery_status(
	delivery_id int auto_increment primary key,
    order_id int,
    delivery_date datetime,
    status varchar(50) default 'Pending',
    delivery_issue varchar(150) default 'None',
    foreign key (order_id) references orders(order_id)
);

-- Basic CRUD Operations
-- Inserting data into tables
insert into customers (customer_name, email, region) values
('Alice Smith', 'alice@gmail.com', 'North'),
('Bob Jones', 'bob@yahoo.com', 'South'),
('Charlie Brown', 'charlie@gmail.com', 'East'),
('Diana Prince', 'diana@amazon.com', 'West'),
('Evan Wright', 'evan@outlook.com', 'North');

insert into orders (customer_id, item_name, order_amount, order_date) values
(1, 'Wireless Headphones', 99.99, '2026-06-10 10:00:00'),
(2, 'Ergonomic Chair', 249.50, '2026-06-12 14:30:00'),
(3, 'Mechanical Keyboard', 120.00, '2026-06-14 09:15:00'),
(4, '4K Monitor', 350.00, '2026-06-15 11:00:00'),
(5, 'USB-C Hub', 45.00, '2026-06-16 16:45:00'),
(1, 'Smartphone Case', 25.00, '2026-06-18 12:00:00');

insert into delivery_status (order_id, delivery_date, status, delivery_issue) values
(1, '2026-06-14 15:00:00', 'Delivered', 'None'),
(2, '2026-06-25 18:00:00', 'Delivered', 'Sorting Hub Delay'),
(3, '2026-06-16 11:30:00', 'Delivered', 'None'),
(4, '2026-06-26 14:00:00', 'Delivered', 'Damaged in Transit'),
(5, NULL, 'Pending', 'Weather Block'),
(6, '2026-06-20 09:00:00', 'Delivered', 'None');

select * from customers;
select * from orders;
select * from delivery_status;

update orders set order_amount = 110.00 where order_id = 1;
update customers set email = 'bobjones@yahoo.com' where customer_id = 2;

-- Deleting the recently inserted values
set sql_safe_updates = 0;
insert into orders (customer_id, item_name, order_amount) values (1, 'Temporary Item', 0.00);
delete from orders where item_name = 'Temporary Item';
set sql_safe_updates = 1;

-- Stored procedure to fetch all delayed deliveries for a customer
delimiter $$
create procedure GetDelayedDeliveriesByCustomer(in p_customer_id int)
begin
	select
		c.customer_name,
        o.order_id,
        o.item_name,
        d.delivery_date,
        d.status,
        d.delivery_issue
	from customers c
    join orders o on c.customer_id = o.customer_id
    join delivery_status d on o.order_id = d.order_id
    where c.customer_id = p_customer_id
		and (d.delivery_issue != 'None' or d.status = 'Pending');
end$$
delimiter ;

call GetDelayedDeliveriesByCustomer(2); -- For customer_id 2 Bob Jones