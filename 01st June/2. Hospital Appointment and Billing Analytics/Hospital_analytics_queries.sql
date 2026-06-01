use retail_capstone2_db;

-- Part 1: Basic Queries (1-10)
select * from patients;
select * from doctors;
select * from patients where city='Hyderabad';
select d.* from doctors d join departments dp 
	on d.department_id=dp.department_id where 
    dp.department_name='Cardiology';
select * from appointments where appointment_date>'2026-01-01';
select * from appointments where appointment_status='Cancelled';
select * from bills where total_amount>5000;
select * from payments where payment_mode='UPI';
select * from patients where age between 30 and 50;
select * from doctors where consultation_fee>800;

-- Part 2: Aggregate Queries (11-20)
select count(*) as TotalPatients from patients;
select count(*) as TotalDoctors from doctors;
select count(*) as TotalAppointments from appointments;
select avg(consultation_fee) as AverageConsultationFee from doctors;
select max(treatment_cost) as HighestTreatmentCost from treatments;
select sum(total_amount) as TotalBillAmount from bills;
select sum(paid_amount) as TotalPaidAmount from payments;
select city, count(*) as TotalPatients from patients group by city;
select specialization, count(*) as TotalDoctors from doctors group by specialization;
select appointment_status, count(*) as TotalAppointments from 
	appointments group by appointment_status;

-- Part 3: Joins (21-27)
select p.patient_name, a.appointment_date, a.appointment_status from patients p
	inner join appointments a on p.patient_id=a.patient_id;
select d.doctor_name, dp.department_name from doctors d 
	inner join departments dp on d.department_id=dp.department_id;
select p.patient_name, d.doctor_name, a.appointment_date from appointments a
	join patients p on a.patient_id = p.patient_id
	join doctors d on a.doctor_id = d.doctor_id;
select a.appointment_id, t.treatment_name, t.treatment_cost from appointments a
	inner join treatments t on a.appointment_id=t.appointment_id;
select b.bill_id, p.patient_name, b.total_amount from bills b
	inner join patients p on b.patient_id=p.patient_id;
select b.bill_id, p.payment_mode, p.paid_amount, p.payment_status from bills b
	inner join payments p on b.bill_id=p.bill_id;
select p.patient_name, d.doctor_name, dp.department_name, a.appointment_date,
	a.appointment_status, t.treatment_name, t.treatment_cost, b.total_amount, py.payment_status 
    from appointments a join patients p on a.patient_id=p.patient_id 
    join doctors d on a.doctor_id=d.doctor_id
    join departments dp on d.department_id=dp.department_id
    left join treatments t on a.appointment_id=t.appointment_id
    left join bills b on a.appointment_id=b.appointment_id
    left join payments py on b.bill_id=py.bill_id;
    
-- Part 4: Group by and Having (28-35)
select doctor_id, count(*) as TotalAppointments 
	from appointments group by doctor_id;
select dp.department_name, count(*) as TotalAppointments from appointments a 
	join doctors d on a.doctor_id=d.doctor_id
    join departments dp on d.department_id=dp.department_id
    group by dp.department_name;
select dp.department_name, count(b.total_amount) as Revenue from bills b
	join appointments a on b.appointment_id=a.appointment_id
    join doctors d on a.doctor_id=d.doctor_id
    join departments dp on d.department_id=dp.department_id
    group by dp.department_name;
select treatment_name, sum(treatment_cost) as TotalCost 
	from treatments group by treatment_name;
select p.city, sum(b.total_amount) as TotalBilling from patients p
	join bills b on p.patient_id=b.patient_id group by city;
select doctor_id, count(*) as TotalAppointments from appointments a
	group by doctor_id having count(*)>2;
select dp.department_name, sum(b.total_amount) as Revenue from bills b
	join appointments a on b.appointment_id=a.appointment_id
    join doctors d on a.doctor_id=d.doctor_id
    join departments dp on d.department_id=dp.department_id
    group by dp.department_name having sum(b.total_amount)>20000;
select city, count(*) as TotalPatients from patients 
	group by city having count(*)>2;

-- Part 5: Subqueries (36-45)
select * from patients where patient_id in (select patient_id from appointments);
select * from patients where patient_id not in (select patient_id from appointments);
select * from doctors where doctor_id not in (select doctor_id from appointments);
select * from bills where total_amount > (select avg(total_amount) from bills);
select * from bills where total_amount = (select max(total_amount) from bills);
select * from doctors where consultation_fee > (select avg(consultation_fee) from doctors);
select distinct p.* from patients p join appointments a
	on p.patient_id=a.patient_id join doctors d
    on a.doctor_id=d.doctor_id join departments dp 
    on d.department_id=dp.department_id 
    where dp.department_name='Cardiology';
select * from bills where bill_id not in (select bill_id from bills where bill_status='Paid');
select * from appointments where appointment_id in (select appointment_id from treatments);
select patient_id, sum(total_amount) as TotalBill from bills
	group by patient_id having sum(total_amount) > 
    (select avg(patient_total) from 
    (select sum(total_amount) as patient_total from bills group by patient_id)x);

-- Part 6: Data Quality Checks (46-52)
select * from appointments where appointment_id not in
	(select appointment_id from treatments);
select b.* from bills b left join payments p on 
	b.bill_id=p.bill_id where p.bill_id is null;
select * from payments where paid_amount is null or paid_amount=0;
select a.appointment_id, a.appointment_status, b.bill_id from appointments a
	join bills b on a.appointment_id=b.appointment_id
    where a.appointment_status='Cancelled';
select b.bill_id, b.total_amount, p.paid_amount from bills b
	join payments p on b.bill_id=p.bill_id where
    p.payment_status='Paid' and p.paid_amount<b.total_amount;
select d.* from doctors d left join departments dp on
	d.department_id=dp.department_id where dp.department_id is null;
select a.* from appointments a left join patients p
	on a.patient_id=p.patient_id left join doctors d
    on a.doctor_id=d.doctor_id 
    where p.patient_id is null or d.doctor_id is null;

-- Final Reports 
-- Report 1: Patient Billing Report
select p.patient_name as Patient_Name, p.city as City,
	count(distinct a.appointment_id) as Total_Appointments,
    coalesce(sum(b.total_amount), 0) as Total_Bill_Amount,
    coalesce(sum(py.paid_amount), 0) as Total_Paid_Amount,
    coalesce(sum(b.total_amount), 0) - coalesce(sum(py.paid_amount), 0) as Pending_Amount
    from patients p left join appointments a on
    p.patient_id=a.patient_id left join bills b on
    a.appointment_id=b.appointment_id left join payments py on
    b.bill_id=py.bill_id group by p.patient_id, p.patient_name, p.city
    order by Total_Bill_Amount DESC;