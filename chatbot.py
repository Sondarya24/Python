print("Welcome! to Chatbot")
print("Type bye to end the chat")

while True:
    user_input = input("You: ")

    if "hello" in user_input or "hii" in user_input:
        print("Chatbot: Hii! How can i help you?")
    elif "how are you" in user_input:
        print("Chatbot: I am fine, i am virtual body.")
    elif "What is your name? " in user_input:
        print("Chatbot: I am chatty chatbot")
    elif "bye" in user_input:
        print("Chatbot: Bye,have a nice day.")
        break
    else:
        print("SOrry, i don't understand.")