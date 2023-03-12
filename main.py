import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hi there!", "Hello!", "Hey!"]
    ],
]

def main():
    print("A.L.I.C.E: Hi, I'm A.L.I.C.E. How can I help you today?")

    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)

        print("A.L.I.C.E:", response)


if __name__ == "__main__":
    main()
