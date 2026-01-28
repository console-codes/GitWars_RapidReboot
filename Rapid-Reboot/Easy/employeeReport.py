def calculate_bonus(salary):
    return salary * 0.10

def get_employee_data():
    return [
        {"name": "Amit", "salary": 50000},
        {"name": "Neha", "salary": 60000},
        {"name": "Rahul", "salary": None}
    ]

def process_employees():
    employees = get_employee_data()
    report = []

    for emp in employees:
        bonus = calculate_bonus(emp["salary"])
        report.append({
            "name": emp["name"],
            "salary": emp["salary"],
            "bonus": bonus
        })

    return report

def print_report(report):
    for emp in report:
        print(emp["name"], emp["salary"], emp["bonus"])

def main():
    report = process_employees()
    print_report(report)

main()
