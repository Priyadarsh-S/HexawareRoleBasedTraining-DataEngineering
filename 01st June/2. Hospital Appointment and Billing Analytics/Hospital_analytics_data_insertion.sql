use retail_capstone2_db;

-- Inserting data into the tables
INSERT INTO patients VALUES
(301,'Rahul Sharma','Male',45,'Hyderabad','9876543210'),
(302,'Priya Nair','Female',32,'Chennai','9876543211'),
(303,'Arun Kumar','Male',55,'Hyderabad','9876543212'),
(304,'Sneha Kapoor','Female',29,'Mumbai','9876543213'),
(305,'Vikram Singh','Male',40,'Delhi','9876543214'),
(306,'Meera Iyer','Female',36,'Bangalore','9876543215'),
(307,'Rohit Gupta','Male',50,'Hyderabad','9876543216'),
(308,'Ananya Das','Female',27,'Chennai','9876543217'),
(309,'Karan Mehta','Male',60,'Pune','9876543218'),
(310,'Divya Sharma','Female',42,'Delhi','9876543219'),
(311,'Suresh Babu','Male',38,'Hyderabad','9876543220'),
(312,'Nisha Reddy','Female',33,'Bangalore','9876543221');

INSERT INTO departments VALUES
(101,'Cardiology'),
(102,'Neurology'),
(103,'Orthopedics'),
(104,'General Medicine'),
(105,'Pediatrics');

INSERT INTO doctors VALUES
(201,'Dr. Rajesh Kumar','Cardiologist',101,1200),
(202,'Dr. Priya Sharma','Neurologist',102,1500),
(203,'Dr. Arjun Reddy','Orthopedic Surgeon',103,1000),
(204,'Dr. Meena Iyer','General Physician',104,700),
(205,'Dr. Karthik Rao','Pediatrician',105,800),
(206,'Dr. Sneha Gupta','Cardiologist',101,1300),
(207,'Dr. Vikram Singh','Neurologist',102,1400),
(208,'Dr. Anjali Das','General Physician',104,750);

INSERT INTO appointments VALUES
(401,301,201,'2026-01-05','Completed'),
(402,302,204,'2026-01-06','Completed'),
(403,303,201,'2026-01-08','Completed'),
(404,304,203,'2026-01-10','Completed'),
(405,305,202,'2026-01-12','Completed'),
(406,306,205,'2026-01-15','Completed'),
(407,307,206,'2026-01-18','Completed'),
(408,308,204,'2026-01-20','Cancelled'),
(409,309,203,'2026-01-22','Completed'),
(410,310,207,'2026-01-25','Completed'),
(411,311,201,'2026-01-28','Completed'),
(412,312,208,'2026-02-01','Completed'),
(413,301,202,'2026-02-03','Completed'),
(414,302,205,'2026-02-05','Completed'),
(415,303,203,'2026-02-07','Completed'),
(416,304,204,'2026-02-10','Pending'),
(417,305,206,'2026-02-12','Completed'),
(418,306,201,'2026-02-15','Completed'),
(419,307,202,'2026-02-18','Cancelled'),
(420,308,205,'2026-02-20','Completed');

INSERT INTO treatments VALUES
(501,401,'ECG',2000),
(502,402,'General Checkup',800),
(503,403,'Angiography',12000),
(504,404,'Fracture Treatment',7000),
(505,405,'Brain Scan',9000),
(506,406,'Vaccination',1500),
(507,407,'Heart Screening',5000),
(508,409,'Knee Treatment',6500),
(509,410,'Neurological Test',8500),
(510,411,'ECG',2000),
(511,412,'General Checkup',800),
(512,413,'Brain Scan',9000),
(513,414,'Vaccination',1500),
(514,415,'Physiotherapy',3000),
(515,417,'Heart Screening',5000);

INSERT INTO bills VALUES
(601,301,401,'2026-01-05',3200,'Paid'),
(602,302,402,'2026-01-06',1500,'Paid'),
(603,303,403,'2026-01-08',13200,'Paid'),
(604,304,404,'2026-01-10',8000,'Paid'),
(605,305,405,'2026-01-12',10500,'Paid'),
(606,306,406,'2026-01-15',2300,'Paid'),
(607,307,407,'2026-01-18',6300,'Paid'),
(608,309,409,'2026-01-22',7500,'Paid'),
(609,310,410,'2026-01-25',9900,'Paid'),
(610,311,411,'2026-01-28',3200,'Paid'),
(611,312,412,'2026-02-01',1550,'Pending'),
(612,301,413,'2026-02-03',10500,'Paid'),
(613,302,414,'2026-02-05',2300,'Paid'),
(614,303,415,'2026-02-07',4000,'Paid'),
(615,305,417,'2026-02-12',6500,'Pending');

INSERT INTO payments VALUES
(701,601,'UPI',3200,'Paid'),
(702,602,'Credit Card',1500,'Paid'),
(703,603,'Net Banking',13200,'Paid'),
(704,604,'UPI',8000,'Paid'),
(705,605,'Debit Card',10500,'Paid'),
(706,606,'UPI',2300,'Paid'),
(707,607,'Credit Card',6300,'Paid'),
(708,608,'UPI',7500,'Paid'),
(709,609,'Net Banking',9900,'Paid'),
(710,610,'Debit Card',3200,'Paid'),
(711,611,'UPI',0,'Pending'),
(712,612,'Credit Card',10500,'Paid'),
(713,613,'UPI',2300,'Paid'),
(714,614,'Net Banking',4000,'Paid'),
(715,615,'UPI',3000,'Partial');