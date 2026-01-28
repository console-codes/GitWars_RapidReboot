def analyze_marks(marks):
    averages = []
    for i in range(len(marks)):
        avg = (marks[i] + marks[i+1]) / 2
        averages.append(avg)
    return averages

def get_marks():
    return [70, 80, 90]

def generate_report():
    marks = get_marks()
    return analyze_marks(marks)

def main():
    report = generate_report()
    print(report)

main()
