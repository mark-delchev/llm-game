import ai
from random import randint


def set_position(pos):  # Internal validation function
    valid_positions = ["GK", "DEF", "MID", "ATT"]
    if pos not in valid_positions:
        raise ValueError(f"Invalid position: {pos}")  # Raise error if invalid
    return pos  # Return the position if it's valid


def gen_random_pos():
    positions = ["GK", "DEF", "MID", "ATT"]
    index = randint(0, 3)
    return positions[index]


class Player:
    def __init__(self, name, age, ability, position):
        self.name = name
        self.age = age
        self.ability = ability
        self.position = set_position(position)

    def __str__(self):
        return f"{self.name}. {self.age} years old. {self.position} with {self.ability} ability."


player1 = Player("Ivan", randint(15, 45), randint(0, 100), gen_random_pos())
player2 = Player("Pesho", randint(15, 45), randint(0, 100), gen_random_pos())
player3 = Player("Tosho", randint(15, 45), randint(0, 100), gen_random_pos())

player_lst = [str(player1), str(player2), str(player3)]


manager_assistant = ai.AI("You are an assistant coach. Help the manager make decisions. Be brief!")

while True:
    manager_assistant.chat(f"Look and remember this set of players {player_lst}$. "
                           f"This is a preprogrammed message. "
                           f"Don't answer now.")
    print(player_lst)
    prompt = input("Player: ")
    if prompt.lower() == "exit":
        break
    response = manager_assistant.chat(prompt)
    print(f"Bot: {response}\n")





