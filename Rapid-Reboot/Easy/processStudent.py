def convert_to_int(value):
    return int(value)

def get_student_data():
    return [
        {"roll": "101", "age": "18"},
        {"roll": "102", "age": "19"},
        {"roll": "103", "age": "N/A"}
    ]

def process_students():
    students = get_student_data()
    processed = []

    for s in students:
        roll = convert_to_int(s["roll"])
        age = convert_to_int(s["age"])
        processed.append((roll, age))

    return processed

def main():
    data = process_students()
    for d in data:
        print(d)

main()
