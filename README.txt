# Payroll Management System

This Python program is designed to help administrators manage employee payroll by calculating gross pay, net pay, and checking if employees meet minimum weekly hours. It includes a login system for security and allows for viewing employee payroll data.

## Features

1. **Login System**:
    - The program is secured with login credentials.
    - Default login credentials:
      - **Username**: `admin`
      - **Password**: `password`

2. **Employee Payroll Calculation**:
    - **Gross Pay**: Calculated based on the number of hours worked and hourly rate. Includes overtime pay for hours worked beyond the standard 40 hours.
    - **Net Pay**: Calculated after applying a user-defined percentage for deductions.
    - **Deductions**: The difference between gross pay and net pay.

3. **Check Minimum Hours**:
    - The program verifies if the employee met the minimum weekly working hours (32 hours by default). If the employee worked fewer hours, a notification is provided.

4. **Employee Data Management**:
    - Allows for entering new employee data and viewing employee details by ID.

5. **Summary of All Employees**:
    - Displays the total net pay and total deductions for all employees entered into the system.

## Default Values

- **Minimum Weekly Hours**: `32 hours`
- **Standard Weekly Hours**: `40 hours`
- **Overtime Pay Multiplier**: `1.5x` for hours worked beyond 40.

## How to Use

### Step 1: Run the Program
```bash
python payroll_system.py
