use retail_capstone_db;

-- Inserting data into the tables
INSERT INTO customers VALUES
(1001,'Rahul Sharma','Hyderabad','Telangana','Male','Gold'),
(1002,'Priya Nair','Chennai','Tamil Nadu','Female','Silver'),
(1003,'Arjun Reddy','Hyderabad','Telangana','Male','Platinum'),
(1004,'Sneha Kapoor','Mumbai','Maharashtra','Female','Gold'),
(1005,'Vikram Singh','Delhi','Delhi','Male','Bronze'),
(1006,'Ananya Das','Bangalore','Karnataka','Female','Gold'),
(1007,'Karthik Raj','Chennai','Tamil Nadu','Male','Silver'),
(1008,'Meera Iyer','Pune','Maharashtra','Female','Platinum'),
(1009,'Rohit Gupta','Delhi','Delhi','Male','Silver'),
(1010,'Divya Sharma','Hyderabad','Telangana','Female','Gold');

INSERT INTO products VALUES
(2001,'iPhone 15','Electronics',79999),
(2002,'Samsung Galaxy S24','Electronics',69999),
(2003,'Boat Rockerz 550','Electronics',2499),
(2004,'Nike Running Shoes','Fashion',4999),
(2005,'Levis Jeans','Fashion',2999),
(2006,'Wooden Study Table','Furniture',8999),
(2007,'Office Chair','Furniture',5499),
(2008,'LG Washing Machine','Home Appliances',25999),
(2009,'Philips Mixer Grinder','Home Appliances',3499),
(2010,'Puma T-Shirt','Fashion',1299);
INSERT INTO orders VALUES
(3001,1001,'2026-01-05','Completed'),
(3002,1002,'2026-01-08','Completed'),
(3003,1003,'2026-01-10','Completed'),
(3004,1004,'2026-01-12','Cancelled'),
(3005,1005,'2026-01-15','Completed'),
(3006,1006,'2026-01-18','Pending'),
(3007,1001,'2026-01-22','Completed'),
(3008,1007,'2026-01-25','Completed'),
(3009,1008,'2026-01-28','Completed'),
(3010,1009,'2026-02-01','Cancelled'),
(3011,1010,'2026-02-05','Completed'),
(3012,1003,'2026-02-10','Completed'),
(3013,1004,'2026-02-14','Pending'),
(3014,1005,'2026-02-20','Completed'),
(3015,1001,'2026-02-25','Completed');

INSERT INTO order_items VALUES
(4001,3001,2001,1),
(4002,3001,2003,2),
(4003,3002,2004,1),
(4004,3002,2010,2),
(4005,3003,2008,1),
(4006,3003,2009,1),
(4007,3004,2005,1),
(4008,3005,2006,1),
(4009,3005,2007,1),
(4010,3006,2002,1),
(4011,3007,2003,3),
(4012,3007,2004,1),
(4013,3008,2010,4),
(4014,3009,2008,1),
(4015,3010,2005,2),
(4016,3011,2001,1),
(4017,3012,2003,2),
(4018,3013,2007,1),
(4019,3014,2004,2),
(4020,3015,2009,3);

INSERT INTO payments VALUES
(5001,3001,'UPI','Successful',84997),
(5002,3002,'Credit Card','Successful',7597),
(5003,3003,'Net Banking','Successful',29498),
(5004,3004,'Wallet','Successful',2999),
(5005,3005,'Debit Card','Successful',14498),
(5006,3006,'UPI','Pending',69999),
(5007,3007,'UPI','Successful',12496),
(5008,3008,'Credit Card','Successful',5196),
(5009,3009,'Net Banking','Successful',25999),
(5010,3010,'UPI','Failed',5998),
(5011,3011,'Debit Card','Successful',79999),
(5012,3012,'Wallet','Successful',4998),
(5013,3013,'UPI','Pending',5499),
(5014,3014,'Credit Card','Successful',9998),
(5015,3015,'Net Banking','Successful',10497);

INSERT INTO deliveries VALUES
(6001,3001,'BlueDart','Delivered','Hyderabad'),
(6002,3002,'Delhivery','Delivered','Chennai'),
(6003,3003,'Ekart','Delivered','Hyderabad'),
(6004,3004,'BlueDart','Cancelled','Mumbai'),
(6005,3005,'Delhivery','Delivered','Delhi'),
(6006,3006,'Ekart','Pending','Bangalore'),
(6007,3007,'BlueDart','Delivered','Hyderabad'),
(6008,3008,'Delhivery','Delivered','Chennai'),
(6009,3009,'Ekart','In Transit','Pune'),
(6010,3010,'BlueDart','Pending','Delhi'),
(6011,3011,'Delhivery','Delivered','Hyderabad'),
(6012,3012,'Ekart','Delivered','Hyderabad'),
(6013,3013,'BlueDart','Pending','Mumbai'),
(6014,3014,'Delhivery','Delivered','Delhi'),
(6015,3015,'Ekart','Delivered','Hyderabad');