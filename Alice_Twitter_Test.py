import os
import openai
import tweepy
import json

# Set up OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Set up Twitter API keys
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Define function to generate a response from the GPT model
def generate_response(prompt):
    # Generate a response from the GPT model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the response
    message = response.choices[0].text.strip()

    return message

# Define function to prompt the user for input and generate a response
def chat():
    # Load library from JSON file
    with open("library.json", encoding="utf-8") as f:
        library = json.load(f)

    # Create list of questions
    questions = [pair["question"] for pair in library["pairs"]]

    print("A.L.I.C.E.: Hi, I'm A.L.I.C.E. How can I help you today?")
    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue

        prompt = ""
        for pair in library["pairs"]:
            if user_input.lower() in pair["question"].lower():
                prompt += f"User: {user_input}\nA.L.I.C.E.: {pair['response']}\n"
                break
        else:
            prompt = f"User: {user_input}\nA.L.I.C.E.: I'm sorry, I don't have an answer for that. Here are some available questions:\n"
            for i, question in enumerate(questions):
                prompt += f"{i+1}. {question}\n"

        response = generate_response(prompt)
        if response.startswith("tweet:"):
            tweet = response[len("tweet:"):]
            twitter_api.update_status(tweet)
            print("A.L.I.C.E.: I just tweeted this:", tweet)
        else:
            print("A.L.I.C.E.:", response)

# Run the chat function
if __name__ == "__main__":
    chat()
    # Save library to JSON file
    with open("library.json", mode="w", encoding="utf-8") as f:
        json.dump({"pairs": pairs}, f, ensure_ascii=False)

# Changelog:
# ALICE_Twitter Change (v1.0) - added Twitter functionality to A.L.I.C.E. by incorporating Tweepy and adding the ability to tweet responses
