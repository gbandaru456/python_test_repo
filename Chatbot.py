responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bunch of code, but I'm doing great!",
    "what is your name": "I'm ChatPy, your Python chatbot.",
    "bye": "Goodbye! Have a great day!"
}
def chatbot():
    print("Chatpy:Hello type 'bye' to exit.")
    while True:
        user_input = input('You: ').lower()
        if user_input in responses:
            print("Chatpy:",responses[user_input])
            if user_input == "bye":
                break
            else:
                print("ChatPy: I'm not sure how to respond to that.")

chatbot()
