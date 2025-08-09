import pymysql

conn = pymysql.connect(
        host="localhost",
        user="root",
        password="mkkapri"
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS workplacedb")
cursor.execute("USE workplacedb")

staff_table = """
        CREATE TABLE IF NOT EXISTS staff (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            address TEXT,
            dob DATE,
            contact VARCHAR(20),
            emergency_contact VARCHAR(20),
            account_number VARCHAR(50),
            ird_number VARCHAR(20),
            account_name VARCHAR(100),
            bank_name VARCHAR(100),
            position VARCHAR(100),
            work_type VARCHAR(50),
            pay_rate DECIMAL(10,2),
            department VARCHAR(100),
            work_email VARCHAR(100)
        )
        """
cursor.execute(staff_table)

staff_attendance_table = """
CREATE TABLE IF NOT EXISTS staff_attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late', 'Sick', 'Leave') DEFAULT 'Present',
    remarks TEXT,
    FOREIGN KEY (staff_id) REFERENCES staff(id)
)
"""
cursor.execute(staff_attendance_table)

staff_salary_table = """
CREATE TABLE IF NOT EXISTS statement (
    statement INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT NOT NULL,
    payment_date DATE NOT NULL,
    gross_pay DECIMAL(10, 2) NOT NULL,
    tax_deductions DECIMAL(10, 2),
    net_pay DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50),
    remarks TEXT,
    FOREIGN KEY (staff_id) REFERENCES staff(id)
)
"""
cursor.execute(staff_salary_table)

staff_task_table = """
create table if not exists staff_task(
    task_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    staff_id INT NOT NULL,
    assigned_date DATE NOT NULL,
    due_date DATE NOT NULL,
    task_title VARCHAR(100) NOT NULL,
    task_details VARCHAR(500) NOT NULL, 
    status VARCHAR(20) DEFAULT 'pending',
    FOREIGN KEY (staff_id) REFERENCES staff(id)
    )
"""
cursor.execute(staff_task_table)

cursor.close()
conn.close()