threshold = 50

def check_temperature(value):
    if value > threshold:
        status = "HIGH"
    elif value < 0:
        status = "LOW"
    return status

def get_sensor_readings():
    return {
        "Sensor-A": [10, 20, 30],
        "Sensor-B": [55, 60],
        "Sensor-C": [15]
    }

def analyze_readings():
    sensors = get_sensor_readings()
    report = []

    for name in sensors:
        for reading in sensors[name]:
            status = check_temperature(reading)
            report.append((name, reading, status))

    return report

def display(report):
    for name, reading, status in report:
        print(name, reading, status)

def main():
    data = analyze_readings()
    display(data)

main()
