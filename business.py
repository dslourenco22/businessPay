#Lourenco DaSilva
#Linkedin: https://www.linkedin.com/in/lourenco-dasilva-b69986234/

# Constants
MINIMUM_HOURS = 32
OVERTIME_MULTIPLIER = 1.5
STANDARD_HOURS = 40
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Function to calculate gross pay
def calculate_gross_pay(hours_worked, hourly_rate):
    if hours_worked <= STANDARD_HOURS:
        return hours_worked * hourly_rate
    else:
        regular_pay = STANDARD_HOURS * hourly_rate
        overtime_hours = hours_worked - STANDARD_HOURS
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        return regular_pay + overtime_pay

# Function to calculate net pay
def calculate_net_pay(gross_pay, net_percentage):
    return gross_pay * (net_percentage / 100)

# Function to check if employee met minimum weekly hours
def check_minimum_hours(hours_worked):
    if hours_worked < MINIMUM_HOURS:
        return "Employee did not meet the minimum weekly hours."
    else:
        return "Employee met the minimum weekly hours."

# Function to handle the login process
def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("Login Successful!")
            break
        else:
            print("Username or Password is incorrect! Please Try Again.")

# Function to display employee details
def display_employee_data(employee_data, employee_id):
    if employee_id in employee_data:
        print(f"\nEmployee ID: {employee_id}")
        print(f"Gross Pay: ${employee_data[employee_id]['gross_pay']:.2f}")
        print(f"Net Pay: ${employee_data[employee_id]['net_pay']:.2f}")
        print(f"Deductions: ${employee_data[employee_id]['deductions']:.2f}")
        print(f"Hours Worked: {employee_data[employee_id]['hours_worked']}")
        print("-" * 40)
    else:
        print(f"No data found for Employee ID: {employee_id}")

# Main program
def main():
    login()
    
    total_net_pay = 0
    total_deductions = 0
    employee_data = {}  # Dictionary to store employee data
    
    while True:
        print("\nOptions:")
        print("1. Enter new employee data")
        print("2. View employee data by ID")
        print("3. Quit")
        option = input("Choose an option: ")
        
        if option == '1':
            # Enter new employee data
            employee_id = input("Enter employee ID: ")
            hourly_rate = float(input("Enter hourly rate for employee: "))
            net_percentage = float(input("Enter net percentage for employee (e.g., 85 for 85%): "))
            hours_worked = float(input("Enter number of hours worked: "))
            
            # Calculate gross pay
            gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
            
            # Calculate net pay
            net_pay = calculate_net_pay(gross_pay, net_percentage)
            deductions = gross_pay - net_pay
            
            # Check if employee met minimum hours
            min_hours_msg = check_minimum_hours(hours_worked)
            
            # Display results
            print(f"\nEmployee ID: {employee_id}")
            print(f"Gross Pay: ${gross_pay:.2f}")
            print(f"Net Pay: ${net_pay:.2f}")
            print(f"Deductions: ${deductions:.2f}")
            print(min_hours_msg)
            print("-" * 40)
            
            # Store employee data in dictionary
            employee_data[employee_id] = {
                'gross_pay': gross_pay,
                'net_pay': net_pay,
                'deductions': deductions,
                'hours_worked': hours_worked
            }
            
            # Update totals
            total_net_pay += net_pay
            total_deductions += deductions
        
        elif option == '2':
            # View employee data by ID
            employee_id = input("Enter employee ID to look up: ")
            display_employee_data(employee_data, employee_id)
        
        elif option == '3':
            # Quit the program
            break
        
        else:
            print("Invalid option, please try again.")
    
    # Display final totals
    print("\nSummary of all employees:")
    print(f"Total Net Pay: ${total_net_pay:.2f}")
    print(f"Total Deductions: ${total_deductions:.2f}")

if __name__ == "__main__":
    main()
