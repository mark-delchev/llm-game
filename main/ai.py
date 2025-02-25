import uuid
import ollama
import sys
import time
import json

DEFAULT_MODEL = "Tohur/natsumura-storytelling-rp-llama-3.1:latest"
DEFAULT_SYSTEM_INSTRUCTION = "You are a helpful AI assistant."  # Define a default instruction


class AI:
    def __init__(self, system_instruction=DEFAULT_SYSTEM_INSTRUCTION, model=DEFAULT_MODEL, conversation_history=None,
                 conversation_id=None):
        self.system_instruction = system_instruction
        self.model = model
        self.conversation_id = conversation_id if conversation_id else str(
            uuid.uuid4())  # Generate a conversation ID if one does not exist.

        # Initialize conversation history correctly
        self.conversation_history = conversation_history if conversation_history is not None else [
            {
                "temperature": 1.0,
                "repetition_penalty": 1.05,
                "top_p": 0.95,
                "top_k": 40,
                "min_p": 0.05,
                "role": "system",
                "content": self.system_instruction
            }
        ]

    def live_chat(self):
        print("Chat with the model (type 'exit' to quit):")

        while True:
            question = input("You: ")

            if question.lower() == "exit":
                print("Ending the chat. Goodbye!")
                break

            # Append user input to conversation history
            self.conversation_history.append({"role": "user", "content": question})

            print("Model: ", end="", flush=True)
            response_text = ""

            # Stream response from the model
            for chunk in ollama.chat(model=self.model, messages=self.conversation_history, stream=True):
                token = chunk["message"]["content"]
                print(token, end="", flush=True)
                sys.stdout.flush()
                time.sleep(0.02)  # Adjust speed

                response_text += token

            print("\n")  # Newline after response
            self.conversation_history.append({"role": "assistant", "content": response_text})

    def chat(self, prompt=""):
        # Append user input to conversation history
        self.conversation_history.append({"role": "user", "content": prompt})
        response_text = ""

        # Stream response from the model
        for chunk in ollama.chat(model=self.model, messages=self.conversation_history, stream=True):
            token = chunk["message"]["content"]
            response_text += token

        self.conversation_history.append({"role": "assistant", "content": response_text})
        return response_text

    def save_conversation(self, filename=None):
        """Saves the conversation history to a JSON file."""
        if filename is None:
            filename = f"conversation_{self.conversation_id}.json"  # Generate a filename based on the conversation ID if one is not provided.
        data = {
            "conversation_id": self.conversation_id,
            "conversation_history": self.conversation_history
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_conversation(self, filename):
        """Loads the conversation history from a JSON file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.conversation_id = data.get("conversation_id",
                                                str(uuid.uuid4()))  # If there is no conversation ID, generate a new one.
                self.conversation_history = data["conversation_history"]
                return self.conversation_history
        except FileNotFoundError:
            return None


