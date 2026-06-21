-- Database Creation
create database supply_chain_db;
use supply_chain_db;

-- Table Creation (Orders, Suppliers, Inventory)
create table suppliers(
	supplier_id int auto_increment primary key,
    supplier_name varchar(100) not null,
    email varchar(100),
    country varchar(50)
);

create table inventory(
	item_id int auto_increment primary key,
    item_name varchar(100) not null,
    stock_level int not null default 0,
    reorder_point int not null default 10,
    supplier_id int,
    foreign key (item_id) references suppliers(supplier_id)
);

create table orders(
	order_id int auto_increment primary key,
    item_id int,
    quantity int not null,
    order_date timestamp default current_timestamp,
    status varchar(50) default 'Pending',
    foreign key (item_id) references inventory(item_id)
);

-- Basic CRUD Operations
-- Inserting data into tables
insert into suppliers (supplier_name, email, country) values
('Global Logistics Corp', 'contact@globallogistics.com', 'USA'),
('Apex Tech Manufacturing', 'sales@apextech.com', 'Germany'),
('Nippon Component Industries', 'support@nipponci.jp', 'Japan'),
('EuroParts Logistics', 'info@europarts.eu', 'France'),
('Pacific Assembly Labs', 'orders@pacificlabs.tw', 'Taiwan');

insert into inventory (item_name, stock_level, reorder_point, supplier_id) values
('Microchips Type-A', 120, 30, 5),
('Aluminium Casings', 85, 20, 1),
('Lithium Battery Packs', 14, 25, 2), 
('Copper Wiring Reels', 200, 40, 3),  
('Fiber Optic Transceivers', 9, 15, 4);

insert into orders (item_id, quantity, status) values
(1, 50, 'Delivered'),
(3, 30, 'Shipped'),
(2, 10, 'Pending'),
(5, 15, 'Processing'),
(4, 100, 'Delivered');

select * from suppliers;
select * from inventory;
select * from orders;

update inventory set stock_level = 150 where item_id = 1;
update orders set status = 'Shipped' where order_id = 3;
select * from inventory where item_id =1;
select * from orders where order_id =3;

insert into suppliers (supplier_name, email, country) 
values ('Discontinued Supplier Ltd', 'obsolete@supplier.com', 'UK'); 
insert into inventory (item_name, stock_level, reorder_point, supplier_id) 
values ('Legacy Cable Cord', 0, 0, 6);

-- Deleting the recently inserted values
set sql_safe_updates = 0;
delete from inventory where item_name = 'Legacy Cable Cord';
delete from suppliers where supplier_name = 'Discontinued Supplier Ltd';
set sql_safe_updates = 1;

-- Stored Procedure for Reorder
delimiter $$
create procedure AutoReorderCheck(in p_item_id int, in p_order_qty int)
begin
	declare v_current_stock int;
    declare v_reorder_point int;
    select stock_level, reorder_point into v_current_stock, v_reorder_point
		from inventory where item_id = p_item_id;
    if v_current_stock <= v_reorder_point then
		insert into orders (item_id, quantity, status) values (p_item_id, p_order_qty*2, 'Auto-Ordered');
	end if;
end$$
delimiter ;

update inventory set stock_level = 5 where item_id = 2;
call AutoReorderCheck(2, 25);
select * from orders;