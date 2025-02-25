import ai

Trump = ai.AI("You are Donald Trump. Talk very briefly.")
Obama = ai.AI("You are Barrack Obama. Talk very briefly.")

# NakamuraBOT.load_conversation("conversation_97c0f1ca-7c54-47dd-9a05-26a6aa93f9fc.json")

'''
while True:
    prompt = input()
    if prompt.lower() == "exit":
        break
    response = NakamuraBOT.chat(prompt)
    print(f"Bot: {response}")
    NakamuraBOT.save_conversation("conversation_97c0f1ca-7c54-47dd-9a05-26a6aa93f9fc.json")
'''

response_A = Trump.chat("Say something to Obama.")
print(f"Trump: {response_A}")
while True:
    response_B = Obama.chat(response_A)
    print(f"Obama: {response_B}")
    response_A = Trump.chat(response_B)
    print(f"Trump: {response_A}")





