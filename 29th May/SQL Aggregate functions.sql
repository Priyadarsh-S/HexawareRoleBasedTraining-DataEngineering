create table products
(
	product_id int primary key,
    product_name varchar(100),
    category varchar(50),
    price decimal(10,2),
    stock_quantity int,
    supplier_city varchar(50)
);
insert into products values
(1, 'Laptop', 'Electronics', 55000, 10, 'Hyderabad'),
(2, 'Tablet', 'Electronics', 35000, 6, 'Pune');
select * from products;
update products set product_name='Phone' where product_id=2;
delete from products where product_id=2;
select * from products;

truncate table products;
select * from products;
INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,10,'Hyderabad'),
(2,'Mobile','Electronics',25000,25,'Bangalore'),
(3,'Printer','Electronics',18000,8,'Pune'),
(4,'Office Chair','Furniture',7500,15,'Mumbai'),
(5,'Desk','Furniture',12000,5,'Chennai'),
(6,'Notebook','Stationery',80,200,'Hyderabad'),
(7,'Pen','Stationery',20,500,'Delhi'),
(8,'Water Bottle','Accessories',500,50,'Bangalore');
select product_name, price from products;
select distinct category from products;
select * from products where category='Electronics';
select * from products where price>10000;
select * from products where stock_quantity<20;
select * from products where category='Electronics' AND price>20000;
select * from products where supplier_city='Hyderabad' OR supplier_city='Bangalore';
select * from products where not category='Electronics';
select * from products where supplier_city in ('Hyderabad', 'Delhi');
select * from products where price between 500 and 20000;
select * from products where product_name like 'P%'; 
select * from products where product_name like '%K'; 
select * from products where product_name like '%top%'; 
select product_name as Product,
	price as ProductPrice from products;
select * from products order by price desc;
select count(*) from products;
select count(*) from products where category='Electronics';
select sum(price) from products;
select count(*) as TotalProducts,
	sum(price) as TotalPrice,
    avg(price) as AveragePrice,
    max(price) as HighestPrice,
    min(price) as LowestPrice from products;
select category, count(*) as ProductCount from products group by category;
select category, sum(price) as TotalPrice from products group by category;
