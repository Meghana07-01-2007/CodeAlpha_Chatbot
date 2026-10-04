def chatbot():
    print("Hello! I am a simple Python chatbot.")
    print("You can say hello, ask how I am, or say bye.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! Nice to meet you.")

        elif user_input in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great! Thanks for asking.")

        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I'm a simple Python chatbot created for my CodeAlpha project.")

        elif user_input in ["what can you do", "help"]:
            print("Bot: I can respond to greetings, simple questions, and goodbye messages.")

        elif user_input in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()