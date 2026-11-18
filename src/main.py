from src.llm import generate_response, clear_conversation_history

def process_command(command):
    command = command.strip().lower()

    if command == "hello":
        return "Hello! I'm NEXA. How can I assist you?"

    elif command == "help":
        return "I'm NEXA, your Neural Executive Assistant."

    elif command == "clear":
        clear_conversation_history()
        return "Conversation memory cleared."

    else:
        return generate_response(command)


def main():
    print("NEXA Initializing...")
    print("Neural Executive Assistant is online.")

    while True:
        command = input("\nYou: ").strip()

        if command.lower() == "exit":
            print("NEXA: Shutting down...")
            break

        if not command:
            continue

        response = process_command(command)
        print(f"NEXA: {response}")


if __name__ == "__main__":
    main()
