def calculate_average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks)

def normalize_marks(marks):
    normalized = []
    for m in marks:
        normalized.append(m / 100)
    return normalized

def get_student_marks():
    return {
        "Alice": [80, 90, 85],
        "Bob": [70, 60, 75],
        "Charlie": []
    }

def process_students():
    students = get_student_marks()
    results = {}

    for name in students:
        marks = students[name]
        avg = calculate_average(marks)
        norm = normalize_marks(marks)

        results[name] = {
            "average": avg,
            "normalized": norm
        }

    return results

def print_report(report):
    for student in report:
        print(student)
        print(report[student])
        print("-" * 20)

def main():
    report = process_students()
    print_report(report)

main()
