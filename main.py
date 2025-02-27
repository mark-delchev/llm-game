import ai
from game import Player

# Game test

starting_eleven = [str(player) for player in [Player() for _ in range(11)]]
for player in starting_eleven:
    print(player)

assistant = ai.AI("You are a football assistant manager. Listen to the player and help him."
                  "Be as brief as possible. Don't hallucinate, work only with the "
                  "available information!")

while True:
    assistant.chat(f"Here is the current squad: {starting_eleven}. This is a pre-coded message don't "
                   f"answer.")
    prompt = input("Player: ")
    if prompt.lower() == "exit":
        break
    response = assistant.chat(prompt)
    print(f"AI assistant: {response}\n")










