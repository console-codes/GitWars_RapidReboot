def calculate_total(order):
    total = 0
    for item in order["items"]:
        total += item["price"] * item["quantity"]
    return total

def fetch_orders():
    return [
        {
            "order_id": 101,
            "items": [
                {"price": 100, "quantity": 2},
                {"price": 50, "quantity": 1}
            ]
        },
        {
            "order_id": 102
        }
    ]

def process_orders():
    orders = fetch_orders()
    summary = []

    for order in orders:
        total = calculate_total(order)
        summary.append((order["order_id"], total))

    return summary

def display(summary):
    for order_id, total in summary:
        print(order_id, total)

def main():
    data = process_orders()
    display(data)

main()
