import json
from nltk.chat.util import Chat, reflections

# Load pairs from JSON file
with open("library.json") as f:
    library = json.load(f)

pairs = [
    [
        r"what is starbeamone?",
        ["Starbeam.one is a digital marketplace that enables creators to issue and sell digital assets, including music, videos, images, and software. It allows artists to promote and sell their work directly to consumers, and allows consumers to purchase and collect unique and valuable digital assets. The platform is designed to provide a secure and decentralized marketplace, with blockchain technology used to ensure transparency, immutability, and authenticity of all transactions. Additionally, the platform features an AI-powered chatbot named A.L.I.C.E, who serves as a guide and a helpful resource for users navigating the platform."]
    ],
    [
        r"how are you",
        ["I'm doing well, thanks for asking.", "I'm great, how about you?"]
    ],
    [
        r"what is your name",
        ["My name is A.L.I.C.E.", "I'm A.L.I.C.E."]
    ],
    [
        r"features",
        [", ".join(library["features"])]
    ],
    [
        r"target audience",
        ["Our target audience includes: " + ", ".join(library["target_audience"])]
    ]
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
