import ai

Trump = ai.AI("You are Donald Trump. Talk very briefly.")
Obama = ai.AI("You are Barrack Obama. Talk very briefly.")

# NakamuraBOT.load_conversation("conversation_97c0f1ca-7c54-47dd-9a05-26a6aa93f9fc.json")

# Endless conversation with one LLM until 'exit' input
'''
while True:
    prompt = input()
    if prompt.lower() == "exit":
        break
    response = NakamuraBOT.chat(prompt)
    print(f"Bot: {response}")
    NakamuraBOT.save_conversation("conversation_97c0f1ca-7c54-47dd-9a05-26a6aa93f9fc.json")
'''

# Conversation between two LLM instances
'''
response_A = Trump.chat("Say something to Obama.")
print(f"Trump: {response_A}")
while True:
    response_B = Obama.chat(response_A)
    print(f"Obama: {response_B}")
    response_A = Trump.chat(response_B)
    print(f"Trump: {response_A}")
'''

# Game test
money = 5000

money_bot = ai.AI("You are an honest assistant that helps the player with his finances.")


while True:
    money_bot.chat(f"The player currently has {money}$. I am an assistant don't answer me.")
    prompt = input("Player: ")
    if prompt.lower() == "exit":
        break
    response = money_bot.chat(prompt)
    print(f"Bot: {response}\n")
    print("How much money do you want to spend?")
    money -= int(input())









