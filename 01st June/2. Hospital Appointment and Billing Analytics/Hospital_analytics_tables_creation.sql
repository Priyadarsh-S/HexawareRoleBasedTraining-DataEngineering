create database retail_capstone2_db;
use retail_capstone2_db;

-- Tables Creation
CREATE TABLE patients 
( 
    patient_id INT PRIMARY KEY, 
    patient_name VARCHAR(100),
    gender VARCHAR(10), 
    age INT, 
    city VARCHAR(50), 
    phone VARCHAR(15) 
); 

CREATE TABLE departments 
( 
    department_id INT PRIMARY KEY, 
    department_name VARCHAR(100) 
);

CREATE TABLE doctors 
( 
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100), 
    specialization VARCHAR(100), 
    department_id INT, 
    consultation_fee DECIMAL(10,2) 
);

CREATE TABLE appointments 
( 
    appointment_id INT PRIMARY KEY,
    patient_id INT, 
    doctor_id INT, 
    appointment_date DATE, 
    appointment_status VARCHAR(30) 
);

CREATE TABLE treatments 
( 
    treatment_id INT PRIMARY KEY, 
    appointment_id INT, 
    treatment_name VARCHAR(100), 
    treatment_cost DECIMAL(10,2) 
);

CREATE TABLE bills 
( 
    bill_id INT PRIMARY KEY, 
    patient_id INT, 
    appointment_id INT, 
    bill_date DATE, 
    total_amount DECIMAL(10,2), 
    bill_status VARCHAR(30) 
);

CREATE TABLE payments 
( 
    payment_id INT PRIMARY KEY, 
    bill_id INT, 
    payment_mode VARCHAR(30), 
    paid_amount DECIMAL(10,2),
    payment_status VARCHAR(30) 
); 