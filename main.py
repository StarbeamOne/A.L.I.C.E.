import os

def read_library():
    # Create the library file if it doesn't exist
    if not os.path.exists("library.txt"):
        with open("library.txt", "w") as f:
            f.write("What is your name?:My name is A.L.I.C.E.\nHow old are you?:I was activated in 1995, so I am over 25 years old.\nWhat can you do?:I can help you with a variety of tasks, from answering questions to playing games.")

    # Read the library file
    with open("library.txt", "r") as f:
        library = f.read().split("\n")

    # Create a dictionary of questions and answers
    pairs = {}
    for pair in library:
        if pair:
            question, answer = pair.split(":")
            pairs[question.lower()] = answer

    return pairs

def chat():
    # Load library
    library = read_library()

    # Create list of questions
    questions = list(library.keys())

    print("A.L.I.C.E.: Hi, I'm A.L.I.C.E. How can I help you today?")
    while True:
        user_input = input("You: ")
        response = library.get(user_input.lower())
        if response:
            print("A.L.I.C.E.:", response)
        else:
            print("A.L.I.C.E.: I'm sorry, I don't have an answer for that. Here are some available questions:")
            for question in questions:
                print(f"- {question.capitalize()}")

if __name__ == "__main__":
    print("A.L.I.C.E. v8.0 Text Library Edition")
    chat()
