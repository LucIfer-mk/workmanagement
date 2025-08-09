# workmanagement

<b>This is my 1st year project on python and CURD operation operation, Python, and MySQL is used as tech stack</b>

# Work Management System Documentation

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Requirements](#system-requirements)
- [Installation & Setup](#installation--setup)
- [Database Schema](#database-schema)
- [Application Structure](#application-structure)
- [User Guide](#user-guide)
- [Admin Dashboard](#admin-dashboard)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Work Management System is a comprehensive desktop application built for managing staff, tracking attendance, processing payroll, and generating financial reports. This is a first-year Python project demonstrating CRUD operations with a user-friendly GUI interface.

**Project Repository:** [https://github.com/LucIfer-mk/workmanagement.git](https://github.com/LucIfer-mk/workmanagement.git)

### Key Objectives

- Streamline staff management processes
- Automate payroll calculations
- Track employee attendance
- Generate financial reports and statements
- Provide an intuitive admin interface

## Features

### 🧑‍💼 Staff Management

- ✅ Add new staff members with complete details
- ✅ Update existing staff information
- ✅ Remove staff members (with cascade deletion)
- ✅ View staff directory with contact information

### 💰 Payroll Management

- ✅ Automatic salary calculations based on hours worked
- ✅ Tax deductions (20% standard rate)
- ✅ Generate detailed payslips
- ✅ Bank account integration for payments
- ✅ IRD number tracking for tax compliance

### 📊 Reporting & Analytics

- ✅ Payment history statements
- ✅ Income vs. Expenses charts
- ✅ Budget tracking dashboard
- ✅ Financial overview cards

### ⚙️ System Administration

- ✅ Admin dashboard with navigation
- ✅ Settings management
- ✅ User authentication
- ✅ Data export capabilities

## Tech Stack

| Component              | Technology     |
| ---------------------- | -------------- |
| **Frontend**           | Python Tkinter |
| **Backend**            | Python         |
| **Database**           | MySQL          |
| **Charts**             | Matplotlib     |
| **GUI Framework**      | Tkinter + TTK  |
| **Database Connector** | PyMySQL        |

## System Requirements

### Minimum Requirements

- **OS:** Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python:** 3.7 or higher
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 100MB free space
- **Database:** MySQL 5.7 or higher

### Required Python Packages

```bash
pymysql>=1.0.0
matplotlib>=3.5.0
tkinter (included with Python)
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/LucIfer-mk/workmanagement.git
cd workmanagement
```

### 2. Install Dependencies

```bash
pip install pymysql matplotlib
```

### 3. Database Setup

#### Create Database

```sql
CREATE DATABASE workplacedb;
USE workplacedb;
```

#### Create Tables

```sql
-- Staff table
CREATE TABLE staff (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
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
    work_email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Staff attendance table
CREATE TABLE staff_attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT,
    attendance_date DATE,
    started_reom TIME,
    end_time TIME,
    total_hours DECIMAL(4,2),
    FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE
);

-- Payment statements table
CREATE TABLE statement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT,
    payment_date DATE,
    gross_pay DECIMAL(10,2),
    tax_deductions DECIMAL(10,2),
    net_pay DECIMAL(10,2),
    payment_method VARCHAR(50),
    remarks TEXT,
    FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE
);
```

### 4. Configure Database Connection

Update the database connection parameters in the code:

```python
conn = pymysql.connect(
    host="localhost",        # Your MySQL host
    user="root",            # Your MySQL username
    password="your_password", # Your MySQL password
    database="workplacedb"   # Database name
)
```

### 5. Run the Application

```bash
python main.py  # or whatever your main file is named
```

## Database Schema

### Entity Relationship Diagram

```
┌─────────────┐       ┌──────────────────┐       ┌─────────────┐
│    STAFF    │──────▶│ STAFF_ATTENDANCE │       │  STATEMENT  │
├─────────────┤       ├──────────────────┤       ├─────────────┤
│ id (PK)     │       │ id (PK)          │       │ id (PK)     │
│ name        │       │ staff_id (FK)    │       │ staff_id(FK)│
│ address     │       │ attendance_date  │       │ payment_date│
│ dob         │       │ started_reom     │       │ gross_pay   │
│ contact     │       │ end_time         │       │ tax_deduct. │
│ emergency_. │       │ total_hours      │       │ net_pay     │
│ account_no  │       └──────────────────┘       │ payment_met │
│ ird_number  │                                  │ remarks     │
│ account_name│                                  └─────────────┘
│ bank_name   │
│ position    │
│ work_type   │
│ pay_rate    │
│ department  │
│ work_email  │
│ created_at  │
└─────────────┘
```

## Application Structure

```
workmanagement/
├── main.py                 # Main application entry point
├── adminpage.py           # Admin dashboard module
├── database/
│   ├── connection.py      # Database connection utilities
│   └── queries.sql        # SQL queries and schema
├── gui/
│   ├── staff_management.py # Staff CRUD operations
│   ├── payroll.py         # Salary processing
│   └── reports.py         # Report generation
├── utils/
│   ├── calculations.py    # Payroll calculations
│   └── validators.py      # Input validation         
├── docs/
│   └── README.md          # This documentation
└── requirements.txt       # Python dependencies
```

## User Guide

### Getting Started

1. **Launch the Application**

   - Run the main Python file
   - The admin dashboard will open in full-screen mode

2. **Navigation**
   - Use the navigation buttons at the top
   - Each module has its own window/interface
   - Use the Exit button to close individual windows

### Admin Dashboard Overview

The main dashboard displays:

- **Budget Overview:** Current budget allocation
- **Expenses Till Date:** Total expenses incurred
- **Income Till Date:** Total income generated
- **Income vs. Expenses Chart:** Visual representation of financial data

## Admin Dashboard

### 1. Add Staff Module

**Purpose:** Register new employees in the system

**Required Information:**

- **Personal Details:** Name, Address, Date of Birth, Contact, Emergency Contact
- **Financial Details:** Bank Account Number, Account Name, Bank Name, IRD Number
- **Work Details:** Position, Pay Rate, Work Email, Work Type, Department

**Process:**

1. Click "Add Staff" from the navigation menu
2. Fill all required fields
3. Click "Save" to add the staff member
4. System validates all fields before saving

### 2. Manage Staff Module

**Purpose:** View, update, or remove existing staff members

**Features:**

- **View Staff:** Display all staff in a searchable table
- **Update Details:** Modify staff information through popup forms
- **Remove Staff:** Delete staff records (with confirmation dialog)

**Important Notes:**

- Removing staff will delete all associated records (attendance, payments)
- Update forms are pre-filled with current information
- Changes are immediately reflected in the database

### 3. Pay Salary Module

**Purpose:** Process payroll and generate payslips

**Calculation Logic:**

```
Gross Pay = Hours Worked × Pay Rate
Tax Deduction = Gross Pay × 20%
Net Pay = Gross Pay - Tax Deduction
```

**Process:**

1. System displays all staff with worked hours
2. Select employee to pay
3. Review payslip details
4. Confirm payment to save to database

**Generated Payslip Includes:**

- Employee information
- Hours worked and pay rate
- Gross pay calculation
- Tax deductions
- Net pay amount
- Payment date and method

### 4. Statements Module

**Purpose:** View payment history and financial records

**Features:**

- Scrollable list of all payment statements
- Complete payment details for each transaction
- Search and filter capabilities
- Export functionality

### 5. Settings Module

**Purpose:** System configuration and administration

**Available Options:**

- User management
- System preferences
- Logout functionality
- Database maintenance

## API Documentation

### Database Functions

#### Staff Management

```python
# Add new staff member
def add_staff(staff_data):
    """
    Insert new staff record into database
    Args: staff_data (dict) - Staff information
    Returns: bool - Success status
    """

# Update staff information
def update_staff(staff_id, updated_data):
    """
    Update existing staff record
    Args: staff_id (int), updated_data (dict)
    Returns: bool - Success status
    """

# Remove staff member
def remove_staff(staff_id):
    """
    Delete staff and related records
    Args: staff_id (int)
    Returns: bool - Success status
    """
```

#### Payroll Functions

```python
# Calculate salary
def calculate_salary(staff_id, hours_worked):
    """
    Calculate gross pay, taxes, and net pay
    Args: staff_id (int), hours_worked (float)
    Returns: dict - Payment breakdown
    """

# Process payment
def process_payment(payment_data):
    """
    Record payment in statements table
    Args: payment_data (dict)
    Returns: bool - Success status
    """
```

## Troubleshooting

### Common Issues

#### 1. Database Connection Error

**Problem:** `pymysql.err.OperationalError: (2003, "Can't connect to MySQL server")`

**Solutions:**

- Verify MySQL server is running
- Check connection parameters (host, user, password)
- Ensure database 'workplacedb' exists
- Verify user permissions

#### 2. Foreign Key Constraint Error

**Problem:** Cannot delete staff due to foreign key constraints

**Solution:**

- The updated code handles this by deleting related records first
- Ensure you're using the fixed version of the remove_staff function

#### 3. GUI Not Displaying Properly

**Problem:** Windows appear too small or elements are misaligned

**Solutions:**

- Check screen resolution compatibility
- Update Tkinter to latest version
- Ensure all required fonts are installed

#### 4. Import Errors

**Problem:** `ModuleNotFoundError: No module named 'pymysql'`

**Solution:**

```bash
pip install pymysql matplotlib
```

### Debug Mode

Enable debug mode by adding this to your code:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Log Files

The application creates log files in:

- **Windows:** `%APPDATA%/WorkManagement/logs/`
- **macOS:** `~/Library/Logs/WorkManagement/`
- **Linux:** `~/.config/WorkManagement/logs/`

## Performance Optimization

### Database Optimization

1. **Index frequently queried columns:**

   ```sql
   CREATE INDEX idx_staff_name ON staff(name);
   CREATE INDEX idx_attendance_date ON staff_attendance(attendance_date);
   ```

2. **Regular database maintenance:**
   ```sql
   OPTIMIZE TABLE staff, staff_attendance, statement;
   ```

### Application Performance

- Use connection pooling for database connections
- Implement data caching for frequently accessed records
- Optimize GUI rendering for large datasets

## Security Considerations

### Database Security

- Use environment variables for database credentials
- Implement SQL injection protection (already using parameterized queries)
- Regular database backups

### Application Security

- Input validation on all user inputs
- Secure storage of sensitive information
- User access control and authentication

## Future Enhancements

### Planned Features

- [ ] Employee self-service portal
- [ ] Advanced reporting and analytics
- [ ] Email notifications for payroll
- [ ] Mobile application support
- [ ] Integration with accounting software
- [ ] Multi-language support
- [ ] Role-based access control
- [ ] Automated backup system

### Technical Improvements

- [ ] Migration to web-based interface
- [ ] REST API development
- [ ] Unit testing implementation
- [ ] Continuous integration setup
- [ ] Docker containerization

## Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Coding Standards

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include error handling
- Write unit tests for new features

### Bug Reports

When reporting bugs, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs. actual behavior
- Error messages and stack traces

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:

- **GitHub Issues:** [Create an issue](https://github.com/LucIfer-mk/workmanagement/issues)
- **Email:** [Contact developer]
- **Documentation:** This README file

## Acknowledgments

- Python Software Foundation for Python
- MySQL for the database system
- Matplotlib for charting capabilities
- Tkinter for the GUI framework

---

**Project Status:** Active Development  
**Version:** 1.0.0  
**Last Updated:** August 2025  
**Developer:** Manoj Kapri (LucIfer-mk)
