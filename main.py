import random

responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "what's your name": "I'm a chatbot. What's yours?",
    "default": "Sorry, I don't understand that.",
}


def get_response(user_input):
    input_lower = user_input.lower()
    if input_lower in responses:
        return responses[input_lower]
    else:
        return responses["default"]


def chat():
    print("Welcome! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)


def main():
    chat()


if __name__ == "__main__":
    main()
