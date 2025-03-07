from random import randint, choice


class Player:
    def __init__(self, name: str = None, age: int = None,
                 ability: int = None, position: str = None):
        self.name = name if name else \
            (generate_random_name("first_names_latinized.csv",
                                  "last_names_latinized.csv"))
        self.age = age if age else randint(15, 40)
        self.ability = ability if ability else randint(0, 100)
        self.position = position if position else generate_random_position()

    def __str__(self):
        return f"{self.name}. {self.age} years old. {self.position} with {self.ability} ability."


def generate_random_position():  # Internal validation function
    valid_positions = ["GK", "DEF", "MID", "ATT"]
    pos = choice(valid_positions)
    return pos


def gen_random_pos():
    positions = ["GK", "DEF", "MID", "ATT"]
    index = randint(0, 3)
    return positions[index]


def generate_random_name(first_names_file, last_names_file):
    """Generates a random full name from two newline-separated CSV files."""
    try:
        with open(first_names_file, 'r', encoding='utf-8') as f_first:
            first_names = [line.strip() for line in f_first]

        with open(last_names_file, 'r', encoding='utf-8') as f_last:
            last_names = [line.strip() for line in f_last]

        first_name = choice(first_names)
        last_name = choice(last_names)
        return f"{first_name} {last_name}"

    except Exception as e:
        return f"An error occurred: {e}"


class Team:
    def __init__(self, players: list = None):
        self.players = players

    def print_team(self):
        for player in self.players:
            print(player)





