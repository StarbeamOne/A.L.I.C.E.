import csv
import os.path
from random import choice

from nltk.chat.util import Chat, reflections

# Check if library file exists, create one if not
if not os.path.isfile("library.csv"):
    with open("library.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["question", "response"])
        writer.writerow(["What is Starbeam One?", "Starbeam.one is a digital marketplace that enables creators to issue and sell digital assets, including music, videos, images, and software. It allows artists to promote and sell their work directly to consumers, and allows consumers to purchase and collect unique and valuable digital assets. The platform is designed to provide a secure and decentralized marketplace, with blockchain technology used to ensure transparency, immutability, and authenticity of all transactions. Additionally, the platform features an AI-powered chatbot named A.L.I.C.E, who serves as a guide and a helpful resource for users navigating the platform."])

# Load library from CSV file
with open("library.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader) # skip header row
    library = [{"question": row[0], "response": row[1]} for row in reader]

# Create pairs from library
pairs = [(pair["question"], pair["response"]) for pair in library]

# Add default reflection pairs
reflections[""] = ""

# Create chat bot
chatbot = Chat(pairs, reflections)

def main():
    print("A.L.I.C.E: Hi, I'm A.L.I.C.E. How can I help you today?")
    while True:
        user_input = input("You: ")
        if not user_input:
            print("Available questions:")
            for i, pair in enumerate(library):
                print(f"{i+1}. {pair['question']}")
            continue
        if user_input.isdigit() and int(user_input) in range(1, len(library)+1):
            response = library[int(user_input)-1]["response"]
        else:
            response = chatbot.respond(user_input)
            if not response:
                print("A.L.I.C.E.: I'm sorry, I didn't understand your question. Here are the available questions:")
                for i, pair in enumerate(library):
                    print(f"{i+1}. {pair['question']}")
                continue
        print("A.L.I.C.E:", response)

if __name__ == "__main__":
    print("A.L.I.C.E. v6.1")
    main()
