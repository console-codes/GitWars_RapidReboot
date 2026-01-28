def format_message(msg):
    return msg.strip().upper()

def get_messages():
    return ["hello", "world", None]

def process_messages():
    messages = get_messages()
    formatted = []

    for m in messages:
        formatted.append(format_message(m))

    return formatted

def main():
    msgs = process_messages()
    for m in msgs:
        print(m)

main()
