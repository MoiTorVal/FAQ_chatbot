import sys
import os

# Add src folder to Python path so it can find chatbot.py
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from chatbot import load_collection, ask_chatbot
from langchain_ollama import OllamaLLM

def main():
    print("Loading chatbot...")
    collection = load_collection()
    llm = OllamaLLM(model="llama3")
    print("Chatbot ready! Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = ask_chatbot(collection, llm, user_input)
        print(f"\nBot: {response}\n")

if __name__ == "__main__":
    main()