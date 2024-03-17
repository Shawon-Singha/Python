def calculate_salary(employee_id, total_hours, hourly_rate):
    days_off = ['Friday', 'Saturday']
    
    total_salary = 0
    for day in range(1, 31):  # Assuming a month has 30 days
        if day % 7 not in [5, 6]:  # Assuming the month starts from Monday (0-base indexing)
            total_salary += hourly_rate * total_hours
    
    print(f"Employee ID: {employee_id}")
    print(f"Salary for the month: ${total_salary:.2f}")


employee_id = input("Enter employee's ID: ")
total_hours = float(input("Enter total worked hours of the month: "))
hourly_rate = float(input("Enter the amount received per hour: "))

calculate_salary(employee_id, total_hours, hourly_rate)
